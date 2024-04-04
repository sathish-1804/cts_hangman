import random
import tkinter as tk
from tkinter import messagebox
import words_list

class HangmanGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("400x400")

        self.words = words_list.word_list
        self.current_word_index = 0
        self.word = self.choose_word()
        self.guessed_letters = set()
        self.hints_used = 0
        self.attempts = 6
        self.score = 0

        self.canvas = tk.Canvas(self.master, width=200, height=200)
        self.canvas.pack()

        self.word_label = tk.Label(self.master, text=self.display_word())
        self.word_label.pack()

        self.score_label = tk.Label(self.master, text=f"Score: {self.score}")
        self.score_label.pack()

        self.guess_entry = tk.Entry(self.master)
        self.guess_entry.pack()

        self.guess_button = tk.Button(self.master, text="Guess", command=self.handle_guess)
        self.guess_button.pack()

        self.hint_button = tk.Button(self.master, text="Hint", command=self.provide_hint)
        self.hint_button.pack()

        self.new_game_button = tk.Button(self.master, text="New Game", command=self.reset_game)
        self.new_game_button.pack()
        
    def handle_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if guess in self.guessed_letters:
            messagebox.showinfo("Hangman", "You already guessed that letter.")
            return

        self.guessed_letters.add(guess)

        if guess in self.word:
            messagebox.showinfo("Hangman", "Correct guess!")
            self.word_label.config(text=self.display_word())
            if self.display_word() == self.word:
                messagebox.showinfo("Hangman", f"Congratulations! You guessed the word: {self.word}")
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
                self.current_word_index += 1
                if self.current_word_index < len(self.words):
                    self.word = self.choose_word()
                    self.guessed_letters = set()
                    self.hints_used = 0
                    self.attempts = 6
                    self.word_label.config(text=self.display_word())
                else:
                    messagebox.showinfo("Hangman", "You've guessed all words! Game over.")
                    self.reset_game()
        else:
            messagebox.showinfo("Hangman", "Incorrect guess.")
            self.attempts -= 1
            self.canvas.delete("all")
            self.canvas.create_text(100, 100, text=self.display_hangman())
            if self.attempts == 0:
                messagebox.showinfo("Hangman", f"Sorry, you ran out of attempts. The word was: {self.word}")
                self.reset_game()
  
    def choose_word(self):
        return self.words[self.current_word_index]

    def display_word(self):
        displayed_word = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                displayed_word += letter
            else:
                displayed_word += '_'
        return displayed_word

     def provide_hint(self):
        if self.hints_used == 0:
            messagebox.showinfo("Hangman", f"The number of words is {len(self.words)}")
            self.hints_used += 1
        elif self.hints_used == 1:
            messagebox.showinfo("Hangman", f"The last letter of the word is '{self.word[-1]}'")
            self.hints_used += 1
        else:
            messagebox.showinfo("Hangman", f"The last letter of the word is '{self.word[-1]}'")
            messagebox.showinfo("Hangman", f"The first letter of the word is '{self.word[0]}'")

 def display_hangman(self):
        stages = [
            """
                 --------
                 |      |
                 |      O
                 |     \|/
                 |      |
                 |     / \
                ---
            """,
            """
                 --------
                 |      |
                 |      O
                 |     \|/
                 |      |
                 |     / 
                ---
            """,
            """
                 --------
                 |      |
                 |      O
                 |     \|/
                 |      |
                 |      
                ---
            """,
            """
                 --------
                 |      |
                 |      O
                 |     \|
                 |      |
                 |     
                ---
            """,
            """
                 --------
                 |      |
                 |      O
                 |      |
                 |      |
                 |     
                ---
            """,
            """
                 --------
                 |      |
                 |      O
                 |    
                 |      
                 |     
                ---
            """,
            """
                 --------
                 |      |
                 |      
                 |    
                 |      
                 |     
                ---
            """
        ]
        return stages[self.attempts]

 def reset_game(self):
        self.current_word_index = 0
        self.word = self.choose_word()
        self.guessed_letters = set()
        self.hints_used = 0
        self.attempts = 6
        self.word_label.config(text=self.display_word())
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")
        self.canvas.delete("all")



def main():
    root = tk.Tk()
    hangman_gui = HangmanGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
