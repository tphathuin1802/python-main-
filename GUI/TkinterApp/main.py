from tkinter import *
from tkinter import filedialog

# để bung ra 1 cửa sổ để chọn file, ta import filedialog

root = Tk()
root.title("Tkinter App")
root.iconbitmap("Project/PyCharmProject/Tkinter App/scoutapp_94109.ico")
root.geometry("500x500")
root.minsize(300, 300)
root.maxsize(800, 800)


def open_file():
    text_file = open(filedialog.askopenfilename(title="Select a file"))
    data = text_file.read()
    text.insert(END, data)
    text_file.close()


def save_file():
    text_file = open(
        filedialog.asksaveasfilename(title="Save file as"), mode="w"
    )
    data = text_file.write(text.get(1.0, END))
    text_file.close()


text = Text(root, width=40, height=10, font=("Jetbrains Mono", 13))
text.pack(anchor="center")

# nút mở và nút đóng:

open_button = Button(root, text="Open File", command=open_file)
open_button.pack(pady=10)

save_button = Button(root, text="Save file", command=save_file)
save_button.pack(pady=10)

root.mainloop()
