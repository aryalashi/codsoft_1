import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

class ToDoList(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("400x400")

        Style().theme_use("cyborg")

        self.create_widgets()

    def create_widgets(self):
        self.task_entry = ttk.Entry(self, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = ttk.Button(self, text="Add", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.delete_button = ttk.Button(self, text="Delete", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=10, pady=10)

        self.tasks_listbox = tk.Listbox(self, width=40, height=20)
        self.tasks_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_task = self.tasks_listbox.curselection()
        if selected_task:
            self.tasks_listbox.delete(selected_task)

if __name__ == "__main__":
    app = ToDoList()
    app.mainloop()