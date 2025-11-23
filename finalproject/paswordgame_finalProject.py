import tkinter as tk
from PIL import Image, ImageTk
import string
import winsound
import os

completed_once = False
played_rule_sound = set()  # track which rules already played


def play_completion_sound():
    sound_path = "finalproject/thank_you.wav"  # renamed clean filename

    if os.path.exists(sound_path):
        try:
            winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
        except:
            winsound.Beep(800, 300)
    else:
        winsound.Beep(800, 300)


def check_rules(event=None):
    global completed_once

    password = entry_password.get()
    length_label.config(text=f"Length: {len(password)}")

    rules = {
        "At least 1 capital letter": any(c.isupper() for c in password),
        "At least 1 number": any(c.isdigit() for c in password),
        "At least 1 special character": any(c in string.punctuation for c in password),
        "Sum of all number have to equal to 25": sum(int(c) for c in password if c.isdigit()) == 25,
        "Does not contain the word 'password'": "password" not in password.lower()
    }

    for rule, label in rule_labels.items():
        if rules[rule]:
            label.config(text=f"✓ {rule}", fg="green", bg="#d4edda")

            # play sound ONCE per rule
            if rule not in played_rule_sound:
                winsound.PlaySound("finalproject/thank_you.wav",
                                   winsound.SND_FILENAME | winsound.SND_ASYNC)
                played_rule_sound.add(rule)

        else:
            label.config(text=f"✗ {rule}", fg="red", bg="#f8d7da")
            if rule in played_rule_sound:
                played_rule_sound.remove(rule)

    # All rules completed
    if all(rules.values()):
        if not completed_once:
            completed_once = True
            play_completion_sound()
            label_bg.config(image=background2)

            # Remove all UI
            title.destroy()
            frame_input.destroy()
            frame_rules.destroy()

    else:
        completed_once = False
        label_bg.config(image=background1)


# GUI
root = tk.Tk()
root.title("The Password Game")
root.geometry("600x700")

background1 = ImageTk.PhotoImage(Image.open("finalproject/monkey.jpg").resize((600, 700)))
background2 = ImageTk.PhotoImage(Image.open("finalproject/download.jpg").resize((600, 700)))

label_bg = tk.Label(root, image=background1)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

title = tk.Label(root, text="The Password Game", font=("Arial", 30, "bold"),
                 bg="black", fg="white")
title.pack(pady=30)

frame_input = tk.Frame(root, bg="#fdf8e4")
frame_input.pack(pady=20)

entry_password = tk.Entry(frame_input, width=30, font=("Georgia", 12))
entry_password.pack(side="left", padx=5)
entry_password.bind("<KeyRelease>", check_rules)

length_label = tk.Label(frame_input, text="Length: 0", font=("Georgia", 12), bg="#fdf8e4")
length_label.pack(side="left", padx=5)

frame_rules = tk.Frame(root, bg="#fdf8e4")
frame_rules.pack(pady=20, fill="x", padx=20)

rule_labels = {}
for rule in [
    "At least 1 capital letter",
    "At least 1 number",
    "At least 1 special character",
    "Sum of all number have to equal to 25",
    "Does not contain the word 'password'"
]:
    label = tk.Label(frame_rules, text=f"✗ {rule}", fg="red", bg="#f8d7da",
                     font=("Georgia", 12), width=50, anchor="w",
                     padx=10, pady=5)
    label.pack(pady=5, fill="x")
    rule_labels[rule] = label

check_rules()
root.mainloop()
