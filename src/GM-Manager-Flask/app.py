import json

from flask import Flask, jsonify, make_response, abort, request
from flask_cors import CORS
from flask_restful import Resource, Api

import constants as c
from database import constants as c_db
from database.query_eso_dungeon_table import QueryEsoDungeonTable
from database.query_eso_raid_table import QueryEsoRaidTable
from database.query_shc_ranking_table import QueryShcRankingTable
from database.query_survrun_table import QuerySurvrunTable
from modes.eso import constants as c_eso
from modes.eso.eso_return_constants import EsoReturnConstants
from modes.misc import constants as c_m
from modes.misc.brainstorm import MiscBrainstorm
from modes.misc.misc_return_constants import MiscReturnConstants
from modes.stronghold import constants as c_shc
from modes.stronghold.shc_ai_picker import StrongholdAiPicker
from modes.survrim import constants as c_sr
from modes.survrim.survrim_return_constants import SurvrimReturnConstants
from modes.survrim.survrun_calculate_statistics import SurvrunCalculateStatistics
from modes.survrim.survrun_goal_location_calculator import SurvrunGoalLocationCalculator
from modes.survrim.survrun_rule_generator import SurvrimRuleGenerator

app = Flask(__name__)
api = Api(app)
CORS(app)  # required for cross origin resource sharing error (temp fix)


class ApiHealthCheck(Resource):
    """
    test endpoint for unit tests and pings
    """
    def get(self):
        return {
            c.KEY_HEALTH_CHECK_RESPONSE: {
                c.KEY_STATUS: c.RESP_OK,
                c.KEY_MESSAGE: c.MSG_HEALTH_CHECK_SUCCESS
            }
        }

    def post(self):
        try:
            payload = json.loads(request.data)
            return {
                c.KEY_HEALTH_CHECK_RESPONSE: {
                    c.KEY_STATUS: c.RESP_OK,
                    c.KEY_MESSAGE: c.MSG_HEALTH_CHECK_SUCCESS,
                    c.KEY_RECEIVED_PAYLOAD: payload
                }
            }
        except Exception:
            return {
                c.KEY_HEALTH_CHECK_RESPONSE: {
                    c.KEY_STATUS: c.RESP_RESOURCE_NOT_FOUND,
                    c.KEY_MESSAGE: c.MSG_HEALTH_CHECK_FAILURE,
                    c.KEY_RECEIVED_PAYLOAD: None
                }
            }


api.add_resource(ApiHealthCheck, c.API_HEALTH_CHECK)


# # # # # # # # # # # # # # # # # # #
# # # # Survrun Api Endpoints # # # #
# # # # # # # # # # # # # # # # # # #

class SurvrunGetClassApi(Resource):
    """
    exposes survrun class data
    """
    def get(self):
        player_class = SurvrimRuleGenerator.pick_class()
        player_class_skills = SurvrimRuleGenerator.get_skills_for_class(player_class)

        if not player_class or not player_class_skills:
            abort(c.RESP_BAD_REQUEST)

        json_model = {
            c_sr.SR_KEY_SURVRIM_DATA: [
                {
                    c_sr.SR_KEY_CLASS_INFO: [
                        {
                            c_sr.SR_KEY_PLAYER_CLASS: player_class,
                            c_sr.SR_KEY_PLAYER_CLASS_SKILLS: player_class_skills
                        }
                    ]
                }
            ]
        }

        return json_model


api.add_resource(SurvrunGetClassApi, c.API_SURVRIM_GET_CLASS_DATA)


class SurvrunGetConstants(Resource):
    """
    exposes survrim/survrun constants to frontend
    """
    def get(self):
        return SurvrimReturnConstants.survrim_get_constants()


api.add_resource(SurvrunGetConstants, c.API_SURVRUN_GET_CONSTANTS)


class SurvrunQueryGetRuns(Resource):
    """
    exposes all recorded survruns from DB
    """
    def get(self):
        db_cursor = QuerySurvrunTable()
        db_data = db_cursor.survrun_select_query()
        if not db_data:
            abort(c.RESP_BAD_REQUEST)

        json_components = []
        for row in db_data:
            try:
                json_components.append(
                    {
                        c_sr.SR_KEY_ID: row.id,
                        c_sr.SR_KEY_PLAYER_CLASS: row.player_class,
                        c_sr.SR_KEY_TARGET_A: row.target_a,
                        c_sr.SR_KEY_TARGET_B: row.target_b,
                        c_sr.SR_KEY_TIMEBOX: row.timebox,
                        c_sr.SR_KEY_COMPLETED: row.completed,
                        c_sr.SR_KEY_TIME_NEEDED: row.time_needed,
                        c_sr.SR_KEY_R_COUNT: row.r_count,
                        c_sr.SR_KEY_DIFFICULTY: row.difficulty
                    }
                )
            except AttributeError:
                abort(c.RESP_INTERNAL_SERVER_ERROR)
        if not json_components[0]:
            return jsonify({c.KEY_INFO: c.MSG_QUERY_EMPTY_TABLE})

        return jsonify({
            c.KEY_QUERY_RESULT: json_components
        })


api.add_resource(SurvrunQueryGetRuns, c.API_SURVRUN_GET_ALL_DB_RUN_DATA)


class SurvrunQueryPostRun(Resource):
    """
    POST endpoint to insert a survrun to the DB
    """
    def post(self):
        run_data = json.loads(request.data)[c_sr.SR_FORM_KEY_SUBMIT_RUN_DATA]
        if not run_data or not run_data[0]:
            abort(c.RESP_BAD_REQUEST)

        player_class = run_data[0][c_sr.SR_KEY_PLAYER_CLASS]
        target_a = run_data[0][c_sr.SR_KEY_TARGET_A]
        target_b = run_data[0][c_sr.SR_KEY_TARGET_B]
        timebox = run_data[0][c_sr.SR_KEY_TIMEBOX]
        time_needed = run_data[0][c_sr.SR_KEY_TIME_NEEDED]
        r_count = run_data[0][c_sr.SR_KEY_R_COUNT]
        difficulty = run_data[0][c_sr.SR_KEY_DIFFICULTY]
        if 0 < time_needed < timebox:
            completed = c_sr.SURVRIM_YES
        else:
            completed = c_sr.SURVRIM_NO

        if not player_class or not target_a or not target_b or not timebox or not time_needed or not difficulty:
            abort(c.RESP_BAD_REQUEST)

        db_cursor = QuerySurvrunTable()
        status, msg = db_cursor.survrun_insert_query(player_class=player_class, target_a=target_a,
                                                     target_b=target_b, timebox=timebox, time_needed=time_needed,
                                                     r_count=r_count, completed=completed, difficulty=difficulty)
        if status is not c.RESP_OK:
            abort(status)
        return make_response(jsonify({c.KEY_STATUS: status, c.KEY_MESSAGE: msg}))


api.add_resource(SurvrunQueryPostRun, c.API_SURVRUN_POST_RUN)


class SurvrunTargetLocationApi(Resource):
    """
    exposes survrun target location data
    """
    def get(self):
        survrun = SurvrunGoalLocationCalculator()
        target_a, target_b = survrun.calc_goal_locations()
        timebox, rating = survrun.calc_time_limit_with_randomness(target_a, target_b)
        if not target_a or not target_b or not timebox:
            abort(c.RESP_BAD_REQUEST)

        json_model = {
            c_sr.SR_KEY_SURVRUN_DATA: [
                {
                    c_sr.SR_KEY_ID: 1,
                    c_sr.SR_KEY_TARGET_LOCATION_ONE: target_a,
                    c_sr.SR_KEY_TARGET_LOCATION_TWO: target_b,
                    c_sr.SR_KEY_TIMEBOX: timebox,
                    c_sr.SR_KEY_RATING: rating
                }
            ]
        }

        return json_model


api.add_resource(SurvrunTargetLocationApi, c.API_SURVRUN_GET_TARGET_LOCATION)


class SurvrunDeleteRunApi(Resource):
    """
    endpoint to delete a recorded survrun from DB
    """
    def post(self):
        run_id = None
        try:
            run_id = json.loads(request.data)[c_db.DB_KEY_DELETE_ROW_ID]
        except KeyError:
            abort(c.RESP_BAD_REQUEST)
        if not run_id:
            abort(c.RESP_BAD_REQUEST)

        db_cursor = QuerySurvrunTable()
        status, msg = db_cursor.survrun_delete_record_by_id_query(run_id)
        if status is not c.RESP_OK:
            abort(status)
        return jsonify({c.KEY_STATUS: status, c.KEY_MESSAGE: msg})


api.add_resource(SurvrunDeleteRunApi, c.API_SURVRUN_DELETE_RUN)


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
            abort(c.RESP_INTERNAL_SERVER_ERROR)


api.add_resource(SurvrunStatisticsApi, c.API_SURVRUN_GET_STATISTICS)


# # # # # # # # # # # # # # # # # # #
# # # Stronghold Api Endpoints  # # #
# # # # # # # # # # # # # # # # # # #

class ShcGetAiBattleApi(Resource):
    """
    endpoint to return shc ai battles
    """
    def post(self):
        ai_count = json.loads(request.data)[c_shc.SHC_KEY_AI_BATTLE_PLAYER_COUNT]
        if not ai_count:
            abort(c.RESP_BAD_REQUEST)
        ai_list = StrongholdAiPicker.pick_random_ai(ai_count)
        ai_list_str = StrongholdAiPicker.format_ai_list(ai_list)
        ai_list_teams = StrongholdAiPicker.split_ai_in_teams(ai_list)
        if not ai_list_str or not ai_list_teams:
            abort(c.RESP_INTERNAL_SERVER_ERROR)

        return {c_shc.SHC_KEY_DATA: [
            {c_shc.SHC_KEY_AI_BATTLE: ai_list_str,
             c_shc.SHC_KEY_TEAMS: ai_list_teams}
        ]}


api.add_resource(ShcGetAiBattleApi, c.API_STRONGHOLD_GET_AI_BATTLE)


class ShcRankingApi(Resource):
    """
    endpoint to return and update shc rankings
    """
    def get(self):
        """
        fetch and return ranking data from DB
        """
        pass

    def post(self):
        """
        update shc rankings in DB
        """
        winning_team = json.loads(request.data)[c_shc.SHC_KEY_WINNING_TEAM_DATA][c_shc.SHC_KEY_WINNING_TEAM]
        if not winning_team:
            abort(c.RESP_BAD_REQUEST)

        cursor = QueryShcRankingTable()
        for ai_name in winning_team.split(','):
            cursor.insert_update_ranking(ai_name, c_shc.RANKING_UPDATE_ON_WIN)


api.add_resource(ShcRankingApi, c.API_SHC_RANKING_UPDATE)


# # # # # # # # # # # # # # # # # # #
# # # # ESO Dungeon Endpoints # # # #
# # # # # # # # # # # # # # # # # # #

class EsoGetConstantsApi(Resource):
    """
    exposes eso constants
    """
    def get(self):
        return EsoReturnConstants.eso_get_constants()


api.add_resource(EsoGetConstantsApi, c.API_ESO_GET_CONSTANTS)


class EsoQueryGetDungeonRuns(Resource):
    """
    exposes recorded eso dungeon runs from DB
    """
    def get(self):
        db_cursor = QueryEsoDungeonTable()
        db_data = db_cursor.eso_select_dungeon_runs_query()
        if not db_data:
            abort(c.RESP_BAD_REQUEST)

        json_components = []
        for row in db_data:
            try:
                json_components.append(
                    {
                        c_eso.ESO_KEY_ID: row.id,
                        c_eso.ESO_KEY_DUNGEON_NAME: row.dungeon_name,
                        c_eso.ESO_KEY_PLAYER_COUNT: row.player_count,
                        c_eso.ESO_KEY_TIME_NEEDED: row.time_needed,
                        c_eso.ESO_KEY_HARDMODE: row.hardmode,
                        c_eso.ESO_KEY_FLAWLESS: row.flawless,
                        c_eso.ESO_KEY_WIPES: row.wipes,
                        c_eso.ESO_KEY_CLASS_ONE: row.class_one,
                        c_eso.ESO_KEY_CLASS_TWO: row.class_two,
                        c_eso.ESO_KEY_CLASS_THREE: row.class_three,
                        c_eso.ESO_KEY_CLASS_FOUR: row.class_four
                    }
                )
            except AttributeError:
                abort(c.RESP_INTERNAL_SERVER_ERROR)
        if not json_components[0]:
            return jsonify({c.KEY_INFO: c.MSG_QUERY_EMPTY_TABLE})

        return jsonify({
            c.KEY_QUERY_RESULT: json_components
        })


api.add_resource(EsoQueryGetDungeonRuns, c.API_ESO_GET_DUNGEON_RUNS)


class EsoQueryPostDungeonRun(Resource):
    """
    POST endpoint to insert a eso dungeon run to the DB
    """
    def post(self):
        run_data = json.loads(request.data)[c_eso.ESO_FORM_KEY_SUBMIT_DUNGEON_RUN_DATA]
        if not run_data:
            abort(c.RESP_BAD_REQUEST)

        dungeon_name = run_data[c_eso.ESO_FORM_KEY_DUNGEON_NAME]
        player_count = run_data[c_eso.ESO_FORM_KEY_PLAYER_COUNT]
        time_needed = run_data[c_eso.ESO_FORM_KEY_TIME_NEEDED]
        hardmode = run_data[c_eso.ESO_FORM_KEY_HARDMODE]
        flawless = run_data[c_eso.ESO_FORM_KEY_FLAWLESS]
        wipes = run_data[c_eso.ESO_FORM_KEY_WIPES]
        class_one = run_data[c_eso.ESO_FORM_KEY_CLASS_ONE]
        class_two = run_data[c_eso.ESO_FORM_KEY_CLASS_TWO]
        class_three = run_data[c_eso.ESO_FORM_KEY_CLASS_THREE]
        class_four = run_data[c_eso.ESO_FORM_KEY_CLASS_FOUR]

        if not dungeon_name or not player_count or not time_needed or not hardmode or not flawless \
                or not class_one or not class_two or not class_three or not class_four:
            abort(c.RESP_BAD_REQUEST)

        db_cursor = QueryEsoDungeonTable()
        status = db_cursor.eso_insert_dungeon_run_query(dungeon_name=dungeon_name, player_count=player_count,
                                                        time_needed=time_needed, hardmode=hardmode, flawless=flawless,
                                                        wipes=wipes, class_one=class_one, class_two=class_two,
                                                        class_three=class_three, class_four=class_four)

        if status is not c.RESP_OK:
            abort(status)
        return make_response(jsonify({c.KEY_STATUS: status}))


api.add_resource(EsoQueryPostDungeonRun, c.API_ESO_POST_DUNGEON_RUN)


class EsoDeleteDungeonRunById(Resource):
    """
    Delete a recorded ESO dungeon run from the DB
    """
    def post(self):
        run_id = None
        try:
            run_id = json.loads(request.data)[c_db.DB_KEY_DELETE_ROW_ID]
        except KeyError:
            abort(c.RESP_BAD_REQUEST)
        if not run_id:
            abort(c.RESP_BAD_REQUEST)

        db_cursor = QueryEsoDungeonTable()
        status = db_cursor.eso_delete_dungeon_run_by_id(run_id)
        if status is not c.RESP_OK:
            abort(status)
        return jsonify({c.KEY_STATUS: status})


api.add_resource(EsoDeleteDungeonRunById, c.API_ESO_DELETE_DUNGEON_RUN)


# # # # # # # # # # # # # # # # # # #
# # # # # ESO Raid Endpoints  # # # #
# # # # # # # # # # # # # # # # # # #

class EsoQueryGetRaidRuns(Resource):
    """
    exposes recorded eso raid runs from DB
    """
    def get(self):
        db_cursor = QueryEsoRaidTable()
        db_data = db_cursor.eso_select_raid_runs_query()
        if not db_data:
            abort(c.RESP_BAD_REQUEST)

        json_components = []
        for row in db_data:
            try:
                json_components.append(
                    {
                        c_eso.ESO_KEY_ID: row.id,
                        c_eso.ESO_KEY_RAID_NAME: row.raid_name,
                        c_eso.ESO_KEY_PLAYER_COUNT: row.player_count,
                        c_eso.ESO_KEY_TIME_NEEDED: row.time_needed,
                        c_eso.ESO_KEY_HARDMODE: row.hardmode,
                        c_eso.ESO_KEY_FLAWLESS: row.flawless,
                        c_eso.ESO_KEY_WIPES: row.wipes,
                        c_eso.ESO_KEY_CLASS_ONE: row.class_one,
                        c_eso.ESO_KEY_CLASS_TWO: row.class_two,
                        c_eso.ESO_KEY_CLASS_THREE: row.class_three,
                        c_eso.ESO_KEY_CLASS_FOUR: row.class_four,
                        c_eso.ESO_KEY_CLASS_FIVE: row.class_five,
                        c_eso.ESO_KEY_CLASS_SIX: row.class_six,
                        c_eso.ESO_KEY_CLASS_SEVEN: row.class_seven,
                        c_eso.ESO_KEY_CLASS_EIGHT: row.class_eight,
                        c_eso.ESO_KEY_CLASS_NINE: row.class_nine,
                        c_eso.ESO_KEY_CLASS_TEN: row.class_ten,
                        c_eso.ESO_KEY_CLASS_ELEVEN: row.class_eleven,
                        c_eso.ESO_KEY_CLASS_TWELVE: row.class_twelve,
                        c_eso.ESO_KEY_NUM_TANKS: row.num_tanks,
                        c_eso.ESO_KEY_NUM_DPS: row.num_dps,
                        c_eso.ESO_KEY_NUM_HEALS: row.num_heals,
                        c_eso.ESO_KEY_TOTAL_PARTY_DPS: row.total_party_dps,
                        c_eso.ESO_KEY_TOTAL_PARTY_HPS: row.total_party_hps
                    }
                )
            except AttributeError:
                abort(c.RESP_INTERNAL_SERVER_ERROR)
        if not json_components[0]:
            return jsonify({c.KEY_INFO: c.MSG_QUERY_EMPTY_TABLE})

        return jsonify({
            c.KEY_QUERY_RESULT: json_components
        })


api.add_resource(EsoQueryGetRaidRuns, c.API_ESO_GET_RAID_RUNS)


class EsoQueryPostRaidRun(Resource):
    """
    POST endpoint to insert a eso raid run to the DB
    """
    def post(self):
        run_data = json.loads(request.data)[c_eso.ESO_FORM_KEY_RAID_RUN_FORM_DATA]

        if not run_data:
            abort(c.RESP_BAD_REQUEST)

        raid_name = run_data[c_eso.ESO_FORM_KEY_RAID_NAME]
        player_count = run_data[c_eso.ESO_FORM_KEY_PLAYER_COUNT]
        time_needed = run_data[c_eso.ESO_FORM_KEY_TIME_NEEDED]
        hardmode = run_data[c_eso.ESO_FORM_KEY_HARDMODE]
        flawless = run_data[c_eso.ESO_FORM_KEY_FLAWLESS]
        wipes = run_data[c_eso.ESO_FORM_KEY_WIPES]
        class_one = run_data[c_eso.ESO_FORM_KEY_CLASS_ONE]
        class_two = run_data[c_eso.ESO_FORM_KEY_CLASS_TWO]
        class_three = run_data[c_eso.ESO_FORM_KEY_CLASS_THREE]
        class_four = run_data[c_eso.ESO_FORM_KEY_CLASS_FOUR]
        class_five = run_data[c_eso.ESO_FORM_KEY_CLASS_FIVE]
        class_six = run_data[c_eso.ESO_FORM_KEY_CLASS_SIX]
        class_seven = run_data[c_eso.ESO_FORM_KEY_CLASS_SEVEN]
        class_eight = run_data[c_eso.ESO_FORM_KEY_CLASS_EIGHT]
        class_nine = run_data[c_eso.ESO_FORM_KEY_CLASS_NINE]
        class_ten = run_data[c_eso.ESO_FORM_KEY_CLASS_TEN]
        class_eleven = run_data[c_eso.ESO_FORM_KEY_CLASS_ELEVEN]
        class_twelve = run_data[c_eso.ESO_FORM_KEY_CLASS_TWELVE]
        num_tanks = run_data[c_eso.ESO_FORM_KEY_NUM_TANKS]
        num_dps = run_data[c_eso.ESO_FORM_KEY_NUM_DPS]
        num_heals = run_data[c_eso.ESO_FORM_KEY_NUM_HEALS]
        total_party_dps = run_data[c_eso.ESO_FORM_KEY_TOTAL_PARTY_DPS]
        total_party_hps = run_data[c_eso.ESO_FORM_KEY_TOTAL_PARTY_HPS]

        if not raid_name or not player_count or not time_needed or not class_one or not class_two or not class_three \
                or not class_four or not class_five or not class_six or not class_seven or not class_eight or not \
                class_nine or not class_ten or not class_eleven or not class_twelve:
            abort(c.RESP_BAD_REQUEST)

        if hardmode is None or flawless is None or wipes is None:
            abort(c.RESP_BAD_REQUEST)

        db_cursor = QueryEsoRaidTable()
        status = db_cursor.eso_insert_raid_run_query(raid_name=raid_name, player_count=player_count,
                                                     time_needed=time_needed,
                                                     hardmode=hardmode, flawless=flawless, wipes=wipes,
                                                     class_one=class_one,
                                                     class_two=class_two, class_three=class_three,
                                                     class_four=class_four,
                                                     class_five=class_five, class_six=class_six,
                                                     class_seven=class_seven,
                                                     class_eight=class_eight, class_nine=class_nine,
                                                     class_ten=class_ten,
                                                     class_eleven=class_eleven, class_twelve=class_twelve,
                                                     num_tanks=num_tanks, num_dps=num_dps, num_heals=num_heals,
                                                     total_party_dps=total_party_dps, total_party_hps=total_party_hps)

        if status is not c.RESP_OK:
            abort(status)
        return make_response(jsonify({c.KEY_STATUS: status}))


api.add_resource(EsoQueryPostRaidRun, c.API_ESO_POST_RAID_RUN)


class EsoDeleteRaidRunById(Resource):
    """
    Delete a recorded ESO raid run from the DB
    """
    def post(self):
        run_id = None
        try:
            run_id = json.loads(request.data)[c_db.DB_KEY_DELETE_ROW_ID]
        except KeyError:
            abort(c.RESP_BAD_REQUEST)
        if not run_id:
            abort(c.RESP_BAD_REQUEST)

        db_cursor = QueryEsoRaidTable()
        status = db_cursor.eso_delete_raid_run_by_id(run_id)
        if status is not c.RESP_OK:
            abort(status)
        return jsonify({c.KEY_STATUS: status})


api.add_resource(EsoDeleteRaidRunById, c.API_ESO_DELETE_RAID_RUN)


# # # # # # # # # # # # # # # # # # #
# # # # # Misc Endpoints  # # # # # #
# # # # # # # # # # # # # # # # # # #


class MiscGetConstantsApi(Resource):
    """
    exposes misc constants
    """
    def get(self):
        return MiscReturnConstants.misc_get_constants()


api.add_resource(MiscGetConstantsApi, c.API_MISC_GET_CONSTANTS)


class MiscBrainstormApi(Resource):
    """
    Returns math exercises for the brainstorm game
    """
    def post(self):
        difficulty = None
        length = None
        try:
            difficulty = json.loads(request.data)[c_m.MISC_KEY_DATA][c_m.MISC_KEY_FORM_BRAINSTROM_DIFFICULTY]
            length = 1  # hardcoded for now, for better user experience in UI
        except KeyError:
            abort(c.RESP_BAD_REQUEST)
        if not difficulty or not length:
            abort(c.RESP_BAD_REQUEST)

        calc = MiscBrainstorm()
        exercises = calc.get_exercise_list(difficulty, length)

        if exercises:
            return jsonify({c_m.MISC_KEY_EXERCISES: exercises})
        else:
            abort(c.RESP_INTERNAL_SERVER_ERROR)


api.add_resource(MiscBrainstormApi, c.API_MISC_BRAINSTORM_GET_EXERCISE_LIST)


# # # # # # # # # # # # # # # # # # #
# # # # # Flask app routes  # # # # #
# # # # # # # # # # # # # # # # # # #

@app.route('/')
def landing_page():
    return c.APP_NAME


@app.errorhandler(c.RESP_BAD_REQUEST)
def error_not_found(error):
    return make_response(jsonify({c.SUCCESS: error}), c.RESP_BAD_REQUEST)


@app.errorhandler(c.RESP_RESOURCE_NOT_FOUND)
def error_not_found(error):
    return make_response(jsonify({c.ERROR: error}), c.RESP_RESOURCE_NOT_FOUND)


@app.errorhandler(c.RESP_INTERNAL_SERVER_ERROR)
def error_not_found(error):
    return make_response(jsonify({c.BACKEND_ERROR: 'an internal error occured in backend while processing data: ' +
                                                   error}), c.RESP_INTERNAL_SERVER_ERROR)


if __name__ == '__main__':
    app.debug = True  # add debug support
    app.run()
