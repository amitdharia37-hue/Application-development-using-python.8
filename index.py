print("===== STUDENT REPORT CARD =====")

name = input("enter student name: ")

m1 = int(input("enter marks of english: "))
m2 = int(input("enter marks of maths: "))
m3 = int(input("enter marks of science: "))
m4 = int(input("enter marks of sst: "))
m5 = int(input("enter marks of computer: "))
total = m1 + m2+ m3+ m4+ m5
percentage = total / 5

print("student name:", name)
print("total marks:",total)
print("percentage:",percentage)
# grade calculation
if percentage >= 90:
    grade = "a+"
elif percentage >= 75:
    grade = "a"
elif percentage >= 60:
    grade = "b"
elif percentage >= 40:
    grade = "c"
else:
    grade = "fail"

print("grade:",grade)

#result
if percentage >= 40:
    print("result: pass")
else:
    print("result:fail")

