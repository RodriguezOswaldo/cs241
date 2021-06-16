
valid_input = False

while not valid_input:
    try:
        n = int(input("Enter a number: "))
        nby2 = n * 2
        print(f'The result is: {nby2}')
        valid_input = True
    except ValueError:
        print("The value entered is not valid")

# class InvalidInteger(Exception):
#     def __init__(self, message):
#         super().__init__(message)
# #
# #     if student.name == None:
# #         raise InvalidStudentError("The student must have a name")
#
