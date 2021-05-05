def prompt_user():
    student = Student()
    student.first_name = input("Please enter your first name: ")
    student.last_name = input("Please enter your last name: ")
    student.student_id = int(input("Please enter your id number: "))
    return student


def display_student(my_student):
    print()
    print("Your information:")
    print(f"{my_student.student_id} - {my_student.first_name} {my_student.last_name}")


class Student:

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.student_id = ""


def main():
    student = prompt_user()
    display_student(student)


if __name__ == '__main__':
    main()
