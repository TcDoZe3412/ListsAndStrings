marks = {}

n = int(input("Enter number of subjects: "))

for i in range(n):
    subject = input("Enter subject name: ")
    mark = int(input("Enter marks: "))
    marks[subject] = mark

print("\n--- Subject Marks Report ---")

total = 0

for subject, mark in marks.items():
    print(subject, ":", mark)
    total += mark

print("Total Marks:", total)
print("Average Marks:", total / n)