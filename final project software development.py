import tkinter as tk
from tkinter import messagebox

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        
        self.categories = {
            "Donations": [],
            "Clothes": [],
            "Hygiene": [],
            "Supplies": []
        }
        
        self.create_widgets()
    
    def create_widgets(self):
        self.category_label = tk.Label(self.root, text="Select Category:")
        self.category_label.pack()
        
        self.category_var = tk.StringVar()
        self.category_var.set("Donations")
        self.category_menu = tk.OptionMenu(self.root, self.category_var, *self.categories.keys())
        self.category_menu.pack()
        
        self.item_label = tk.Label(self.root, text="Item Name:")
        self.item_label.pack()
        
        self.item_entry = tk.Entry(self.root)
        self.item_entry.pack()
        
        self.add_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.add_button.pack()
        
        self.view_button = tk.Button(self.root, text="View Inventory", command=self.view_inventory)
        self.view_button.pack()
    
    def add_item(self):
        category = self.category_var.get()
        item = self.item_entry.get().strip()
        
        if item:
            self.categories[category].append(item)
            messagebox.showinfo("Success", f"'{item}' added to {category}.")
            self.item_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter an item name.")
    
    def view_inventory(self):
        inventory_text = "\n".join([f"{cat}: {', '.join(items) if items else 'No items'}" for cat, items in self.categories.items()])
        messagebox.showinfo("Inventory", inventory_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
