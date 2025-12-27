from flask import Flask, render_template
from flask_cors import CORS
import requests
from flask import jsonify

app = Flask(__name__, template_folder="website/templates", static_folder="website/static")

CORS(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/standings')
def standings():
    return render_template('standings.html')

@app.route('/players')
def players():
    return render_template('player.html')

@app.route('/teams')
def teams():
    return render_template('teams.html')

@app.route('/players/<player_name>')
def player_page(player_name):
    return render_template('player-stats.html', player_name=player_name)

@app.route('/matches')
def matches():
    return render_template('matches.html')

@app.route('/admin')
def admin():
    return render_template('data-manager.html')

@app.route('/admin/players')
def admin_players():
    return render_template('data-manager-players.html')

@app.route('/admin/teams')
def admin_teams():
    return render_template('data-manager-teams.html')

if __name__ == '__main__':
    # Set debug=True for auto reloads during development
    app.run(debug=True)

    