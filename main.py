import tkinter as tk
import keyboard

word = ""

def any_key_pressed(keyboard_event):
    global word  # Use the global keyword to access the global variable
    word += "Get hacc nuub\n"

# Create the Tkinter window
window = tk.Tk()
window.title("HackerTyper")
window.geometry("1280x720")
window.configure(bg="black")

# Create a label to display the result
result_label = tk.Label(window, fg="green",bg="black", font=("Arial", 18, "bold"))
result_label.pack(pady=20, anchor="w")  # Use anchor="w" to align text to the left

# Bind the any_key_pressed function to any key press event
keyboard.hook(any_key_pressed)

# Start the Tkinter event loop
window.mainloop()


