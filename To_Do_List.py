from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
Label(text="TO DO LIST", font=("Impact", "20"),highlightthickness=1, highlightbackground="red", padx=100, background="black",foreground="white").pack()
root.title("TODO APP")
root.resizable(0, 0)  
root.geometry("300x610")
f = Frame(root)
f.pack()
lbTask = Listbox(f,bg="white", fg="black", height=15, width=50,borderwidth=5,relief=SOLID, font="Consolas")
lbTask.pack(side=LEFT)
sbtask = Scrollbar(f)
sbtask.pack(side=RIGHT, fill=Y)
lbTask.config(yscrollcommand=sbtask.set)
sbtask.config(command=lbTask.yview)


def enterTask():
    def add():
        task = txtTask.get(1.0, "end-1c")
        if task=="":
            tmsg.showwarning(title="Warning!",
                             message="Please enter some text")
        else:
            lbTask.insert(END,task)
            dialog.destroy()
    dialog = Tk()
    dialog.title("Add Task")
    txtTask=Text(dialog,width=40, height=4)
    txtTask.pack()
    Button(dialog, text="Add task", command=add).pack()
    dialog.mainloop()

def deleteTask():
    selected = lbTask.curselection()
    lbTask.delete(selected[0])

def markCompleted():
    selected = lbTask.curselection()
    if selected:
        task_index = selected[0]
        task = lbTask.get(task_index)
        if not task.endswith(" ✔"):
            completed_task = task + " ✔"
            lbTask.delete(task_index)
            lbTask.insert(task_index, completed_task)

def clearTasks():
    lbTask.delete(0, END)


btnAdd=Button(root, text="ADD TASK",background="black",foreground="white",width=23,font=("Segoe UI Black Italic","14"),command=enterTask)
btnAdd.pack(pady=3)

btnDelete = Button(root, text="DELETE SELECTED TASK",background="black",foreground="white", width=23,font=("Segoe UI Black Italic","14"),command=deleteTask)
btnDelete.pack(pady=3)



btnMark = Button(root, text="MARK AS COMPLETED",background="black",foreground="white", width=23,font=("Segoe UI Black Italic","14"),command=markCompleted)
btnMark.pack(pady=3)

btnClear = Button(root, text="CLEAR ALL TASKS",background="black",foreground="white", width=23,font=("Segoe UI Black Italic","14"),command=clearTasks)
btnClear.pack(pady=3)
root.mainloop()
