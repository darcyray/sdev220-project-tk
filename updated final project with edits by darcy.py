import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Added Item and Category class to better manage inventory and allow main class to utilize them
class Item:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

class Category:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, item_name):
        item = Item(item_name)
        self.items.append(item)
    
    def get_items(self):
        return [str(item) for item in self.items] if self.items else ["No items"]

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("700x500")  # Increased window size
        
        self.categories = {
            "Donations": Category("Donations"),
            "Clothes": Category("Clothes"),
            "Hygiene": Category("Hygiene"),
            "Supplies": Category("Supplies")
        }
        
        self.create_widgets()
    
    def create_widgets(self):
        frame = tk.Frame(self.root, bd=10, relief="ridge")
        frame.place(relx=0.5, rely=0.4, anchor="center", width=500, height=250)
        
        # Load background image for the frame
        self.frame_bg_image = Image.open("assets/bg for categories.jpg")
        self.frame_bg_image = self.frame_bg_image.resize((500, 250), Image.Resampling.LANCZOS)
        self.frame_bg_photo = ImageTk.PhotoImage(self.frame_bg_image)
        
        self.frame_bg_label = tk.Label(frame, image=self.frame_bg_photo)
        self.frame_bg_label.place(relwidth=1, relheight=1)
        
        self.category_label = tk.Label(frame, text="Select Category:", bg="white", font=("Arial", 14, "bold"))
        self.category_label.pack(pady=5)
        
        self.category_var = tk.StringVar()
        self.category_var.set("Donations")
        self.category_menu = tk.OptionMenu(frame, self.category_var, *self.categories.keys())
        self.category_menu.config(font=("Arial", 12))
        self.category_menu.pack(pady=5)
        
        input_frame = tk.Frame(self.root, bg="#f4e1e6")
        input_frame.place(relx=0.5, rely=0.7, anchor="center")
        
        self.item_entry = tk.Entry(input_frame, font=("Arial", 12), width=25, relief="ridge", bd=3)
        self.item_entry.grid(row=0, column=0, padx=10)
        
        self.add_button = tk.Button(input_frame, text="Add Item", command=self.add_item, bg="#b56576", fg="white", font=("Arial", 12, "bold"), relief="ridge", bd=3, padx=10, pady=5)
        self.add_button.grid(row=0, column=1, padx=10)
        
        self.view_button = tk.Button(input_frame, text="View Inventory", command=self.view_inventory, bg="#b56576", fg="white", font=("Arial", 12, "bold"), relief="ridge", bd=3, padx=10, pady=5)
        self.view_button.grid(row=0, column=2, padx=10)
    
    def add_item(self):
        category_name = self.category_var.get()
        item_name = self.item_entry.get().strip()
        
        if item_name:
            self.categories[category_name].add_item(item_name)
            messagebox.showinfo("Success", f"'{item_name}' added to {category_name}.")
            self.item_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter an item name.")
    
    def view_inventory(self):
        inventory_text = "\n".join([f"{cat}: {', '.join(self.categories[cat].get_items())}" for cat in self.categories])
        messagebox.showinfo("Inventory", inventory_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()