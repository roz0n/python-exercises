# Refactor this to a Student class

class_roster = []

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []

    def average_grades(self):
        total = len(self.grades)

        if total != 0:
            average = sum(self.grades) / total
        else:
            return 0

        return average


def launch_menu():
    user_selection = input("Enter 'p' to print the class roster, \n"
                           "'a' to add a new student to the roster, \n"
                           "'g' to add a grade to a student, \n"
                           "'q' to quit:\n"
                           "\n")

    while user_selection != "q":
        if user_selection == "p":
            class_report(class_roster)
        elif user_selection == "a":
            class_roster.append(create_student())
        elif user_selection == "g":
            student_id = input("\nEnter the student id: ")
            student = class_roster[int(student_id)]

            new_grade = input("\nEnter the grade to be added: ")
            add_grades(student, [int(new_grade)])
        else:
            print("\n That's an invalid entry, sorry.")

        user_selection = input("\nEnter 'p' to print the class roster, \n"
                               "'a' to add a new student to the roster, \n"
                               "'g' to add a grade to a student, \n"
                               "'q' to quit:\n"
                               "\n")


def create_student():
    first_name = input("\nEnter the student's first name: ")
    last_name = input("\nEnter the student's last name: ")

    student = Student(first_name, last_name)

    return student


def add_grades(student, grades):
    for grade in grades:
        student.grades.append(grade)

    return None


def student_report(student):
    return "Student name: {} {} \n Average grade: {} \n"\
            .format(student.first_name,
                    student.last_name,
                    student.average_grades())


def class_report(roster):
    # We'd be better off adding an ID here and not relying on the its index inside class_roster
    for i, student in enumerate(roster):
        print("ID: {}".format(i))
        print(student_report(student))

    return None


launch_menu()
