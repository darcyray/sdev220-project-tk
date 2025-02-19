import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3

# Create database
conn = sqlite3.connect('clothes_closet.db')
cursor = conn.cursor()

# Create table
cursor.execute("""CREATE TABLE donations (
    id INTEGER PRIMARY KEY,
    item_name TEXT NOT NULL,
    category TEXT NOT NULL,
    quantity INTEGER NOT NULL
)"""
)

conn.commit()
conn.close()

# GUI
root = tk.Tk()
root.title("Donation Manager")
root.geometry("500x500")
root.configure(bg="#F0F0F0")

root.mainloop()