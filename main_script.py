import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
from cryptography import caesar_encrypt, caesar_decrypt, playfair_encrypt, playfair_decrypt, monoalphabetic_encrypt, monoalphabetic_decrypt

class CipherGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cipher GUI")

        # Use ThemedTk for a themed GUI
        self.master = ThemedTk(theme="clearlooks")  # You can choose a different theme

        # Set custom colors
        bg_color = "#ececec"  # Light gray background
        entry_bg_color = "#ffff58"  # White entry background
        entry_fg_color = "#1f6feb"  # Dark gray entry text color
        button_bg_color = "#4caf50"  # Green button background
        button_fg_color = "#1f6feb"  # White button text color

        # Set styles
        style = ttk.Style()
        style.configure("TLabel", background=bg_color)
        style.configure("TEntry", background=entry_bg_color, foreground=entry_fg_color)
        
        # Configure button colors
        style.configure("TButton", background=button_bg_color, foreground=button_fg_color)
        style.map("TButton",
                  background=[("pressed", "#45a049"), ("active", "#45a049")],
                  foreground=[("pressed", "#ffffff"), ("active", "#ffffff")])

        self.method_var = tk.StringVar()
        self.method_var.set("Caesar")  # Default to Caesar cipher

        self.method_menu = ttk.Combobox(master, textvariable=self.method_var, values=["Caesar", "Playfair", "Monoalphabetic"])
        self.method_menu.pack(pady=10)

        self.label_text = ttk.Label(master, text="Enter Text:")
        self.label_text.pack(pady=10)

        self.text_entry = ttk.Entry(master, width=40)
        self.text_entry.pack(pady=10)

        self.shift_label = ttk.Label(master, text="Shift Amount (for Caesar):")
        self.shift_label.pack(pady=10)

        self.shift_entry = ttk.Entry(master, width=40)
        self.shift_entry.pack(pady=10)

        self.label_key = ttk.Label(master, text="Enter Key (for Playfair):")
        self.label_key.pack(pady=10)

        self.key_entry = ttk.Entry(master, width=40)
        self.key_entry.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_var.set("Encrypt")  # Default to encryption

        self.encrypt_radio = ttk.Radiobutton(master, text="Encrypt", variable=self.radio_var, value="Encrypt")
        self.encrypt_radio.pack(pady=10)

        self.decrypt_radio = ttk.Radiobutton(master, text="Decrypt", variable=self.radio_var, value="Decrypt")
        self.decrypt_radio.pack(pady=10)

        self.submit_button = ttk.Button(master, text="Submit", command=self.apply_cipher)
        self.submit_button.pack(pady=20)

        self.result_entry = ttk.Entry(master, state="readonly", width=80)
        self.result_entry.pack(pady=20)

        self.copy_button = ttk.Button(master, text="Copy", command=self.copy_result)
        self.copy_button.pack(pady=20)

    def apply_cipher(self):
        text = self.text_entry.get()
        method = self.method_var.get()
        operation = self.radio_var.get()

        if method == "Caesar":
            shift = self.shift_entry.get()
            if not shift.isdigit():
                messagebox.showwarning("Input Error", "Please enter a valid shift amount for Caesar.")
                return
            shift = int(shift)
            if operation == "Encrypt":
                result_text = caesar_encrypt(text, shift)
            else:
                result_text = caesar_decrypt(text, shift)
        elif method == "Playfair":
            key = self.key_entry.get()
            if text and key:
                if operation == "Encrypt":
                    result_text = playfair_encrypt(text, key)
                else:
                    result_text = playfair_decrypt(text, key)
            else:
                messagebox.showwarning("Input Error", "Please enter text and key for Playfair.")
                return
        elif method == "Monoalphabetic":
            if text:
                if operation == "Encrypt":
                    result_text = monoalphabetic_encrypt(text)
                else:
                    result_text = monoalphabetic_decrypt(text)
            else:
                messagebox.showwarning("Input Error", "Please enter text for Monoalphabetic.")
                return

        self.update_result(result_text)

    def update_result(self, result_text):
        self.result_entry.config(state="normal")  # Enable the entry widget
        self.result_entry.delete(0, tk.END)  # Clear the result entry
        self.result_entry.insert(0, result_text)  # Update with the result
        self.result_entry.config(state="readonly")  # Disable the entry widget

    def copy_result(self):
        result_text = self.result_entry.get()
        self.master.clipboard_clear()
        self.master.clipboard_append(result_text)
        self.master.update()  # Required to ensure clipboard update
        messagebox.showinfo("Copy", "Result copied to clipboard.")

def main():
    root = ThemedTk(theme="clearlooks")  # You can choose a different theme
    app = CipherGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
