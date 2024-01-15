#Michael Yisheng Han, Student Number 101157504
#Assignment 1, Problem 3
#displays assignments/exams, their max grade, and their weight
print("Assignment 1\t( /18)\nAssignment 2\t( /22)\nAssignment 3\t( /15)\nAssignment 4\t( /30)\nMidterm\t\t( /35)\nFinal Exam\t( /50)\n\n")
#mark for assignment 1
aOne = int(input("What was your mark for assignment 1 ( /18)? "))


#mark for assignment 2
aTwo = int(input("What was your mark for assignment 2 ( /22)? "))


#mark for assignment 3
aThree = int(input("What was your mark for assignment 3 ( /15)? "))


#mark for assignment 4
aFour = int(input("What was your mark for assignment 4 ( /30)? "))


#mark for midterm
mExam = int(input("What was your mark for the midterm ( /35)? "))


#mark for final exam
fExam = int(input("What was your mark for the final exam ( /50)? "))



#calculating percentages for each mark
p1 = float(aOne / 18)
p2 = float(aTwo / 22)
p3 = float(aThree / 15)
p4 = float(aFour / 30)
pm = float(mExam / 35)
pf = float(fExam / 50)
#turning decimals for each mark into percentages
per1 = float(p1 * 100)
per2 = float(p2 * 100)
per3 = float(p3 * 100)
per4 = float(p4 * 100)
perm = float(pm * 100)
perf = float(pf * 100)
#calculating weighted percentage of each grade
w1 = float(p1 * 0.1)
w2 = float(p2 * 0.1)
w3 = float(p3 * 0.1)
w4 = float(p4 * 0.1)
wm = float(pm * 0.25)
wf = float(pf * 0.35)
#calculating final grade using weighted percentages
fGrade = float(w1 + w2 + w3 + w4 + wm + wf)
#caculating final grade percentage
finalGrade = float(fGrade * 100)


#printing final grades table
print("\n\nGrades\n~~~~~~~~~~~~~~~~~~~~~~")
print(f"Assignment 1\t{per1:.2f}%")
print(f"Assignment 2\t{per2:.2f}%")
print(f"Assignment 3\t{per3:.2f}%")
print(f"Assignment 4\t{per4:.2f}%")
print(f"Midterm\t\t{perm:.2f}%")
print(f"Final Exam\t{perf:.2f}%")
print("~~~~~~~~~~~~~~~~~~~~~~")
print(f"Final grade is {finalGrade:.2f}%")