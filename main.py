import random
import tkinter as tk
from playsound import playsound
import winsound

MAX_TURNS = 12

# Create the graphical application
root = tk.Tk()
root.iconbitmap('resources\icon.ico')
root.title("Guess The Word")
root.geometry("500x600")
root.configure(bg='#e6f2ff')
word = ""
theme_name = ""
words = ""

# Define random complexion

theme_animals = ['cat', 'dog', 'monkey', 'cow', 'crocodile', 'elephant', 'lion', 'tiger', 'giraffe', 'zebra']
theme_birds = ['raven', 'eagle', 'duck', 'sparrow', 'dove', 'parrot', 'seagull', 'pelican', 'flamingo', 'marabou']
theme_jobs = ['programmer', 'analyst', 'actor', 'singer', 'engineer', 'architect', 'barber', 'scientist', 'lawyer',
                'designer']
theme_body_parts = ['head', 'neck', 'arm', 'leg', 'foot', 'arm', 'chest', 'knee', 'elbow', 'ankle']

theme_index = random.choice(range(0, 4))

if theme_index == 0:
     theme_name = "animals"
     words = theme_animals
elif theme_index == 1:
     theme_name = "birds"
     words = theme_birds
elif theme_index == 2:
     theme_name = "professions"
     words = theme_jobs
elif theme_index == 3:
     theme_name = "body parts"
     words = theme_body_parts

word = random.choice(words)

# Define variables for the word, familiar letters, and wrong attempts
guesses = set()
wrong_guesses = set()
wrong_attempts = 0
wrong_attempts_words = ["""
________     
|            
|            
|            
|            
|            
|            
|____________
""",
                        """
________     
|      |     
|            
|            
|            
|            
|            
|____________
""",
                        """
________     
|      |     
|      O     
|            
|            
|            
|            
|____________
""",
                        """
________     
|      |     
|      O     
|      |     
|            
|            
|            
|____________
""",
                        """
________     
|      |     
|      O     
|      |     
|      |     
|            
|            
|____________
""",
                        """
________     
|      |     
|      O     
|     /|     
|      |     
|            
|            
|____________
""",
                        """
________     
|      |     
|      O     
|     /|     
|    / |     
|            
|            
|____________
""",
                        """
________     
|      |     
|      O     
|     /|\    
|    / |     
|            
|            
|____________
""",
                        """
________     
|      |     
|      O     
|     /|\    
|    / | \   
|            
|            
|____________
""",
                        """
________     
|      |     
|      O     
|     /|\    
|    / | \   
|     /      
|            
|____________
""",
                        """
________     
|      |     
|      O     
|     /|\    
|    / | \   
|     /      
|    /       
|____________
""",
                        """
________     
|      |     
|      O     
|     /|\    
|    / | \   
|     / \    
|    /       
|____________
""",
                        """
________     
|      |     
|      O     
|     /|\    
|    / | \   
|     / \    
|    /   \   
|____________
"""
                        ]


# Определяме функция, която връща думата за броя на грешните опити
def get_wrong_attempts_word():
    return wrong_attempts_words[wrong_attempts]


# Дефинираме функцията, която ще бъде извиквана при натискане на буква
def guess_letter(letter):
    if letter in word:
        global wrong_attempts
        guesses.add(letter)
        update_display()
        winsound.Beep(350, 200)
        winsound.Beep(450, 300)
        if all(letter in guesses for letter in word):
            show_message(f"Congratulations! You guessed The word is '{word}'!")
            file = "resources\win.mp3"
            playsound(file)
            # root.quit() # Не затваряме играта веднага след победа
    else:
        global wrong_attempts  # това не съм сигурен, без него работи, но дава warning :)
        wrong_guesses.add(letter)
        wrong_attempts += 1  # увеличаваме брояча на грешните опити
        update_display()
        winsound.Beep(250, 500)
        if wrong_attempts >= MAX_TURNS:
            show_message(f"You lost! The word was '{word}'!")
            file = "resources\lose.mp3"
            playsound(file)
            # root.quit()  # We don't close the game immediately after a loss


# Define the function that will refresh the game display
def update_display():

    theme_label.configure(text=f"Guess the word! Theme is: {theme_name.upper()}")
    display_word = " ".join([letter if letter in guesses else "_" for letter in word])
    display_word_label.config(text=display_word)
    wrong_guesses_label.config(text="Грешни опити: " + ", ".join(sorted(wrong_guesses)))
    wrong_attempts_label.config(text=f"{get_wrong_attempts_word()}")


# Define the function that displays a message on the screen
def show_message(message):
    message_label.config(text=message)

# код за рестартиране на приложението


def restart():
    global word, guesses, wrong_guesses, wrong_attempts, theme_index, theme_name, words
    word = ""
    guesses = set()
    wrong_guesses = set()
    wrong_attempts = 0
    theme_index = random.choice(range(0, 4))
    if theme_index == 0:
        theme_name = "животни"
        words = theme_animals
    elif theme_index == 1:
        theme_name = "птици"
        words = theme_birds
    elif theme_index == 2:
        theme_name = "професии"
        words = theme_jobs
    elif theme_index == 3:
        theme_name = "части на тялото"
        words = theme_body_parts
    word = random.choice(words)
    # theme_label = tk.Label(root, text="")
    update_display()



# Добавяме елементи към графичното приложение


theme_label = tk.Label(root, text=f"Познай думата! Темата е: {theme_name.upper()}",
                       font=('Arial', 15),
                       bg="#e6f2ff",
                       fg="#0000FF")
theme_label.pack()

display_word_label = tk.Label(root, text=" ".join(["_" for letter in word]),
                              font=('Arial', 25),
                              bg="#e6f2ff",
                              fg="#0000FF")
display_word_label.pack()

letters_frame = tk.Frame(root)

for i, letter in enumerate("абвгдежзийклмнопрстуфхцчшщъьюя"):
    letter_button = tk.Button(letters_frame, text=letter, command=lambda letter=letter: guess_letter(letter),
                              bg="#0000FF",
                              fg="#e6f2ff",
                              font=('Consolas', 15),
                              padx=5,
                              pady=5,
                              # relief=tk.RIDGE,
                              borderwidth=5)
    letter_button.grid(row=i // 10, column=i % 10)

letters_frame.pack()

wrong_guesses_label = tk.Label(root, text="Грешни опити:",
                               bg="#e6f2ff",
                               fg="#0000FF",
                               font=('Arial', 13))
wrong_guesses_label.pack()

message_label = tk.Label(root, text="", bg="#e6f2ff",
                         fg="#0000FF",
                         font=('Consolas', 15))
message_label.pack()

wrong_attempts_label = tk.Label(root, text=f"{get_wrong_attempts_word()}",
                                font=('Consolas', 15),
                                fg="#0000FF",
                                bg="#cce6ff")
wrong_attempts_label.pack()

restart_button = tk.Button(root, text="Изтегли нова дума и тема", command=restart,
                                bg="#0000FF",
                                fg="#e6f2ff",
                                font=('Consolas', 15),
                                padx=5,
                                pady=5,
                                relief=tk.RIDGE,
                                borderwidth=5)
restart_button.pack()


# Стартираме графичното приложение

root.mainloop()
