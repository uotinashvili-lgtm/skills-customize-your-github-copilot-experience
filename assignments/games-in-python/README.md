# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python where players guess letters to reveal a hidden word before attempts run out. In this assignment, you will practice string manipulation, loops, conditionals, and user input handling.

## 📝 Tasks

### 🛠️ Create the Game Setup

#### Description
Set up the core game state, including a predefined word list, random word selection, and tracking variables for guessed letters and remaining attempts.

#### Requirements
Completed program should:

- Select a random word from a predefined list.
- Initialize hidden word progress using underscores (for example: `_ _ _ _`).
- Track guessed letters and remaining incorrect attempts.

### 🛠️ Implement the Game Loop

#### Description
Build the interactive game loop that accepts letter guesses, updates game progress, validates input, and ends with a clear result message.

#### Requirements
Completed program should:

- Accept one letter guess at a time from the player.
- Reveal correctly guessed letters in the word progress display.
- Decrease remaining attempts for incorrect guesses.
- End the game when the word is fully guessed or attempts reach zero.
- Display a clear win or lose message at the end.
