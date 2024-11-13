from tkinter import *
from tkinter import filedialog

# Initialize the main window
root = Tk()
root.title("STUDENT MANAGER APP AND VISUALIZATION")
root.geometry("500x500")
root.minsize(300, 300)
root.maxsize(800, 800)
root.config(bg = "#808080")


root.iconbitmap("C:/Users/phath/Downloads/ueloz.ico")

# Function to open a file
def open_file():
    text_file = open(filedialog.askopenfilename(title="Select a file"), "r")
    data = text_file.read()
    text.insert(END, data)
    text_file.close()


# Function to save a file
def save_file():
    text_file = open(filedialog.asksaveasfilename(title="Save file as"), "w")
    text_file.write(text.get(1.0, END))
    text_file.close()


# Create a Text widget
text = Text(root, width=40, height=10, font=("Jetbrains Mono", 13))
text.pack(anchor="center")

# Create Open and Save buttons
open_button = Button(root, text="Open File", command=open_file)
open_button.pack(pady=10)

save_button = Button(root, text="Save File", command=save_file)
save_button.pack(pady=10)

# Run the application
root.mainloop()
