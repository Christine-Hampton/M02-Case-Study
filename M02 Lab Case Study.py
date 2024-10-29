# Name: Christine Hampton
# File Name: student_gpa_checker.py
# Description: This app accepts student names and GPAs
# to determine if they qualify for the Dean's List
# or the Honor Roll.

def is_deans_list(gpa):
    return gpa - 3.5 >= 0
def is_honor_roll(gpa):
    return gpa - 3.25 >= 0

while True: 
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    if last_name == 'ZZZ':
        break

    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))

    if is_deans_list(gpa):
        print(f"{first_name} {last_name} made the Dean's List.")
    elif is_honor_roll(gpa):
        print(f"{first_name} {last_name} made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} did not qualify for the Dean's list or Honor Roll.")




