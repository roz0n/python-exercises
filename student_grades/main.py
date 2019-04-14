def create_student():
    first_name = input("Enter the student's first name: ")
    last_name = input("Enter the student's last name: ")

    student = {
        "first_name": first_name,
        "last_name": last_name,
        "grades": []
    }

    return student


def add_grades(student, grades):
    for grade in grades:
        student["grades"].append(grade)

    return None


def calculate_average(grades):
    total = len(grades)

    if total != 0:
        average = sum(grades) / total
    else:
        return 0

    return average


new_student = create_student()
add_grades(new_student, [100, 95, 100, 92, 75])
average_grades = calculate_average(new_student["grades"])

print(new_student)
print("{}%".format(average_grades))

