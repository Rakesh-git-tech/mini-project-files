
def analyze_result(name, roll, marks):
    # Calculate total and average
    total = sum(marks)
    average = total / len(marks)

    # Assign grade
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    # Display student details
    print("Student Name:", name)
    print("Roll Number:", roll)
    print("Marks:", marks)
    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Grade:", grade)

    # Check subjects with marks below 40
    print("Subjects with marks below 40:")
    found = False

    for i in range(len(marks)):
        if marks[i] < 40:
            print("Subject", i + 1, ":", marks[i])
            found = True

    if not found:
        print("None")



# Sample Input
name = "Aarav"
roll = 101
marks = [88.5, 35.0, 76.0, 92.5, 48.0]

analyze_result(name, roll, marks)