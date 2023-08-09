import os
import tkinter as tk
from tkinter import filedialog

def search_folder(directory, search_term):
    found_items = []
    for root, dirs, files in os.walk(directory):
        for item in files + dirs:
            if search_term.lower() in item.lower():
                found_items.append(os.path.join(root, item))
    return found_items

def search_button_click():
    search_directory = directory_var.get()
    search_term = search_term_var.get()
    search_results = search_folder(search_directory, search_term)

    result_text.delete(1.0, tk.END)
    if not search_results:
        result_text.insert(tk.END, "No items found.")
    else:
        for item in search_results:
            result_text.insert(tk.END, item + "\n")

def browse_button_click():
    directory = filedialog.askdirectory()
    directory_var.set(directory)

# Create the main window
root = tk.Tk()
root.title("Folder Search Engine")

# Create and place widgets
directory_var = tk.StringVar()
search_term_var = tk.StringVar()

directory_label = tk.Label(root, text="Directory:")
directory_label.pack()

directory_entry = tk.Entry(root, textvariable=directory_var)
directory_entry.pack()

browse_button = tk.Button(root, text="Browse", command=browse_button_click)
browse_button.pack()

search_term_label = tk.Label(root, text="Search Term:")
search_term_label.pack()

search_term_entry = tk.Entry(root, textvariable=search_term_var)
search_term_entry.pack()

search_button = tk.Button(root, text="Search", command=search_button_click)
search_button.pack()

result_text = tk.Text(root, wrap=tk.WORD, width=50, height=10)
result_text.pack()

# Start the GUI event loop
root.mainloop()
