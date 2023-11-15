import tkinter as tk
import keyboard

word = ""

def any_key_pressed(keyboard_event):
    global word
    word += "Get hacc nuub\n"
    result_label.config(text=word)

window = tk.Tk()
window.title("HackerTyper")
window.geometry("1280x720")
window.configure(bg="black")

result_label = tk.Label(window, fg="green",bg="black", font=("Arial", 18, "bold"))
result_label.pack(pady=20, anchor="w") 

keyboard.hook(any_key_pressed)
window.mainloop()