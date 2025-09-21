def askForNumber():
    grades = []
    grades.append(int(input("Enter grade number: ")))
    grades.append(int(input("Enter grade number: ")))
    grades.append(int(input("Enter grade number: ")))
    grades.append(int(input("Enter grade number: ")))
    grades.append(int(input("Enter grade number: ")))
    return grades

nameStudent = str(input("Enter student name: "))
gradeList = askForNumber()
totalGrade = gradeList[0]+ gradeList[1]+gradeList[2]+ gradeList[3]+gradeList[4]
averageGrade = float(totalGrade/5)
if averageGrade >= 90:
    letterGrade = "A"
elif averageGrade >= 80:
    letterGrade = "B"
elif averageGrade >= 70:
    letterGrade = "C"
elif averageGrade >= 60:
    letterGrade = "D"
else:
    letterGrade = "F"

print()

print(nameStudent)
print(f"Average: {averageGrade}")
print(f"Letter grade: {letterGrade}")


