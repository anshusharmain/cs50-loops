#5 part of loops file
'''
students = {
    "Hermione": "Grryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin",
}'''
'''
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
'''
# Now it print all the name from data
'''
for student in students:
    print(student)
'''
# In this code we can see name also and data we put 
'''for student in students: # the student we give name of it but students is data name that we given in up
    print(student, students[student], sep=",")# sep=";" we use because to give space between them 
'''

#Now we see How to add multiple data in table 
students = [
    {"name": "Hermione", "house": "Gryffiindor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffiindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffiindor", "patronus": "Jack"},
    {"name": "Draco", "house": "Slytherin", "patronus": "None"},
]
for student in students:
    print(student["name"], student["house"], sep=",") #now with name it show only name but we add house that house of people and we add value their
