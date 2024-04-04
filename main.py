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
