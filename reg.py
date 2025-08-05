import tkinter as tk
from tkinter import messagebox, scrolledtext
import pandas as pd
import os

# Define the name of the Excel file
EXCEL_FILE = 'registration_data.xlsx'

class RegistrationApp:
    """
    A Tkinter application for user registration that saves and retrieves data
    from an Excel file.
    """
    def __init__(self, master):
        self.master = master
        master.title("Registration Form")
        master.geometry("600x500")
        master.resizable(False, False)

        # Main frame for padding
        self.main_frame = tk.Frame(master, padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.create_widgets()

    def create_widgets(self):
        """
        Creates all the widgets for the GUI window (labels, entries, buttons).
        """
        # --- Input Section ---
        input_frame = tk.LabelFrame(self.main_frame, text="User Registration", padx=10, pady=10)
        input_frame.pack(pady=10, fill=tk.X)

        # Name Input
        self.name_label = tk.Label(input_frame, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.name_entry = tk.Entry(input_frame, width=40)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Email Input
        self.email_label = tk.Label(input_frame, text="Email:")
        self.email_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.email_entry = tk.Entry(input_frame, width=40)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        # Phone Input
        self.phone_label = tk.Label(input_frame, text="Phone:")
        self.phone_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.phone_entry = tk.Entry(input_frame, width=40)
        self.phone_entry.grid(row=2, column=1, padx=5, pady=5)

        # --- Buttons Section ---
        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(pady=10)

        self.save_button = tk.Button(button_frame, text="Save to Excel", command=self.save_to_excel, width=15)
        self.save_button.pack(side=tk.LEFT, padx=10)

        self.retrieve_button = tk.Button(button_frame, text="Retrieve Data", command=self.retrieve_from_excel, width=15)
        self.retrieve_button.pack(side=tk.LEFT, padx=10)

        # --- Display Section ---
        display_frame = tk.LabelFrame(self.main_frame, text="Retrieved Data", padx=10, pady=10)
        display_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.data_display = scrolledtext.ScrolledText(display_frame, wrap=tk.WORD, width=60, height=10)
        self.data_display.pack(fill=tk.BOTH, expand=True)

    def save_to_excel(self):
        """
        Saves the user input from the entry fields to the Excel file.
        It appends data if the file exists, or creates a new file if it doesn't.
        """
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        if not name or not email or not phone:
            messagebox.showwarning("Incomplete Data", "Please fill in all fields.")
            return

        # Create a new DataFrame with the current data
        new_data = pd.DataFrame([{'Name': name, 'Email': email, 'Phone': phone}])

        try:
            if os.path.exists(EXCEL_FILE):
                # If the file exists, read it and append the new data
                existing_df = pd.read_excel(EXCEL_FILE)
                updated_df = pd.concat([existing_df, new_data], ignore_index=True)
                updated_df.to_excel(EXCEL_FILE, index=False)
            else:
                # If the file doesn't exist, create a new one
                new_data.to_excel(EXCEL_FILE, index=False)

            messagebox.showinfo("Success", "Registration data saved successfully!")
            self.clear_entries()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the data: {e}")

    def retrieve_from_excel(self):
        """
        Reads all data from the Excel file and displays it in the scrolled text widget.
        """
        # Clear the display area first
        self.data_display.delete(1.0, tk.END)

        try:
            if os.path.exists(EXCEL_FILE):
                # Read the data from the Excel file
                df = pd.read_excel(EXCEL_FILE)

                if not df.empty:
                    # Convert the DataFrame to a string and insert into the text widget
                    self.data_display.insert(tk.END, df.to_string(index=False))
                else:
                    self.data_display.insert(tk.END, "Excel file is empty.")
                    messagebox.showinfo("Empty File", "The Excel file is empty.")
            else:
                self.data_display.insert(tk.END, "No registration data found.")
                messagebox.showwarning("File Not Found", "The Excel file does not exist yet.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while retrieving the data: {e}")
            self.data_display.insert(tk.END, f"Error: {e}")

    def clear_entries(self):
        """
        Clears the text in all the input entry fields.
        """
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

# Main block to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationApp(root)
    root.mainloop()
