import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to run Steghide
def run_steghide(password, carrier_path, secret_message_path):
    if not (password and carrier_path and secret_message_path):
        messagebox.showerror("Error", "All fields are required!")
        return

    command = f"steghide embed -cf {carrier_path} -ef {secret_message_path} -p {password}"
    try:
        os.system(command)
        messagebox.showinfo("Success", "Steghide operation completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run Steghide: {e}")

# Function to redirect to the Steghide page
def open_steghide_page():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Enter Steghide Details", font=("Arial", 16)).pack(pady=10)

    # Password input
    tk.Label(root, text="Password:").pack(anchor="w", padx=10)
    password_entry = tk.Entry(root, show="*", width=30)
    password_entry.pack(pady=5, padx=10)

    # Carrier file input
    tk.Label(root, text="Carrier File Path:").pack(anchor="w", padx=10)
    carrier_path_entry = tk.Entry(root, width=30)
    carrier_path_entry.pack(pady=5, padx=10)
    
    def browse_carrier():
        carrier_path = filedialog.askopenfilename()
        carrier_path_entry.delete(0, tk.END)
        carrier_path_entry.insert(0, carrier_path)

    tk.Button(root, text="Browse", command=browse_carrier).pack(pady=5)

    # Secret message file input
    tk.Label(root, text="Secret Message File:").pack(anchor="w", padx=10)
    secret_message_entry = tk.Entry(root, width=30)
    secret_message_entry.pack(pady=5, padx=10)

    def browse_message():
        secret_message_path = filedialog.askopenfilename()
        secret_message_entry.delete(0, tk.END)
        secret_message_entry.insert(0, secret_message_path)

    tk.Button(root, text="Browse", command=browse_message).pack(pady=5)

    # Run Steghide button
    tk.Button(
        root,
        text="Run Steghide",
        command=lambda: run_steghide(
            password_entry.get(),
            carrier_path_entry.get(),
            secret_message_entry.get()
        )
    ).pack(pady=20)

# Main page
root = tk.Tk()
root.title("Steghide GUI")
root.geometry("400x400")

# Main Label and Button
label = tk.Label(root, text="Welcome to Steghide GUI", font=("Arial", 16))
label.pack(pady=20)

open_button = tk.Button(root, text="Open Steghide Page", command=open_steghide_page)
open_button.pack(pady=20)

root.mainloop()
