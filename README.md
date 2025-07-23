# Natalia's Flashcards

A modern, web-based flashcard application built with Flask and Bootstrap. Create decks, add cards, and study efficiently with an interactive interface.

## Features

- 🃏 **Create Multiple Decks**: Organize your flashcards into different subjects or topics
- ➕ **Add Cards Easily**: Simple interface to add question-answer pairs
- 📚 **Interactive Study Mode**: Flip cards, navigate with buttons or keyboard shortcuts
- 📊 **Progress Tracking**: Visual progress bar during study sessions
- 🗑️ **Deck Management**: Edit and delete decks and individual cards
- 📱 **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- ⌨️ **Keyboard Shortcuts**: Use spacebar to flip cards, arrow keys to navigate

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup Steps

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd nataliaflashcard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open in browser**
   Navigate to `http://localhost:5000` in your web browser

## Usage

### Creating Your First Deck
1. Click "Create New Deck" on the home page
2. Enter a name and optional description
3. Click "Create Deck"

### Adding Cards
1. Click "View" on any deck
2. Click "Add Card" 
3. Enter your question and answer
4. Click "Add Card"

### Studying
1. Click "Study" on any deck with cards
2. Read the question and try to answer
3. Click the card or press spacebar to reveal the answer
4. Use navigation buttons or arrow keys to move between cards

### Keyboard Shortcuts (Study Mode)
- **Spacebar/Enter**: Flip card to show answer/question
- **Left Arrow**: Previous card
- **Right Arrow**: Next card

## Project Structure

```
nataliaflashcard/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/            # HTML templates
│   ├── base.html        # Base template with navigation
│   ├── index.html       # Home page showing all decks
│   ├── create_deck.html # Create new deck form
│   ├── deck.html        # View deck and manage cards
│   ├── add_card.html    # Add new card form
│   └── study.html       # Interactive study mode
└── static/              # Static files (CSS, JS)
    ├── css/
    │   └── style.css    # Custom styles
    └── js/
        └── app.js       # JavaScript functionality
```

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5
- **Icons**: Font Awesome

## Database Schema

### Decks Table
- `id`: Primary key
- `name`: Deck name (required)
- `description`: Optional deck description

### Cards Table
- `id`: Primary key
- `question`: Card question (required)
- `answer`: Card answer (required)
- `deck_id`: Foreign key to decks table

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## License

This project is open source and available under the MIT License.
