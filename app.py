from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flashcards.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class Deck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    cards = db.relationship('Card', backref='deck', lazy=True, cascade='all, delete-orphan')

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    deck_id = db.Column(db.Integer, db.ForeignKey('deck.id'), nullable=False)

# Routes
@app.route('/')
def index():
    decks = Deck.query.all()
    return render_template('index.html', decks=decks)

@app.route('/deck/<int:deck_id>')
def view_deck(deck_id):
    deck = Deck.query.get_or_404(deck_id)
    return render_template('deck.html', deck=deck)

@app.route('/study/<int:deck_id>')
def study_deck(deck_id):
    deck = Deck.query.get_or_404(deck_id)
    if not deck.cards:
        return redirect(url_for('view_deck', deck_id=deck_id))
    return render_template('study.html', deck=deck)

@app.route('/create_deck', methods=['GET', 'POST'])
def create_deck():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        deck = Deck(name=name, description=description)
        db.session.add(deck)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_deck.html')

@app.route('/add_card/<int:deck_id>', methods=['GET', 'POST'])
def add_card(deck_id):
    deck = Deck.query.get_or_404(deck_id)
    if request.method == 'POST':
        question = request.form['question']
        answer = request.form['answer']
        card = Card(question=question, answer=answer, deck_id=deck_id)
        db.session.add(card)
        db.session.commit()
        return redirect(url_for('view_deck', deck_id=deck_id))
    return render_template('add_card.html', deck=deck)

@app.route('/delete_deck/<int:deck_id>', methods=['POST'])
def delete_deck(deck_id):
    deck = Deck.query.get_or_404(deck_id)
    db.session.delete(deck)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_card/<int:card_id>', methods=['POST'])
def delete_card(card_id):
    card = Card.query.get_or_404(card_id)
    deck_id = card.deck_id
    db.session.delete(card)
    db.session.commit()
    return redirect(url_for('view_deck', deck_id=deck_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)