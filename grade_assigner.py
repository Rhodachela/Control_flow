student_score =float(input("Enter your score: "))

if student_score >= 90:
    grade= "A"
elif student_score >= 80:
    grade = "B"
elif student_score >= 70:
    grade = "C"
elif student_score >= 60:
    grade = "D"
else:
    grade = "E"

print("Your grade is: " + str(grade))