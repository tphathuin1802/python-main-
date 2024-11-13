# LIBRARY

import csv
from tabulate import tabulate

MINIMUM_CREDIT = 15  # condition

# Input file and print input table

input_path = "C:/Local Code/Projects/PyCharmProject/Chapter3Project/stack.csv"
output_path = "C:/Local Code/Projects/PyCharmProject/Chapter3Project/output_stack.csv"


# SUBFUNCTIONS

def input_table():
    list_candidate = []
    with open(input_path, "r", encoding="UTF-8") as input_file:
        candidate = csv.DictReader(input_file)
        for line in candidate:
            list_candidate.append(line)

    print(tabulate(
        list_candidate,
        headers=["Student Name", "Overall GPA", "Letter Grade", "Total Credits", "Scholar"],
        tablefmt="fancy_grid"
    ))


def calculate_average(list_courses):
    if not list_courses:  # Check if the list is empty
        return 0
    total_average = sum(list_courses) / len(list_courses)
    return total_average


def stack_average(values):
    if values > 8.5:
        return "A+"
    elif 8 <= values <= 8.5:
        return "A"
    elif 7 <= values < 8:
        return "B+"
    elif 6 <= values < 7:
        return "B"
    elif 5 <= values < 6:
        return "C"
    else:
        return "F, Fail"


def stack_scholar(total_average, student_credits):  # condition function
    if total_average >= 8 and student_credits >= MINIMUM_CREDIT:
        return True
    else:
        return False


def output_table(final_results):
    with open(output_path, "w", encoding="UTF-8", newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["Student Name", "Overall GPA", "Letter Grade", "Total Credits", "Scholar"])
        for student_name, overall_gpa, letter_grade, total_credits, scholar_status in final_results:
            writer.writerow([student_name, f"{overall_gpa:.2f}", letter_grade, total_credits, scholar_status])


# Main Function
def main():
    # CSV INPUT
    print("--------------------------------------------------")
    print("SAMPLE TABLE")

    input_table()

    students_averages = []
    student_gpas = {}
    student_credits = {}

    print("--------------------------------------------------")
    print("WELCOME TO GPA COUNTING AND ANALYSIS PROGRAM")
    print("--------------------------------------------------")
    print("""
            Select your choice of average point
            1. Average Grade Manually Input
            2. Average Grade Existed
            """)
    print("--------------------------------------------------")
    select = input("Enter your choice (1 or 2): ")

    # Setup constraint of course and student execution
    num_courses = int(input("Enter the number of courses: "))
    num_students = int(input("Enter the number of students: "))

    for i in range(num_courses):
        course_name = input(f"\nEnter the name of course {i + 1}: ")
        try:
            course_credit = float(input(f"Enter the credit for {course_name}: "))
        except ValueError:
            print("Invalid input for course credit. Skipping this course.")
            continue

        for j in range(num_students):
            student_name = input(f"Enter name of Student {j + 1}: ")

            try:
                if select == "1":
                    process = float(input("Input Process Grade: "))
                    mid_term = float(input("Input Midterm Grade: "))
                    end_term = float(input("Input Endterm Grade: "))
                    course_average = (20 / 100) * process + (30 / 100) * mid_term + (50 / 100) * end_term
                elif select == "2":
                    course_average = float(input(f"Enter the GPA for {course_name} for {student_name}: "))
                else:
                    print("Invalid choice. Skipping input for this student.")
                    continue
            except ValueError:
                print("Invalid grade input. Skipping this student's grade entry.")
                continue

            letter_grade = stack_average(course_average)
            scholar_status = stack_scholar(course_average, student_credits.get(student_name, 0))

            students_averages.append(
                (student_name, course_average, letter_grade, student_credits.get(student_name, 0), scholar_status))

            if student_name not in student_gpas:
                student_gpas[student_name] = []
            if student_name not in student_credits:
                student_credits[student_name] = 0

            student_gpas[student_name].append(course_average)
            student_credits[student_name] += course_credit

    # Prepare final results
    final_results = []
    for student_name, averages in student_gpas.items():
        total_average = calculate_average(averages)
        overall_letter_grade = stack_average(total_average)
        scholar_status = stack_scholar(total_average, student_credits[student_name])  # Determine scholar status

        # Format GPA to two decimal places for consistency
        final_results.append(
            [student_name, round(total_average, 2), overall_letter_grade, student_credits[student_name],
             scholar_status])

    # Final output
    print("\nFinal GPA Results:\n")
    print(tabulate(final_results, headers=["Student Name", "Overall GPA", "Letter Grade", "Total Credits", "Scholar"],
                   tablefmt="fancy_grid"))

    # CSV Output
    output_table(final_results)


if __name__ == "__main__":  # Execute Function
    main()
