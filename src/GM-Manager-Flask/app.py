from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'GM-Manager'


@app.route('/survrim')
def survrim_route():
    return 'Survivalrim'


@app.route('/shc')
def stronghold_route():
    return 'Stronghold'


if __name__ == '__main__':
    app.debug = True  # add debug support
    app.run()
