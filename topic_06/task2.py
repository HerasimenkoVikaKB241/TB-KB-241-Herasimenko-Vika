students = [
    {"name": "Emma", "grade": 9},
    {"name": "Bob",  "grade": 64},
    {"name": "Zak",  "grade": 13},
    {"name": "Jon",  "grade": 45}
]

sorted_by_name = sorted(students, key=lambda x: x["name"])
print("Сортування за ім'ям:")
for s in sorted_by_name:
    print(s)

sorted_by_grade = sorted(students, key=lambda x: x["grade"])
print("\nСортування за оцінкою:")
for s in sorted_by_grade:
    print(s)