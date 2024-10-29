import tkinter as tk 
from tkinter import messagebox 
from datetime import datetime

root = tk.Tk() # for main window 
root.title("To-Do-List")
root.geometry("400x450")

tasks = [] #global list hold 

# default function for to do list
def update_listbox():
    task_listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks):
        status = 'Done' if task ['completed'] else 'Pending'
        display_task = f"{task['text']} - {status} - Due: {task ['due_date']} - priority: {task ['priority']}"
        task_listbox.insert(tk.END, f"{idx + 1}.{display_task}")


def create_task():
    task_text = task_entry.get()
    due_date = due_date_entry.get()
    priority = priority_var.get()
    
    if task_text and due_date:
        tasks.append({
            "text": task_text,
            "completed": False,
            "due_date": due_date,
            "priority": priority
        })
        task_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Input Error", "Task and Due Date cannot be empty!")




def mark_completed():
    try:
        selected_idx = task_listbox.curselection()[0]
        tasks[selected_idx]['complete'] = True
        tasks[selected_idx]['completion_date'] = datetime.now().strftime("%Y-%m-%d %H:%M :%S")
        update_listbox()
    except IndexError:
        messagebox.showwarning("mark th completed task")
        
        
def delete_task():
    try:
        selected_idx = task_listbox.curselection()[0]
        tasks.pop(selected_idx)
        update_listbox()
    except IndexError:
        messagebox.showwarning("atkeast select one task to delete")

# input fields 
task_entry = tk.Entry(root,width = 30, font = ('Arial', 14))
task_entry.pack(pady=6)

due_date_label= tk.Label(root,text = "Due Date (YYYY-MM-DD):") 
due_date_label.pack(pady=6)
due_date_entry = tk.Entry(root,width= 30, font = ('Arial', 12))
due_date_entry.pack(pady=6)

priority_var = tk.StringVar(value = "medium")
priority_label = tk.Label(root, text="Priority:")
priority_label.pack(pady=6)
priority_dropdown = tk.OptionMenu(root, priority_var, "High", "Medium", "Low")
priority_dropdown.pack(pady=6)


#create button 
create_btn = tk.Button(root, text="Create Task", command=create_task)
create_btn.pack(pady=6)

mark_done_btn = tk.Button(root, text="Mark as Completed", command=mark_completed)
mark_done_btn.pack(pady=6)

delete_task_btn = tk.Button(root, text= "Delete Task", command = delete_task)
delete_task_btn.pack(pady=6)

task_listbox = tk.Listbox(root, width=60, height=15, font=("Arial", 12))
task_listbox.pack(pady=10)


root.mainloop()

