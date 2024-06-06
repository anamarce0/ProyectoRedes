from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

WORDS = ['python', 'flask', 'docker', 'ahorcado', 'programacion','audifono']


def initialize_game():
    word = random.choice(WORDS)
    return {
        'word': word,
        'guesses': [],
        'incorrect_guesses': 0,
        'max_incorrect': 6,
        'game_over': False,
        'win': False
    }


@app.route('/')
def index():
    if 'game' not in session:
        session['game'] = initialize_game()
    game = session['game']

    # Check for win condition
    if all(letter in game['guesses'] for letter in game['word']):
        game['win'] = True
        game['game_over'] = True
    elif game['incorrect_guesses'] >= game['max_incorrect']:
        game['game_over'] = True

    session['game'] = game
    return render_template('index.html', game=game)


@app.route('/guess', methods=['POST'])
def guess():
    game = session.get('game', initialize_game())
    if not game['game_over']:
        letter = request.form['letter'].lower()
        if letter not in game['guesses']:
            game['guesses'].append(letter)
            if letter not in game['word']:
                game['incorrect_guesses'] += 1
        # Check for win condition
        if all(letter in game['guesses'] for letter in game['word']):
            game['win'] = True
            game['game_over'] = True
        elif game['incorrect_guesses'] >= game['max_incorrect']:
            game['game_over'] = True
    session['game'] = game
    return redirect(url_for('index'))


@app.route('/reset')
def reset():
    session['game'] = initialize_game()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
