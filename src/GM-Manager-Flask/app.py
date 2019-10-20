from flask import Flask, jsonify, abort, make_response
from modes.survrim.survrun_goal_location_calculator import SurvrunGoalLocationCalculator
from modes.stronghold.shc_ai_picker import StrongholdAiPicker

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'GM-Manager'


@app.route('/api/survrim', methods=['GET'])
def get_survrun_locations():
    survrun_targets = SurvrunGoalLocationCalculator()
    target_a, target_b = survrun_targets.calc_goal_locations()
    if not target_a or not target_b:
        abort(404)

    survrun_data = [
        {
            'id': 1,
            'target_location_one': target_a,
            'target_location_two': target_b
        }
    ]

    return jsonify({'survrun_data': survrun_data})


@app.route('/api/shc')
def stronghold_route():
    ai_list = StrongholdAiPicker.pick_random_ai(8)
    ai_list_str = StrongholdAiPicker.format_ai_list(ai_list)
    return 'Stronghold random game: ' + ai_list_str


@app.errorhandler(404)
def error_not_found(error):
    return make_response(jsonify({'error': '404: Not found'}), 404)


if __name__ == '__main__':
    app.debug = True  # add debug support
    app.run()
