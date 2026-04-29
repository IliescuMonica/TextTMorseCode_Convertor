# ---------------------------- IMPORT LIBRARIES ------------------------------- #

from tkinter import *
from tkinter import messagebox
import time
import winsound

# ---------------------------- MORSE CODE CONVERTOR ------------------------------- #

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def convert(message):
    message = message.upper()
    converted_message = ''
    for char in message:
        if char == " ":
            converted_message += "/"
        elif char not in MORSE_CODE_DICT:
            raise ValueError(f"Character '{char}' not supported in Morse code")
        else:
            morse_char = MORSE_CODE_DICT[char]
            converted_message += morse_char + " "
    return converted_message

# ---------------------------- CONVERT BUTTON FUNCTION ------------------------------- #

def on_convert_click():
    message = message_entry.get()
    try:
        converted_message = convert(message)
        converted_text_entry.config(state="normal")
        converted_text_entry.delete(0, END)
        converted_text_entry.insert(0, converted_message)
        converted_text_entry.config(state="readonly")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# ---------------------------- COPY BUTTON FUNCTION ------------------------------- #

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(converted_text_entry.get())

# ---------------------------- PLAY SOUND FUNCTION ------------------------------- #

def play_morse_sound():
    global stop_sound
    stop_sound = False
    morse_text = converted_text_entry.get()
    for symbol in morse_text:
        if symbol == ".":
            winsound.Beep(800, 150)
        elif symbol == "-":
            winsound.Beep(800, 400)
        elif symbol == "/":
            time.sleep(0.4)  # pause between words
        elif symbol == " ":
            time.sleep(0.15)  # pause between letters


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Morse Code Converter")
window.config(bg="#f5f5f5",padx=30, pady=30)

logo_img = PhotoImage(file="logo.png")

canvas = Canvas(window, width=500, height=200)
canvas.create_image(150, 100, image=logo_img)
canvas.image = logo_img
canvas.grid(row=0, column=1)

message_label = Label(window,text="Message:",
                      font=("Consolas", 11, "bold"),
                      fg="#333333",
                      bg="#f5f5f5",
                      anchor="w"
                      )
message_label.grid(row=1,column=0)

message_entry = Entry(window,width=54)
message_entry.grid(row=1,column=1)
message_entry.focus()
message_entry.bind("<Return>", lambda event: on_convert_click())

convert_button = Button(text="Convert",
    font=("Arial", 11, "bold"),
    width=15,
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    command=on_convert_click)
convert_button.grid(row=1,column=2)

converted_text_label = Label(window,text="Converted Message:",
                             font=("Consolas", 11, "bold"),
                             fg="#333333",
                             bg="#f5f5f5",
                             anchor="w"
                             )
converted_text_label.grid(row=2,column=0)

converted_text_entry = Entry(window,width=54)
converted_text_entry.grid(row=2,column=1)

copy_button = Button(text="Copy",
    font=("Arial", 11, "bold"),
    width=15,
    bg="#607D8B",
    fg="white",
    activebackground="#455A64",
    command=copy_to_clipboard)
copy_button.grid(row=2,column=2)

sound_button = Button(
    text="Play Morse",
    font=("Arial", 11, "bold"),
    width=15,
    bg="#9C27B0",
    fg="white",
    activebackground="#7B1FA2",
    command=play_morse_sound)
sound_button.grid(row=3, column=1)

window.mainloop()
