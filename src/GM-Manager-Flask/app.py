from flask import Flask, jsonify, make_response, abort, request
from flask_cors import CORS
from flask_restful import Resource, Api

from database.query_eso_table import QueryEsoTable
from database.query_survrun_table import QuerySurvrunTable
from modes.survrim.survrun_calculate_statistics import SurvrunCalculateStatistics
from modes.survrim.survrun_goal_location_calculator import SurvrunGoalLocationCalculator
from modes.survrim.survrun_rule_generator import SurvrimRuleGenerator
from modes.survrim.survrim_return_constants import SurvrimReturnConstants
from modes.stronghold.shc_ai_picker import StrongholdAiPicker
from modes.eso.eso_return_constants import EsoReturnConstants
import constants
import json

app = Flask(__name__)
api = Api(app)
CORS(app)  # required for cross origin resource sharing error (temp fix)


class SurvrunGetClassApi(Resource):
    """
    exposes survrun class data
    """

    def get(self):
        player_class = SurvrimRuleGenerator.pick_class()
        player_class_skills = SurvrimRuleGenerator.get_skills_for_class(player_class)

        if not player_class or not player_class_skills:
            abort(400)

        json_model = {
            'survrimData': [
                {
                    'class_info': [
                        {
                            'player_class': player_class,
                            'player_class_skills': player_class_skills
                        }
                    ]
                }
            ]
        }

        return json_model


api.add_resource(SurvrunGetClassApi, constants.API_SURVRIM_GET_CLASS_DATA)


class SurvrunGetConstants(Resource):
    """
    exposes survrim/survrun constants to frontend
    """

    def get(self):
        return SurvrimReturnConstants.survrim_get_constants()


api.add_resource(SurvrunGetConstants, constants.API_SURVRUN_GET_CONSTANTS)


class SurvrunQueryGetRuns(Resource):
    """
    exposes all recorded survruns from DB
    """

    def get(self):
        db_query = QuerySurvrunTable()
        db_data = db_query.survrun_select_query()
        if not db_data:
            abort(400)

        json_components = []
        for row in db_data:
            try:
                json_components.append(
                    {
                        'id': row.id,
                        'player_class': row.player_class,
                        'target_a': row.target_a,
                        'target_b': row.target_b,
                        'timebox': row.timebox,
                        'completed': row.completed,
                        'time_needed': row.time_needed,
                        'r_count': row.r_count,
                        'difficulty': row.difficulty
                    }
                )
            except AttributeError:
                abort(500)
        if not json_components[0]:
            return jsonify({'Info': 'No data to fetch, table is empty'})

        return jsonify({
            'queryResult': json_components
        })


api.add_resource(SurvrunQueryGetRuns, constants.API_SURVRUN_GET_ALL_DB_RUN_DATA)


class SurvrunQueryPostRun(Resource):
    """
    POST endpoint to insert a survrun to the DB
    """

    def post(self):
        run_data = json.loads(request.data)["submitRunFormData"]
        if not run_data or not run_data[0]:
            abort(400)

        player_class = run_data[0]["player_class"]
        target_a = run_data[0]["target_a"]
        target_b = run_data[0]["target_b"]
        timebox = run_data[0]["timebox"]
        time_needed = run_data[0]["time_needed"]
        r_count = run_data[0]["r_count"]
        difficulty = run_data[0]["difficulty"]
        if 0 < time_needed < timebox:
            completed = "yes"
        else:
            completed = "no"

        if not player_class or not target_a or not target_b or not timebox or not time_needed or not difficulty:
            abort(400)

        db_query = QuerySurvrunTable()
        status, msg = db_query.survrun_insert_query(player_class=player_class, target_a=target_a,
                                                    target_b=target_b, timebox=timebox, time_needed=time_needed,
                                                    r_count=r_count, completed=completed, difficulty=difficulty)
        if status is not 200:
            abort(status)
        return make_response(jsonify({'status': status, 'message': msg}))


api.add_resource(SurvrunQueryPostRun, constants.API_SURVRUN_POST_RUN)


class SurvrunTargetLocationApi(Resource):
    """
    exposes survrun target location data
    """

    def get(self):
        survrun = SurvrunGoalLocationCalculator()
        target_a, target_b = survrun.calc_goal_locations()
        timebox, rating = survrun.calc_time_limit_with_randomness(target_a, target_b)
        if not target_a or not target_b or not timebox:
            abort(400)

        json_model = {
            'survrunData': [
                {
                    'id': 1,
                    'target_location_one': target_a,
                    'target_location_two': target_b,
                    'timebox': timebox,
                    'rating': rating
                }
            ]
        }

        return json_model


api.add_resource(SurvrunTargetLocationApi, constants.API_SURVRUN_GET_TARGET_LOCATION)


class SurvrunDeleteRunApi(Resource):
    """
    endpoint to delete a recorded survrun from DB
    """

    def post(self):
        run_id = None
        try:
            run_id = json.loads(request.data)["delete_row_id"]
        except KeyError:
            abort(400)
        if not run_id:
            abort(400)

        db_query = QuerySurvrunTable()
        status, msg = db_query.survrun_delete_record_by_id_query(run_id)
        if status is not 200:
            abort(status)
        return jsonify({'status': status, 'message': msg})


api.add_resource(SurvrunDeleteRunApi, constants.API_SURVRUN_DELETE_RUN)


class SurvrunStatisticsApi(Resource):
    """
    exposes survrun statistics
    """

    def get(self):
        stats_calc = SurvrunCalculateStatistics()
        try:
            stats = stats_calc.get_statistics()
            return jsonify(stats)
        except ConnectionError:
            abort(500)


api.add_resource(SurvrunStatisticsApi, constants.API_SURVRUN_GET_STATISTICS)


class StrongholdApi(Resource):
    """
    exposes shc data
    """

    def post(self):
        ai_count = json.loads(request.data)["shc_ai_battle_player_count"]
        if not ai_count:
            abort(400)
        ai_list = StrongholdAiPicker.pick_random_ai(ai_count)
        ai_list_str = StrongholdAiPicker.format_ai_list(ai_list)
        if not ai_list_str:
            abort(400)

        return {'shcData': [{'ai_battle': ai_list_str}]}


api.add_resource(StrongholdApi, constants.API_STRONGHOLD_GET_AI_BATTLE)


class EsoGetConstantsApi(Resource):
    """
    exposes eso constants
    """

    def get(self):
        return EsoReturnConstants.eso_get_constants()


api.add_resource(EsoGetConstantsApi, constants.API_ESO_GET_CONSTANTS)


class EsoQueryGetDungeonRuns(Resource):
    """
    exposes recorded eso dungeon runs from DB
    """

    def get(self):
        db_query = QueryEsoTable()
        db_data = db_query.eso_select_dungeon_runs_query()
        if not db_data:
            abort(400)

        json_components = []
        for row in db_data:
            try:
                json_components.append(
                    {
                        'id': row.id,
                        'dungeon_name': row.dungeon_name,
                        'player_count': row.player_count,
                        'time_needed': row.time_needed,
                        'hardmode': row.hardmode,
                        'flawless': row.flawless,
                        'wipes': row.wipes,
                        'class_one': row.class_one,
                        'class_two': row.class_two,
                        'class_three': row.class_three,
                        'class_four': row.class_four
                    }
                )
            except AttributeError:
                abort(500)
        if not json_components[0]:
            return jsonify({'Info': 'No data to fetch, table is empty'})

        return jsonify({
            'queryResult': json_components
        })


api.add_resource(EsoQueryGetDungeonRuns, constants.API_ESO_GET_DUNGEON_RUNS)


class EsoQueryPostDungeonRun(Resource):
    """
    POST endpoint to insert a eso dungeon run to the DB
    """

    def post(self):
        run_data = json.loads(request.data)["submitDungeonRunFormData"]
        if not run_data:
            abort(400)

        dungeon_name = run_data["formDungeonName"]
        player_count = run_data["formPlayerCount"]
        time_needed = run_data["formTimeNeeded"]
        hardmode = run_data["formHardmode"]
        flawless = run_data["formFlawless"]
        wipes = run_data["formWipes"]
        class_one = run_data["formClassOne"]
        class_two = run_data["formClassTwo"]
        class_three = run_data["formClassThree"]
        class_four = run_data["formClassFour"]

        if not dungeon_name or not player_count or not time_needed or not hardmode or not flawless \
                or not class_one or not class_two or not class_three or not class_four:
            abort(400)

        db_query = QueryEsoTable()
        status = db_query.eso_insert_dungeon_run_query(dungeon_name=dungeon_name, player_count=player_count,
                                                       time_needed=time_needed, hardmode=hardmode, flawless=flawless,
                                                       wipes=wipes, class_one=class_one, class_two=class_two,
                                                       class_three=class_three, class_four=class_four)

        if status is not 200:
            abort(status)
        return make_response(jsonify({'status': status}))


api.add_resource(EsoQueryPostDungeonRun, constants.API_ESO_POST_DUNGEON_RUN)


class EsoDeleteDungeonRunById(Resource):
    """
    Delete a recorded ESO dungeon run from the DB
    """

    def post(self):
        run_id = None
        try:
            run_id = json.loads(request.data)["delete_row_id"]
        except KeyError:
            abort(400)
        if not run_id:
            abort(400)

        db_query = QueryEsoTable()
        status = db_query.eso_delete_dungeon_run_by_id(run_id)
        if status is not 200:
            abort(status)
        return jsonify({'status': status})


api.add_resource(EsoDeleteDungeonRunById, constants.API_ESO_DELETE_DUNGEON_RUN)


@app.route('/')
def landing_page():
    return 'GM-Manager'


@app.errorhandler(400)
def error_not_found(error):
    return make_response(jsonify({'Bad request': error}), 400)


@app.errorhandler(404)
def error_not_found(error):
    return make_response(jsonify({'error': '404: Not found'}), 404)


@app.errorhandler(500)
def error_not_found(error):
    return make_response(jsonify({'Backend error': 'an internal error occured in backend while processing data: ' +
                                                   error}), 500)


if __name__ == '__main__':
    app.debug = True  # add debug support
    app.run()
