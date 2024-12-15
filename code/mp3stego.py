print("hello")
import os
import subprocess
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog


def center_window(width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')


root = Tk()
root.title("Steghide Tool - Embed & Extract Message")
root.config()
window_width = 800
window_height = 500
center_window(window_width, window_height)

# Function to embed message using Steghide
def steghide_embed(image_path, message_path, password):
    # Provide path to Steghide executable on your system
    steghide_path = r"E:\lectures\semister 7\steganography\project\steghide-0.5.1-win32\steghide\steghide.exe"  # Update this to the actual path of steghide.exe

    try:
        # Run steghide command to embed the secret message in the carrier image
        subprocess.run([steghide_path, "embed", "-cf", image_path, "-ef", message_path, "-p", password], check=True)
        messagebox.showinfo("Success", "Message embedded successfully!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to embed message. Check paths and try again.")



