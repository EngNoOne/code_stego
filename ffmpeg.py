import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import os

FFMPEG_PATH = r"E:\lectures\semister 7\steganography\Stegno Project\Stegno Project\ffmpeg-master-latest-win64-gpl-shared\ffmpeg-master-latest-win64-gpl-shared\bin\ffmpeg.exe"  # حط الباث
#this function to center the pop up window
def center_window(root, width, height):
    """Centers the window on the screen."""
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

def animate_title(label):
    """Animates the title text with a glowing effect."""
    colors = ["#ff4444", "#44ff44", "#4444ff", "#ffff44", "#ff44ff"]
    index = 0

    def update_color():
        nonlocal index
        label.config(foreground=colors[index])
        index = (index + 1) % len(colors)
        label.after(400, update_color)

    update_color()

def on_button_hover(event):
    """Changes button background color on hover."""
    event.widget.config(bg="#0056b3", fg="white")

def on_button_leave(event):
    """Restores button background color when hover ends."""
    event.widget.config(bg="SystemButtonFace", fg="black")
#this function hides the message in the metafile data (specifically in header)
def conceal_message():
    """Conceals a message in the video metadata."""
    input_video = filedialog.askopenfilename(title="Select Input Video", filetypes=[("Video Files", "*.mp4")])
    if not input_video:
        return

    output_video = filedialog.asksaveasfilename(title="Save Output Video As", defaultextension=".mp4",
                                                filetypes=[("Video Files", "*.mp4")])
    if not output_video:
        return

    message = message_entry.get()

    if not message:
        messagebox.showerror("Error", "Message cannot be empty.")
        return

    try:
        #embed message in metadata
        command = [
            FFMPEG_PATH, "-i", input_video, "-metadata", f"comment={message}", "-c", "copy", output_video
        ]
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            messagebox.showinfo("Success", f"Message concealed in '{output_video}'.")
        else:
            messagebox.showerror("Error", result.stderr)
    except Exception as e:
        messagebox.showerror("Error", str(e))
#this function is to extract the secret message from the video metadata
def extract_message():
    """Extracts a message from the video metadata."""
    input_video = filedialog.askopenfilename(title="Select Input Video", filetypes=[("Video Files", "*.mp4")])
    if not input_video:
        return

    try:
        # extract metadata
        command = [FFMPEG_PATH, "-i", input_video, "-f", "ffmetadata", "-"]
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            metadata = result.stdout
            for line in metadata.splitlines():
                if line.startswith("comment="):
                    message = line.split("=", 1)[1]
                    messagebox.showinfo("Extracted Message", f"Message: {message}")
                    return
            messagebox.showinfo("No Message Found", "No concealed message found in the video.")
        else:
            messagebox.showerror("Error", result.stderr)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Main window setup
root = tk.Tk()
root.title("Video Metadata Steganography Tool")
window_width = 600
window_height = 300
center_window(root, window_width, window_height)

title = tk.Label(root, text="Video Steganography Tool", font=("Helvetica", 20, "bold"), fg="#ff4444")
title.grid(row=0, column=0, columnspan=2, pady=(20, 10))
animate_title(title)

# Message input
tk.Label(root, text="Message:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
message_entry = tk.Entry(root, width=40)
message_entry.grid(row=1, column=1, padx=10, pady=10)

# Buttons
conceal_button = tk.Button(root, text="Conceal Message", font=("Arial", 12), command=conceal_message)
conceal_button.grid(row=3, column=0, padx=10, pady=20)

extract_button = tk.Button(root, text="Extract Message", font=("Arial", 12), command=extract_message)
extract_button.grid(row=3, column=1, padx=10, pady=20)

# Bind hover effects to buttons
conceal_button.bind("<Enter>", on_button_hover)
conceal_button.bind("<Leave>", on_button_leave)
extract_button.bind("<Enter>", on_button_hover)
extract_button.bind("<Leave>", on_button_leave)

# Run the GUI
root.mainloop()