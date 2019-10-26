from flask import Flask, jsonify, make_response, abort, request
from flask_cors import CORS
from flask_restful import Resource, Api

from database.querys_survrun_table import SurvrunTableQuerys
from modes.survrim.survrun_goal_location_calculator import SurvrunGoalLocationCalculator
from modes.survrim.survrim_rule_generator import SurvrimRuleGenerator
from modes.survrim.survrim_return_constants import SurvrimReturnConstants
from modes.stronghold.shc_ai_picker import StrongholdAiPicker
import constants
import json

app = Flask(__name__)
api = Api(app)
CORS(app)  # required for cross origin resource sharing error (temp fix)


class SurvrimApi(Resource):
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


api.add_resource(SurvrimApi, constants.API_SURVRIM_GET_CLASS_DATA)


class SurvrunGetConstants(Resource):
    """
    Expose survrim/survrun constants to frontend
    """

    def get(self):
        return SurvrimReturnConstants.survrim_get_constants()


api.add_resource(SurvrunGetConstants, constants.API_SURVRUN_GET_CONSTANTS)


# todo: needs integration test
class SurvrunQueryGetSubmitRuns(Resource):
    def get(self):
        db_query = SurvrunTableQuerys()
        db_data = db_query.survrun_select_query()
        if not db_data:
            abort(400)

        json_components = []
        for row in db_data:
            json_components.append(
                {
                    'id': row.id,
                    'player_class': row.player_class,
                    'target_a': row.target_a,
                    'target_b': row.target_b,
                    'timebox': row.timebox,
                    'completed': row.completed,
                    'time_needed': row.time_needed,
                    'r_count': row.r_count
                }
            )
        if not json_components[0]:
            return jsonify({'Info': 'No data to fetch, table is empty'})

        return jsonify({
            'queryResult': json_components
        })


api.add_resource(SurvrunQueryGetSubmitRuns, constants.API_SURVRUN_GET_ALL_DB_RUN_DATA)


class SurvrunQueryPostRun(Resource):
    def post(self) -> int:
        a = json.loads(request.data)
        run_data = json.loads(request.data)["submitRunFormData"]
        if not run_data or not run_data[0]:
            abort(400)

        player_class = run_data[0]["player_class"]
        target_a = run_data[0]["target_a"]
        target_b = run_data[0]["target_b"]
        timebox = run_data[0]["timebox"]
        time_needed = run_data[0]["time_needed"]
        r_count = run_data[0]["r_count"]
        if 0 < time_needed < timebox:
            completed = "yes"
        else:
            completed = "no"

        db_query = SurvrunTableQuerys()
        status = db_query.survrun_insert_query(player_class=player_class, target_a=target_a,
                                               target_b=target_b, timebox=timebox, time_needed=time_needed,
                                               r_count=r_count, completed=completed)
        return status


api.add_resource(SurvrunQueryPostRun, constants.API_SURVRUN_POST_RUN)


class SurvrunTargetLocationApi(Resource):
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


class StrongholdApi(Resource):
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


@app.route('/')
def landing_page():
    return 'GM-Manager'


@app.errorhandler(404)
def error_not_found(error):
    return make_response(jsonify({'error': '404: Not found'}), 404)


@app.errorhandler(400)
def error_not_found(error):
    return make_response(jsonify({'Bad request': error}), 400)


if __name__ == '__main__':
    app.debug = True  # add debug support
    app.run()
