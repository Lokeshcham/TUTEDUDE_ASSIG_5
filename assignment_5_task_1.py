# Creating a dictionary of student marks
student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
    "Eve": 88
}

# Asking the user to input a student's name
student_name = input("Enter the student's name: ")

# Retrieving and displaying the corresponding marks
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found in the records.")
