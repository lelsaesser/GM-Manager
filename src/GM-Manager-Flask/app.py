from flask import Flask
from modes.survrim.survrun_goal_location_calculator import SurvrunGoalLocationCalculator
from modes.stronghold.shc_ai_picker import StrongholdAiPicker

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'GM-Manager'


@app.route('/survrim')
def survrim_route():
    survrun_goals = SurvrunGoalLocationCalculator()
    a, b = survrun_goals.calc_goal_locations()
    return 'Survrun target locations: ' + a + " " + b


@app.route('/shc')
def stronghold_route():
    ai_list = StrongholdAiPicker.pick_random_ai(8)
    ai_list_str = StrongholdAiPicker.format_ai_list(ai_list)
    return 'Stronghold random game: ' + ai_list_str


if __name__ == '__main__':
    app.debug = True  # add debug support
    app.run()
