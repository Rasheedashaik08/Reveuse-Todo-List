import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        # Initialize task list
        self.tasks = []
        
        # Set up the GUI
        self.setup_ui()

    def setup_ui(self):
        # Title label
        self.title_label = tk.Label(self.root, text="To-Do List", font=("Helvetica", 16))
        self.title_label.pack(pady=10)
        
        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)
        
        # Buttons
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.edit_button = tk.Button(self.root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.complete_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.view_button = tk.Button(self.root, text="View Task", command=self.view_task)
        self.view_button.pack(side=tk.LEFT, padx=10, pady=10)

    def add_task(self):
        title = simpledialog.askstring("Input", "Enter task title:")
        if title:
            description = simpledialog.askstring("Input", "Enter task description:")
            priority = simpledialog.askstring("Input", "Enter task priority (High, Medium, Low):")
            due_date = simpledialog.askstring("Input", "Enter due date (YYYY-MM-DD):")
            
            task = {
                "title": title,
                "description": description,
                "priority": priority,
                "due_date": due_date,
                "completed": False
            }
            
            self.tasks.append(task)
            self.update_task_listbox()

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Warning", "Please select a task to edit")
            return

        selected_task = self.tasks[selected_task_index[0]]
        
        new_title = simpledialog.askstring("Input", "Edit task title:", initialvalue=selected_task['title'])
        if new_title:
            selected_task['title'] = new_title
        
        new_description = simpledialog.askstring("Input", "Edit task description:", initialvalue=selected_task['description'])
        if new_description:
            selected_task['description'] = new_description
        
        new_priority = simpledialog.askstring("Input", "Edit task priority (High, Medium, Low):", initialvalue=selected_task['priority'])
        if new_priority:
            selected_task['priority'] = new_priority
        
        new_due_date = simpledialog.askstring("Input", "Edit due date (YYYY-MM-DD):", initialvalue=selected_task['due_date'])
        if new_due_date:
            selected_task['due_date'] = new_due_date
        
        self.update_task_listbox()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Warning", "Please select a task to delete")
            return

        del self.tasks[selected_task_index[0]]
        self.update_task_listbox()

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Warning", "Please select a task to mark as complete")
            return
        
        self.tasks[selected_task_index[0]]['completed'] = True
        self.update_task_listbox()

    def view_task(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Warning", "Please select a task to view")
            return

        selected_task = self.tasks[selected_task_index[0]]
        task_details = (
            f"Title: {selected_task['title']}\n"
            f"Description: {selected_task['description']}\n"
            f"Priority: {selected_task['priority']}\n"
            f"Due Date: {selected_task['due_date']}\n"
            f"Completed: {'Yes' if selected_task['completed'] else 'No'}"
        )
        messagebox.showinfo("Task Details", task_details)

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = f"{task['title']} - {'Completed' if task['completed'] else 'Pending'}"
            self.task_listbox.insert(tk.END, display_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
