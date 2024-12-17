import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# Path to steghide executable
STEGHIDE_PATH = r"c:\\legion\\0xkillua\\stegano\\project\\steghide\\steghide.exe"
OUTPUT_DIR = r"c:\\legion\\0xkillua\\stegano\\project\\code"

# Color Scheme
BACKGROUND_COLOR = "#f0f0f0"
PRIMARY_COLOR = "#3498db"
SECONDARY_COLOR = "#2ecc71"
TEXT_COLOR = "#2c3e50"
ACCENT_COLOR = "#e74c3c"

class SteganoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography Toolbox")
        self.root.configure(bg=BACKGROUND_COLOR)
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Custom style configuration
        self.style.configure('TLabel', 
            background=BACKGROUND_COLOR, 
            foreground=TEXT_COLOR, 
            font=('Segoe UI', 10)
        )
        self.style.configure('TButton', 
            background=PRIMARY_COLOR, 
            foreground='white', 
            font=('Segoe UI', 10, 'bold')
        )
        self.style.configure('TEntry', 
            background='white', 
            foreground=TEXT_COLOR
        )
        
        self.create_ui()
        
    def create_ui(self):
        # Main frame with padding
        main_frame = ttk.Frame(self.root, padding="20 20 20 20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        main_frame.configure(style='TFrame')
        
        # Hide Section
        hide_frame = ttk.LabelFrame(main_frame, text="Hide Secret File", style='TLabelframe')
        hide_frame.pack(fill=tk.X, pady=(0, 10))
        
       #erorr
        secret_button = ttk.Button(
            secret_frame, 
            text="Browse", 
            command=lambda: self.upload_file(self.secret_entry),
            style='TButton'
        )
        secret_button.pack(side=tk.RIGHT)
        
        # Password input for Hiding
        password_frame = ttk.Frame(main_frame)
        password_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(password_frame, text="Password:", style='TLabel').pack(anchor='w')
        self.password_entry = ttk.Entry(password_frame, show="*", width=50)
        self.password_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))
        
        # Action buttons for Hide
        hide_action_frame = ttk.Frame(main_frame)
        hide_action_frame.pack(fill=tk.X, pady=(0, 20))
        
        hide_button = ttk.Button(
            hide_action_frame, 
            text="Hide", 
            command=self.hide_action,
            style='TButton'
        )
        hide_button.pack(side=tk.LEFT, padx=(0, 10))
        
        reset_hide_button = ttk.Button(
            hide_action_frame, 
            text="Reset", 
            command=self.reset_hide_fields,
            style='TButton'
        )
        reset_hide_button.pack(side=tk.LEFT)
        
        # Separator
        ttk.Separator(main_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        
        # Extract Section
        extract_frame = ttk.LabelFrame(main_frame, text="Extract Secret File", style='TLabelframe')
        extract_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Carrier file input for Extraction
        ttk.Label(extract_frame, text="Carrier File:", style='TLabel').pack(anchor='w')
        self.extract_carrier_entry = ttk.Entry(extract_frame, width=50)
        self.extract_carrier_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))
        
        extract_carrier_button = ttk.Button(
            extract_frame, 
            text="Browse", 
            command=lambda: self.upload_file(self.extract_carrier_entry),
            style='TButton'
        )
        extract_carrier_button.pack(side=tk.RIGHT)
        
        # Password input for Extraction
        extract_password_frame = ttk.Frame(main_frame)
        extract_password_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(extract_password_frame, text="Password:", style='TLabel').pack(anchor='w')
        self.extract_password_entry = ttk.Entry(extract_password_frame, show="*", width=50)
        self.extract_password_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))
        
        # Action buttons for Extract
        extract_action_frame = ttk.Frame(main_frame)
        extract_action_frame.pack(fill=tk.X)
        
        extract_button = ttk.Button(
            extract_action_frame, 
            text="Extract", 
            command=self.extract_action,
            style='TButton'
        )
        extract_button.pack(side=tk.LEFT, padx=(0, 10))
        
        reset_extract_button = ttk.Button(
            extract_action_frame, 
            text="Reset", 
            command=self.reset_extract_fields,
            style='TButton'
        )
        reset_extract_button.pack(side=tk.LEFT)
        
    def upload_file(self, entry):
        file_path = filedialog.askopenfilename()
        entry.delete(0, tk.END)
        entry.insert(0, file_path)
    
    def hide_action(self):
        carrier_path = self.carrier_entry.get()
        secret_path = self.secret_entry.get()
        password = self.password_entry.get()

        if not (carrier_path and secret_path):
            messagebox.showerror("Error", "Both files must be selected!")
            return

        if not password:
            messagebox.showerror("Error", "Password is required!")
            return

        # Ensure the output directory exists
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        # Run steghide embed command
        command = [
            STEGHIDE_PATH, "embed",
            "-cf", carrier_path,
            "-ef", secret_path,
            "-p", password
        ]
        try:
            result = subprocess.run(command, capture_output=True, text=True)
            if result.returncode == 0:
                messagebox.showinfo("Success", f"Hiding successful! File saved at:\n{carrier_path}")
            else:
                messagebox.showerror("Error", f"Steghide failed:\n{result.stderr}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run Steghide: {e}")
    
    def extract_action(self):
        carrier_path = self.extract_carrier_entry.get()
        password = self.extract_password_entry.get()

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
    
    def reset_hide_fields(self):
        self.carrier_entry.delete(0, tk.END)
        self.secret_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
    
    def reset_extract_fields(self):
        self.extract_carrier_entry.delete(0, tk.END)
        self.extract_password_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    root.title("Steganography Toolbox")
    
    # Center the window
    window_width = 600
    window_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    
    app = SteganoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
