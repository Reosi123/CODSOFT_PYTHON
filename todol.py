import sqlite3
from tkinter import *
from tkinter import messagebox

def setup_db():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 task TEXT NOT NULL,
                 status TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_task():
    task = entry_task.get()
    if task == "":
      messagebox.showwarning("Warning", "Task cannot be empty!")
      return
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task, status) VALUES (?, 'pending')", (task,))
    conn.commit()
    conn.close()
    entry_task.delete(0, END)
    show_tasks()

def show_tasks():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()
    conn.close()
    listbox_tasks.delete(0, END)
    for row in rows:
        listbox_tasks.insert(END, row)

def delete_task():
    selected_task = listbox_tasks.curselection()
    if not selected_task:
        messagebox.showwarning("Warning", "Select a task to delete!")
        return
    task_id = listbox_tasks.get(selected_task)[0]
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    show_tasks()

def update_task():
    selected_task = listbox_tasks.curselection()
    if not selected_task:
        messagebox.showwarning("Warning", "Select a task to update!")
        return
    task_id = listbox_tasks.get(selected_task)[0]
    new_status = entry_status.get()
    if new_status not in ["pending", "complete"]:
        messagebox.showwarning("Warning", "Status must be 'pending' or 'complete'!")
        return
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
    conn.commit()
    conn.close()
    show_tasks()

root = Tk()
root.title("To-Do List")

frame = Frame(root)
frame.pack(pady=10)

listbox_tasks = Listbox(frame, width=50, height=10)
listbox_tasks.pack(side=LEFT)

scrollbar_tasks = Scrollbar(frame)
scrollbar_tasks.pack(side=RIGHT, fill=Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = Entry(root, width=54)
entry_task.pack(pady=5)

entry_status = Entry(root, width=54)
entry_status.pack(pady=5)

button_add_task = Button(root, text="Add Task", command=add_task)
button_add_task.pack(pady=5)

button_delete_task = Button(root, text="Delete Task", command=delete_task)
button_delete_task.pack(pady=5)

button_update_task = Button(root, text="Update Task", command=update_task)
button_update_task.pack(pady=5)

setup_db()
show_tasks()

root.mainloop()
