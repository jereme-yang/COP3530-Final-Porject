from flask import Flask, request, jsonify, render_template, session
from main_code import game_logic, initialize_game
from Artist import Artist
from random import randint
from flask_session import Session
import json

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'inter1'
Session(app)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/initialize_game', methods=['POST'])
def initialize_game_endpoint():
    data = request.get_json()
    genre = data['genre']
    sorting = data['sorting']
    
    game_state = initialize_game(genre, sorting)
    session['current_index'] = game_state['current_index']
    session['level'] = game_state['level']
    session['has_lost'] = game_state['has_lost']
    session['correct_option'] = game_state['correct_option']

    return jsonify({
        'current_artist': game_state['current_artist'],
        'options': game_state['options'],
        'level': game_state['level'],
    })

@app.route('/api/new_round', methods=['POST'])
def new_round():
    data = request.get_json()
    user_choice = data['user_choice']
    current_index = session['current_index']
    level = session['level']
    has_lost = session['has_lost']
    correct_option = session['correct_option']


    if user_choice == correct_option:
        current_index = current_index - randint(20, 40)
        game_state = game_logic(current_index, level, has_lost)
        # Update the session with the new game state
        session['current_index'] = game_state['current_index']
        session['level'] = game_state['level']
        session['has_lost'] = game_state['has_lost']
        session['correct_option'] = game_state['correct_option']
    else:
        game_state = {
            'has_lost': True,
            'final_score': level,
            'current_index': current_index
        }
        # Update the session with the new game state
        session['current_index'] = game_state['current_index']
        session['has_lost'] = game_state['has_lost']

    return jsonify(game_state)


if __name__ == '__main__':
    app.run(debug=True)