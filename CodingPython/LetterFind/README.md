# LetterFind - Word Guessing Game

**Created:** May 9, 2026

## Overview

LetterFind is a simple Python-based word guessing game where players try to reveal a secret word by guessing individual letters. It's similar to the classic Hangman game but focuses on progressive letter revelation without penalties for incorrect guesses. The game continues until all letters in the secret word are correctly guessed.

## What It Does

The script implements a complete word guessing game with the following features:

1. **Random Word Selection**: Chooses a secret word randomly from a predefined list
2. **Visual Display**: Shows the word as underscores initially, revealing letters as they're guessed
3. **Letter Guessing**: Accepts player input for letter guesses
4. **Progressive Revelation**: Reveals all matching letters in the word for each correct guess
5. **Win Detection**: Ends the game when all letters are revealed

## Requirements

- Python 3.x
- No external dependencies (uses only built-in `random` module)

## How to Use

### Running the Script

Execute the script from the command line:

```bash
python project1.py
```

### Gameplay

1. The game displays a welcome message
2. Shows the secret word as underscores (e.g., `['_', '_', '_', '_', '_']`)
3. Prompts for letter guesses
4. Reveals matching letters in their correct positions
5. Continues until all letters are guessed
6. Displays a win message when complete

### Example Session

``` LetterFind

Welcome to LetterFind!
['_', '_', '_', '_', '_']
Guess a Letter: l
['_', 'l', '_', '_', '_']
Guess a Letter: u
['_', 'l', 'u', '_', '_']
Guess a Letter: f
['_', 'l', 'u', 'f', '_']
Guess a Letter: f
['_', 'l', 'u', 'f', 'f']
Guess a Letter: y
['_', 'l', 'u', 'f', 'f', 'y']
Dull Man -> Code Copier
```

## Code Explanation

### Imports and Setup

```python
import random
print("Welcome to LetterFind!")
words = ["bossbaby", "luffy", "jimbei", "mandip", "otw"]
```

- Imports the `random` module for word selection
- Prints a welcome message
- Defines a list of possible secret words

### Word Selection and Display Creation

```python
secret_word = random.choice(words)
display_word = []
for letter in secret_word:
    display_word += "_"
print(display_word)
```

- Randomly selects one word from the list
- Creates a list of underscores matching the word's length
- Prints the initial display

### Game Loop

```python
game_over = False
while not game_over:
    guess = input("Guess a Letter: ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    print(display_word)
        
    if "_" not in display_word:
        print("Dull Man -> Code Copier")
        game_over = True
```

- Initializes game state with `game_over = False`
- Loops until the game ends
- Gets user input and converts to lowercase
- Scans the secret word, revealing matching letters
- Prints updated display after each guess
- Checks for win condition (no underscores remaining)
- Ends game with win message

## Word List

The current word list includes:

- `bossbaby` (8 letters)
- `luffy` (5 letters)
- `jimbei` (6 letters)
- `mandip` (6 letters)
- `otw` (3 letters)

## How It Works

### Letter Guessing Logic

For each guess, the script iterates through each position in the secret word:

```python
for position in range(len(secret_word)):
    letter = secret_word[position]
    if letter == guess:
        display_word[position] = letter
```

This reveals **all** instances of the guessed letter in one go, unlike some games that reveal one at a time.

### Win Condition

```python
if "_" not in display_word:
    print("Dull Man -> Code Copier")
    game_over = True
```

The game ends when no underscores remain in the display list, indicating all letters have been guessed.

## Limitations

### 1. No Wrong Guess Handling

The game doesn't track incorrect guesses, provide feedback, or limit attempts. Players can guess the same letter repeatedly without penalty.

### 2. No Input Validation

- Accepts non-letter characters
- Doesn't handle empty input
- Case-insensitive but doesn't validate input type

### 3. Limited Word List

Only 5 words are available, making the game repetitive after a few plays.

### 4. Display Format

The display is printed as a Python list `['_', 'l', 'u', '_', '_']` rather than a clean string like `_ l u _ _`.

### 5. No Scoring or Statistics

No tracking of guesses made, time taken, or difficulty levels.

### 6. Win Message

The win message "Dull Man -> Code Copier" is unclear and may not be user-friendly.

## Improvements and Extensions

### 1. Better Display Format

```python
print(' '.join(display_word))  # Shows: _ l u _ _
```

### 2. Input Validation

```python
while True:
    guess = input("Guess a Letter: ").lower()
    if len(guess) == 1 and guess.isalpha():
        break
    print("Please enter a single letter.")
```

### 3. Track Guesses and Lives

```python
lives = 6
guessed_letters = []
while not game_over and lives > 0:
    guess = input("Guess a Letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    guessed_letters.append(guess)
    
    if guess in secret_word:
        # Reveal letters
        for position in range(len(secret_word)):
            if secret_word[position] == guess:
                display_word[position] = guess
    else:
        lives -= 1
        print(f"Wrong guess! {lives} lives remaining.")
    
    print(' '.join(display_word))
    
    if "_" not in display_word:
        print("You win!")
        game_over = True
    elif lives == 0:
        print(f"You lose! The word was: {secret_word}")
        game_over = True
```

### 4. Expand Word List

```python
words = [
    "python", "hangman", "computer", "programming",
    "algorithm", "function", "variable", "loop",
    "condition", "string", "integer", "boolean"
]
```

### 5. Difficulty Levels

```python
easy_words = ["cat", "dog", "run"]
medium_words = ["python", "computer", "algorithm"]
hard_words = ["programming", "functionality", "optimization"]

difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
if difficulty == "easy":
    words = easy_words
elif difficulty == "medium":
    words = medium_words
else:
    words = hard_words
```

### 6. ASCII Art

```python
hangman_art = [
    """
     +---+
     |   |
         |
         |
         |
         |
=========""",
    # ... more stages
]

print(hangman_art[6 - lives])
```

### 7. Score System

```python
score = len(secret_word) * 10 + lives * 5
print(f"Your score: {score}")
```

### 8. File-Based Word List

```python
with open("words.txt", "r") as f:
    words = [line.strip() for line in f if line.strip()]
```

### 9. Multiplayer Support

```python
players = ["Player 1", "Player 2"]
current_player = 0
# Alternate turns
```

### 10. Save/Load Game State

```python
import json
# Save progress to file
game_state = {
    "secret_word": secret_word,
    "display_word": display_word,
    "lives": lives,
    "guessed_letters": guessed_letters
}
with open("savegame.json", "w") as f:
    json.dump(game_state, f)
```

## Learning Outcomes

This script teaches:

1. **List Manipulation**: Creating and modifying lists dynamically
2. **Loop Control**: Using `while` loops with boolean flags
3. **String Processing**: Iterating over strings by index
4. **User Input**: Capturing and processing user input
5. **Conditional Logic**: `if` statements for game logic
6. **Random Selection**: Using `random.choice()` for variety
7. **Game State Management**: Tracking progress with variables

## Common Mistakes

### 1. Forgetting List Indexing

```python
# WRONG: display_word[letter] = guess
# CORRECT: display_word[position] = letter
```

### 2. String vs List Confusion

```python
# WRONG: display_word = "_" * len(secret_word)  # Creates string
# CORRECT: display_word = ["_"] * len(secret_word)  # Creates list
```

### 3. Case Sensitivity Issues

```python
# WRONG: if letter == guess:  # Case sensitive
# CORRECT: if letter == guess.lower():  # Case insensitive
```

## Example Enhanced Version

Here's a more complete Hangman-style game:

```python
import random

def play_hangman():
    words = ["python", "hangman", "computer", "programming"]
    secret_word = random.choice(words)
    display_word = ["_"] * len(secret_word)
    guessed_letters = []
    lives = 6
    
    print("Welcome to Hangman!")
    print(" ".join(display_word))
    
    while lives > 0 and "_" in display_word:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
            
        guessed_letters.append(guess)
        
        if guess in secret_word:
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    display_word[i] = guess
            print("Good guess!")
        else:
            lives -= 1
            print(f"Wrong! {lives} lives remaining.")
        
        print(" ".join(display_word))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    
    if "_" not in display_word:
        print("Congratulations! You won!")
    else:
        print(f"Game over! The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()
```

## Notes

- The current implementation is a basic prototype for learning purposes
- The win message appears to be a reference or joke—consider replacing with something more standard
- For production use, add proper error handling and user experience improvements
- The game works best with words of similar lengths to avoid giving away difficulty clues

## Author

Created: December, 2025

---

This simple game is an excellent starting point for learning Python game development. Try implementing the suggested improvements to make it more robust and engaging!
