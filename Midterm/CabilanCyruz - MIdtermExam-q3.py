import tkinter as tk

def display_fullname():
    full_name = entry.get()
    label_result.config(text=f"Full Name: {full_name}")

root = tk.Tk()
root.title("Midterm in OOP")
root.geometry("400x200")

label_instruction = tk.Label(root, text="Enter your full name:", font=("Arial", 12))
label_instruction.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

button_display = tk.Button(root, text="Click to Display", command=display_fullname, font=("Arial", 12))
button_display.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=20)

root.mainloop()