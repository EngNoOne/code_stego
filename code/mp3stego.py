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


# Function to extract message using Steghide
def steghide_extract(stego_image_path, password, output_path):
    steghide_path = r"E:\lectures\semister 7\steganography\project\steghide-0.5.1-win32\steghide\steghide.exe"  # Update this to the actual path of steghide.exe

    try:
        # Run steghide command to extract the secret message from the stego image
        subprocess.run([steghide_path, "extract", "-sf", stego_image_path, "-p", password, "-xf", output_path], check=True)
        messagebox.showinfo("Success", f"Message extracted successfully! Saved to {output_path}")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to extract message. Check paths and try again.")


# Function to select the carrier image file
def upload_carrier_file():
    filename = filedialog.askopenfilename(title="Select Carrier Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if filename:
        path_carrier_img.delete(0, END)
        path_carrier_img.insert(0, filename)


# Function to select the secret message file
def upload_secret_message():
    filename = filedialog.askopenfilename(title="Select Secret Message", filetypes=[("Text Files", "*.txt")])
    if filename:
        path_secret_message.delete(0, END)
        path_secret_message.insert(0, filename)


# Function to select the stego image for extraction
def upload_stego_image():
    filename = filedialog.askopenfilename(title="Select Stego Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if filename:
        path_stego_img.delete(0, END)
        path_stego_img.insert(0, filename)


# Function to clear all input fields
def clear_form():
    path_carrier_img.delete(0, 'end')
    path_secret_message.delete(0, 'end')
    password.delete(0, 'end')
    path_stego_img.delete(0, 'end')
    path_extract_message.delete(0, 'end')


# Function to hide message using the input data
def hide_message():
    carrier_file = path_carrier_img.get()
    secret_message = path_secret_message.get()
    passphrase = password.get()

    if carrier_file and secret_message and passphrase:
        steghide_embed(carrier_file, secret_message, passphrase)
    else:
        messagebox.showerror("Error", "Please fill in all fields.")


# Function to extract message using the input data
def extract_message():
    stego_file = path_stego_img.get()
    passphrase = password.get()
    output_file = path_extract_message.get()

    if stego_file and passphrase and output_file:
        steghide_extract(stego_file, passphrase, output_file)
    else:
        messagebox.showerror("Error", "Please fill in all fields.")


# UI setup
title = ttk.Label(root, text="Steghide Tool - Embed & Extract Message", font="Ubuntu 20 bold")
title.grid(row=0, column=0, columnspan=6, padx=20, pady=10)

# Carrier file label and input (for embedding)
path_carrier_img_label = ttk.Label(root, text="Path of Carrier Image")
path_carrier_img_label.grid(row=1, column=0, padx=10, pady=10)

path_carrier_img = ttk.Entry(root, width=50)
path_carrier_img.grid(row=1, column=1, padx=10, pady=10)

btn_upload_carrier = ttk.Button(root, text="Upload Carrier Image", command=upload_carrier_file)
btn_upload_carrier.grid(row=1, column=2, padx=10, pady=10)

# Secret message label and input (for embedding)
path_secret_message_label = ttk.Label(root, text="Path of Secret Message")
path_secret_message_label.grid(row=2, column=0, padx=10, pady=10)

path_secret_message = ttk.Entry(root, width=50)
path_secret_message.grid(row=2, column=1, padx=10, pady=10)

btn_upload_message = ttk.Button(root, text="Upload Secret Message", command=upload_secret_message)
btn_upload_message.grid(row=2, column=2, padx=10, pady=10)

# Password input
pass_label = ttk.Label(root, text="Enter Password")
pass_label.grid(row=3, column=0, padx=10, pady=10)

password = ttk.Entry(root, width=20, show="*")  # Hide input
password.grid(row=3, column=1, padx=10, pady=10)

# Embed Message Button
btn_embed = ttk.Button(root, text="Embed Message", command=hide_message)
btn_embed.grid(row=4, column=1, padx=10, pady=20)

# Extraction Section
title_extract = ttk.Label(root, text="Steghide Tool - Extract Message", font="Ubuntu 20 bold")
title_extract.grid(row=5, column=0, columnspan=6, padx=20, pady=10)

# Stego image label and input (for extraction)
path_stego_img_label = ttk.Label(root, text="Path of Stego Image")
path_stego_img_label.grid(row=6, column=0, padx=10, pady=10)

path_stego_img = ttk.Entry(root, width=50)
path_stego_img.grid(row=6, column=1, padx=10, pady=10)

btn_upload_stego = ttk.Button(root, text="Upload Stego Image", command=upload_stego_image)
btn_upload_stego.grid(row=6, column=2, padx=10, pady=10)

# Extracted message output file label
path_extract_message_label = ttk.Label(root, text="Output File for Extracted Message")
path_extract_message_label.grid(row=7, column=0, padx=10, pady=10)

path_extract_message = ttk.Entry(root, width=50)
path_extract_message.grid(row=7, column=1, padx=10, pady=10)

# Extract Button
btn_extract = ttk.Button(root, text="Extract Message", command=extract_message)
btn_extract.grid(row=8, column=1, padx=10, pady=20)

# Clear Button
btn_clear = ttk.Button(root, text="Clear", command=clear_form)
btn_clear.grid(row=9, column=1, padx=10, pady=20)

# Exit Button
btn_exit = ttk.Button(root, text="Exit", command=root.quit)
btn_exit.grid(row=9, column=2, padx=10, pady=20)

root.mainloop()
