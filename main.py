import os
import tkinter as tk
import keyboard
from PIL import Image, ImageTk

word = ""
Percentage = 0

def any_key_pressed(keyboard_event):
    global word, Percentage
    word += "Get hacc nuub\n"
    result_label.config(text=word)
    percentage_label.config(text=str(int(Percentage)) + "% Haccet inn i mainfram")
    Percentage += 0.1

    if int(Percentage) >= 101:
        path = os.getcwd() + "\\003 leker med python\\hackertyper\\HACKERTYPER\\anders18.png"
        image1 = Image.open(path)  # Correct the image file extension
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(window, image=test)
        label1.image = test
        label1.pack() 

        exit(0)

window = tk.Tk()
window.title("HackerTyper")
window.geometry("1280x720")
window.configure(bg="black")

percentage_label = tk.Label(window, fg="green", bg="black", font=("Arial", 50, "bold"))
percentage_label.pack(pady=20, anchor="center")

result_label = tk.Label(window, fg="green", bg="black", font=("Arial", 18, "bold"))
result_label.pack(pady=20, anchor="w") 

keyboard.hook(any_key_pressed)
window.mainloop()
