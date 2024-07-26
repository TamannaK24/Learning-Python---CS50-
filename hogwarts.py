students = ["Hermione","Harry","Ron"]
print(students[0])

# can't use _ because you're using the variable 
for student in students:
    print(student)

for i in range(len(students)):
    print(i + 1, students[i])

for i in [0, 1, 2]:
    print("meow")


# dict which is dictionary data type
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron":"Gryffindor",
    "Draco":"Slytherin"
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

for student in students:
    print(student, students[student])

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], sep=", ")










