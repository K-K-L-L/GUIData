import tkinter as tk
import json
import email_validator

def save_data():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    data = {
        "name": name,
        "age": age,
        "email": email
    }
    if not name:
        return label.config(text="Please enter your name", fg="#A42A04")
    if not age.isdigit():
        return label.config(text="Please enter a valid age", fg="#A42A04")
    try:
        email_validator.validate_email(email)
    except email_validator.EmailNotValidError as e:
        return label.config(text=str(e), fg="#A42A04")
    try:
        with open("data.json", "r", encoding="utf-8") as f:
          existing_data = json.load(f)
    except FileNotFoundError:
        existing_data = []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        existing_data = []
    # Appends the data
    existing_data.append(data)
      # Writes the file as a .json file
    try:
        with open("data.json", "w", encoding="utf-8") as f:
          json.dump(existing_data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
    
    label.config(text="Data saved successfully!", fg="green")

root = tk.Tk()
root.geometry("400x350") # Set the window size to 200 pixels wide by 350 pixels tall

root.title("Save Data to JSON")
root.config(bg="#a69c9c")

name_label = tk.Label(root, text="Name:", bg="#a69c9c", fg="#212121")
name_entry = tk.Entry(root)

age_label = tk.Label(root, text="Age:", bg="#a69c9c", fg="#212121")
age_entry = tk.Entry(root)

email_label = tk.Label(root, text="Email:", bg="#a69c9c", fg="#212121")
email_entry = tk.Entry(root)

save_button = tk.Button(root, text="Save", bg="#007C92", fg="white", command=save_data, activebackground="#004D40", activeforeground="white", borderwidth=0, relief="solid", height=2, width=10, bd=0, overrelief="groove", cursor="hand2")

label = tk.Label(root, bg="#a69c9c", fg="#212121")

name_label.pack(pady=10)
name_entry.pack(pady=10)

age_label.pack(pady=10)
age_entry.pack(pady=10)

email_label.pack(pady=10)
email_entry.pack(pady=20)

save_button.pack(pady=10)

label.pack(pady=10)

root.mainloop()
