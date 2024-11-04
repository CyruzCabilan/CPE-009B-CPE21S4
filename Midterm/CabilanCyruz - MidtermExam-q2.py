import tkinter as tk

def change_color():
    button.config(bg='yellow')

# Create the main window
root = tk.Tk()
root.title("Special Midterm Exam in oop")

# Create a button
button = tk.Button(root, text="Click to change color", command=change_color)
button.pack(pady=50, padx=50)

# Run the application
root.mainloop()