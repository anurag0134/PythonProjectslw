import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    contact_no = contact_no_entry.get()
    email_id = email_id_entry.get()
    whatsapp_no = whatsapp_no_entry.get()
    
    # You can add validation for each field here if needed
    if not name or not contact_no or not email_id or not whatsapp_no:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    
    # For demonstration purposes, we'll just print the values
    print(f"Name: {name}")
    print(f"Contact No: {contact_no}")
    print(f"Email ID: {email_id}")
    print(f"WhatsApp No: {whatsapp_no}")
    
    # You can also add code to save these details to a file or a database

    # Clear the fields after submission
    name_entry.delete(0, tk.END)
    contact_no_entry.delete(0, tk.END)
    email_id_entry.delete(0, tk.END)
    whatsapp_no_entry.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Inquiry Form")

# Create and place the labels and entry widgets
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Contact No:").grid(row=1, column=0, padx=10, pady=5)
contact_no_entry = tk.Entry(root)
contact_no_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email ID:").grid(row=2, column=0, padx=10, pady=5)
email_id_entry = tk.Entry(root)
email_id_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="WhatsApp No:").grid(row=3, column=0, padx=10, pady=5)
whatsapp_no_entry = tk.Entry(root)
whatsapp_no_entry.grid(row=3, column=1, padx=10, pady=5)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=4, columnspan=2, pady=10)

# Run the application
root.mainloop()
