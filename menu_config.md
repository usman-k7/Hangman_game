# 🎮 Hangman Game Menu Options

This file explains all the options and flow when running `hangman.py`.

---

## Main Flow

When you run the program, you will see:

1. **Start Game**
   - A random word is selected from the word list (`words.py`).
   - The word is hidden with underscores (`_`) for each letter.
   - The player begins with **6 tries**.

2. **Guess a Letter or Word**
   - Enter a **single letter** to check if it exists in the word.
   - Enter a **full word guess** (must match the exact word).
   - Invalid inputs (numbers, symbols, wrong length) are rejected with a message.

3. **Game Feedback**
   - Correct guesses reveal the letters in their positions.
   - Wrong guesses reduce tries and update the **ASCII hangman graphic**.
   - Already guessed letters/words are stored and cannot be repeated.

4. **Win / Lose Condition**
   - **Win:** If all letters are guessed correctly before tries run out.
   - **Lose:** If tries reach 0, the word is revealed.

5. **Replay Option**
   - After each game, the program asks:  
     *“Play Again? (Y/N)”*
   - Enter `Y` to start with a new random word, or `N` to exit.

---

## Notes

- Words are stored in `words.py` (can be customized).
- ASCII art visuals for the hangman are shown based on remaining tries.
- Input is case-insensitive (all guesses are converted to uppercase).

---
