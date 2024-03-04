import tkinter
import random
import tkinter.messagebox

root =  tkinter.Tk()

root.configure(bg = "white")
root.title("To Do List")
root.geometry("250x250")

tasks = []

def update_list_box():
    clear_list_box()
    for task in tasks:
        button_task_entry.insert("end", task)
        
def clear_list_box():
    button_task_entry.delete(0, "end")

def add_task():
    task = text_input.get()  #Get info from text entry
    if task != "":
        tasks.append(task)
        update_list_box()
    else:
        tkinter.messagebox.showwarning("Warning","You need to enter task.")
    text_input.delete(0, "end")  #Delete the contents of the input box

def delete_all():
    confirm = tkinter.messagebox.askyesno("Please Confirm", "Do you really want to delete the all items on the list? ")
    if confirm == True:
        global tasks
        tasks = []
        update_list_box()

def delete_one():
    task = button_task_entry.get("active")
    if task in tasks:
        tasks.remove(task)
    update_list_box()

def number_of_tasks():
    number_of_tasks = len(tasks)
    message = "Number of tasks: %s " %number_of_tasks
    label_display["text"] = message
    
#Create Widgets
label_title = tkinter.Label(root, text = "To-Do List", bg = "white")
label_title.grid(row = 0, column = 0)

label_display = tkinter.Label(root, text = "", bg = "white")
label_display.grid(row = 0, column = 1)

text_input = tkinter.Entry(root, width = 20)
text_input.grid(row = 1, column = 1)

button_add_task = tkinter.Button(root, text = "Add Task", fg = "green", bg = "white", command = add_task)
button_add_task.grid(row = 1, column = 0)

button_delete_all = tkinter.Button(root, text = "Delete All", fg = "green", bg = "white", command = delete_all)
button_delete_all.grid(row = 2, column = 0)

button_delete_one = tkinter.Button(root, text = "Delete One", fg = "green", bg = "white", command = delete_one)
button_delete_one.grid(row = 3, column = 0)

button_number_of_tasks = tkinter.Button(root, text = "Number Of Tasks", fg = "green", bg = "white", command = number_of_tasks)
button_number_of_tasks.grid(row = 4, column = 0)

button_exit = tkinter.Button(root, text = "Exit", fg = "green", bg = "white", command = root.destroy)
button_exit.grid(row = 5, column = 0)

button_task_entry = tkinter.Listbox(root)
button_task_entry.grid(row = 2, column = 1, rowspan = 7)


root.mainloop()