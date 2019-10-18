from flask import Flask
from modes.survrim import survrun_goal_location_calculator

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'GM-Manager'


@app.route('/survrim')
def survrim_route():
    survrun_goals = survrun_goal_location_calculator.SurvrunGoalLocationCalculator()
    a, b = survrun_goals.calc_goal_locations()
    return 'Survrun target locations: ' + a + " " + b


@app.route('/shc')
def stronghold_route():
    return 'Stronghold'


if __name__ == '__main__':
    app.debug = True  # add debug support
    app.run()
