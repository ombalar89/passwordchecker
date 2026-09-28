import re
import tkinter as tk
from tkinter import messagebox

# ---------------------------------------------------------
# FUNCTION: Logic to check password security level
# ---------------------------------------------------------
def check_password_strength():
    # Retrieve the password entered by the user in the text box
    password = entry.get()
    
    # Check 1: Minimum length requirement (at least 8 characters)
    if len(password) < 8:
        messagebox.showwarning(
            "Security Status", 
            "🔴 WEAK: Password must be at least 8 characters long!"
        )
    # Check 2: Must contain at least one lowercase letter (a-z)
    elif not re.search("[a-z]", password):
        messagebox.showwarning(
            "Security Status", 
            "🟡 MEDIUM: Include at least one lowercase letter (a-z)."
        )
    # Check 3: Must contain at least one uppercase letter (A-Z)
    elif not re.search("[A-Z]", password):
        messagebox.showwarning(
            "Security Status", 
            "🟡 MEDIUM: Include at least one uppercase letter (A-Z)."
        )
    # Check 4: Must contain at least one numerical digit (0-9)
    elif not re.search("[0-9]", password):
        messagebox.showwarning(
            "Security Status", 
            "🟡 MEDIUM: Include at least one number (0-9)."
        )
    # Check 5: Must contain at least one special character (@, #, $, %, etc.)
    elif not re.search("[_@$#%!]", password):
        messagebox.showwarning(
            "Security Status", 
            "🟡 MEDIUM: Include at least one special character (@, #, $, %, _)."
        )
    # If all security rules are passed:
    else:
        messagebox.showinfo(
            "Security Status", 
            "🟢 STRONG: Your password meets all security criteria!"
        )

# ---------------------------------------------------------
# GRAPHICAL USER INTERFACE (GUI) SETUP
# ---------------------------------------------------------
# Initialize the main application window
app = tk.Tk()
app.title("Cybersecurity - Password Strength Checker")
app.geometry("400x250")
app.config(bg="#f4f4f9")

# Add a Heading Label
label_title = tk.Label(
    app, 
    text="Password Security Analyzer", 
    font=("Arial", 14, "bold"), 
    bg="#f4f4f9", 
    fg="#333333"
)
label_title.pack(pady=15)

# Add an Instruction Label
label_instruction = tk.Label(
    app, 
    text="Enter a password to test:", 
    font=("Arial", 10), 
    bg="#f4f4f9"
)
label_instruction.pack()

# Input Field (Entry box) where users type the password
# Note: show="*" masks the input characters for privacy
entry = tk.Entry(app, show="*", font=("Arial", 12), width=25)
entry.pack(pady=10)

# Action Button to trigger the evaluation
btn = tk.Button(
    app, 
    text="Analyze Security", 
    font=("Arial", 11, "bold"), 
    bg="#4CAF50", 
    fg="white", 
    command=check_password_strength
)
btn.pack(pady=15)

# Keep the application window open and listening for user events
app.mainloop()