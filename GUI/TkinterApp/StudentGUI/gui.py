from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk

# root pack
root = Tk()
root.title("Student Management System")
root.iconbitmap("PyCharmProject/StudentGUI/manage.ico")
root.minsize(300, 300)
root.maxsize(650, 650)
root.resizable(False, False)
root.attributes("-alpha", 0.9)

# body
Label(
    root,
    text="Welcome to Student Management System",
    fg="purple",
    font=("SF Mono", 10, "bold"),
).pack(padx=5)
# image:

img_path = "PyCharmProject/StudentGUI/student.png"
img = Image.open(img_path)
img = img.resize((300, 300))
photo = ImageTk.PhotoImage(img)

img = PhotoImage(
    file="PyCharmProject/StudentGUI/student.png", height=200, width=200
)

button = Button(root, text="Import file")


# function:
def import_file():
    file_import = filedialog.askopenfilename()
    file_import.read()
    print(file_import)


def save_file():
    file_save = filedialog.asksaveasfilename()
    file_save.write()
    print(file_save)


Label(root, image=img, padx=5, pady=5).pack()
student_button = Button(
    root, text="Import file of Students", command=import_file
)


# show GUI (Graphical User Interface)
root.mainloop()
