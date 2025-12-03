from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder="website/templates", static_folder="website/static")

CORS(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/standings')
def standings():
    return render_template('standings.html')

@app.route('/players/<player_name>')
def player_page(player_name):
    return render_template('player.html', player_name=player_name)

if __name__ == '__main__':
    # Set debug=True for auto reloads during development
    app.run(debug=True)