import os
import shutil
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

# Path to steghide executable
STEGHIDE_PATH = r"F:\\BFCAI\\lv4s1\\stegano\\project\\steghide\\steghide.exe"
OUTPUT_DIR = r"F:\\BFCAI\\lv4s1\\stegano\\project\\code"

# Function to handle upload carrier button
def upload_carrier(carrier_entry):
    carrier_path = filedialog.askopenfilename()
    carrier_entry.delete(0, tk.END)
    carrier_entry.insert(0, carrier_path)

# Function to handle upload secret button
def upload_secret(secret_entry):
    secret_path = filedialog.askopenfilename()
    secret_entry.delete(0, tk.END)
    secret_entry.insert(0, secret_path)

# Function for hide button
def hide_action(carrier_path, secret_path, password):
    if not (carrier_path and secret_path):
        messagebox.showerror("Error", "Both files must be selected!")
        return

    if not password:
        messagebox.showerror("Error", "Password is required!")
        return

    # Ensure the output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Copy carrier file to output directory
    copied_carrier_path = os.path.join(OUTPUT_DIR, os.path.basename(carrier_path))
    try:
        shutil.copy(carrier_path, copied_carrier_path)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to copy carrier file: {e}")
        return

    # Run steghide embed command
    command = [
        STEGHIDE_PATH, "embed",
        "-cf", copied_carrier_path,
        "-ef", secret_path,
        "-p", password
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("Success", f"Hiding successful! Output file:\n{copied_carrier_path}")
        else:
            messagebox.showerror("Error", f"Steghide failed:\n{result.stderr}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run Steghide: {e}")

# Function for extract button
def extract_action(carrier_path, password):
    if not carrier_path:
        messagebox.showerror("Error", "Carrier file must be selected!")
        return

    if not password:
        messagebox.showerror("Error", "Password is required!")
        return

    # Ask for output directory for the extracted file
    output_file = filedialog.asksaveasfilename(title="Save Extracted File As")
    if not output_file:
        messagebox.showinfo("Info", "Extraction cancelled.")
        return

    # Run steghide extract command
    command = [
        STEGHIDE_PATH, "extract",
        "-sf", carrier_path,
        "-xf", output_file,
        "-p", password
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("Success", f"Extraction successful! File saved at:\n{output_file}")
        else:
            messagebox.showerror("Error", f"Steghide failed:\n{result.stderr}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run Steghide: {e}")

# Main page
root = tk.Tk()
root.title("File Upload GUI")
root.geometry("600x400")

# Configure grid for responsiveness
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(9, weight=1)

# Create a container frame
frame = tk.Frame(root)
frame.grid(sticky="nsew", padx=20, pady=20)

# Carrier file input
carrier_label = tk.Label(frame, text="Carrier File:", font=("Arial", 12))
carrier_label.grid(row=0, column=0, sticky="w", pady=5)
carrier_entry = tk.Entry(frame, width=50)
carrier_entry.grid(row=0, column=1, pady=5, padx=10)
carrier_button = tk.Button(frame, text="Upload Carrier", command=lambda: upload_carrier(carrier_entry))
carrier_button.grid(row=0, column=2, pady=5, padx=10)

# Secret file input
secret_label = tk.Label(frame, text="Secret File:", font=("Arial", 12))
secret_label.grid(row=1, column=0, sticky="w", pady=5)
secret_entry = tk.Entry(frame, width=50)
secret_entry.grid(row=1, column=1, pady=5, padx=10)
secret_button = tk.Button(frame, text="Upload Secret", command=lambda: upload_secret(secret_entry))
secret_button.grid(row=1, column=2, pady=5, padx=10)

# Password input
password_label = tk.Label(frame, text="Password:", font=("Arial", 12))
password_label.grid(row=2, column=0, sticky="w", pady=5)
password_entry = tk.Entry(frame, show="*", width=50)
password_entry.grid(row=2, column=1, pady=5, padx=10)

# Hide button
hide_button = tk.Button(
    frame, text="Hide", font=("Arial", 12),
    command=lambda: hide_action(carrier_entry.get(), secret_entry.get(), password_entry.get())
)
hide_button.grid(row=3, column=0, columnspan=3, pady=10)

# Extract button
extract_button = tk.Button(
    frame, text="Extract", font=("Arial", 12),
    command=lambda: extract_action(carrier_entry.get(), password_entry.get())
)
extract_button.grid(row=4, column=0, columnspan=3, pady=10)

# Center the frame
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)

root.mainloop()
