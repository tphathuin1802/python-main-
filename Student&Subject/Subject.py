import random
import string

# Initialize constants
LETTER = string.ascii_letters
NUMBER = string.digits
PUNCTUATION = string.punctuation


def randomId():
    printable = f"{LETTER}{NUMBER}{PUNCTUATION}"
    printable = printable.upper()
    printable = list(printable)
    id_subject = "".join(random.choices(printable, k=8))
    return id_subject


class Subjects:
    def __init__(self, name, credit):
        self.idsubject = randomId()
        self.name = name
        self.credit = credit

    def __str__(self):
        return f"ID: {self.idsubject}, Name: {self.name}, Credit: {self.credit}"


class Student:
    def __init__(self, idstudent, name, classes, major):
        self.idstudent = idstudent
        self.name = name
        self.classes = classes
        self.major = major

    def __str__(self):
        return f"Student ID: {self.idstudent}, Name: {self.name}, Class: {self.classes}, Major: {self.major}"


list_subjects = []


def inputList():
    number = int(input("Enter number of subjects: "))
    for i in range(number):
        name = input("Enter subject name: ")
        credit = input("Enter subject credit: ")
        subject = Subjects(name, credit)
        list_subjects.append(subject)


def showSubjects():
    for subject in list_subjects:
        print(subject)


def main():
    inputList()
    showSubjects()


if __name__ == "__main__":
    main()
