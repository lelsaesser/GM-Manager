from flask import Flask, jsonify, make_response, abort, request
from flask_cors import CORS
from flask_restful import Resource, Api
from modes.survrim.survrun_goal_location_calculator import SurvrunGoalLocationCalculator
from modes.stronghold.shc_ai_picker import StrongholdAiPicker
import constants
import json

app = Flask(__name__)
api = Api(app)
CORS(app)  # required for cross origin resource sharing error (temp fix)


class SurvrunApi(Resource):
    def get(self):
        survrun_targets = SurvrunGoalLocationCalculator()
        target_a, target_b = survrun_targets.calc_goal_locations()
        if not target_a or not target_b:
            abort(404)
        return {'survrunData': [{'id': 1, 'target_location_one': target_a, 'target_location_two': target_b}]}


api.add_resource(SurvrunApi, constants.API_SURVRUN_GET_TARGET_LOCATION)


class StrongholdApi(Resource):
    def get(self):
        ai_list = StrongholdAiPicker.pick_random_ai(8)
        ai_list_str = StrongholdAiPicker.format_ai_list(ai_list)
        if not ai_list_str:
            abort(404)
        return {'shcData': [{'ai_battle': ai_list_str}]}

    def post(self):
        ai_count = json.loads(request.data)["shc_ai_battle_player_count"]
        if not ai_count:
            abort(404)
        ai_list = StrongholdAiPicker.pick_random_ai(ai_count)
        ai_list_str = StrongholdAiPicker.format_ai_list(ai_list)
        if not ai_list_str:
            abort(404)
        return {'shcData': [{'ai_battle': ai_list_str}]}


api.add_resource(StrongholdApi, constants.API_STRONGHOLD_GET_AI_BATTLE)


@app.route('/')
def hello_world():
    return 'GM-Manager'


@app.errorhandler(404)
def error_not_found(error):
    return make_response(jsonify({'error': '404: Not found'}), 404)


if __name__ == '__main__':
    app.debug = True  # add debug support
    app.run()
