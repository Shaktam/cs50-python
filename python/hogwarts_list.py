# list and len()
students=["Ron","Tonny", "Harry"]
print(students[0])
print(students[1])
print(students[2])

# or
for student in students:
    print(student)

for i in range(len(students)):
    print(i+1, students[i])

# dict

students={"Ron" : "Gryffindor",
           "Tonny": "Gryffindor",
           "Harry" :"Gryffindor",
           "Syri": "slytherin"
        }

print(students["Ron"])
print(students["Tonny"])
print(students["Harry"])
print(students["Syri"])

for student in students:
    print(student, students[student], sep=",")

#if we have multiple information for same key
    
students=[{"name":"Ron","house": "Gryffindor", "patronus":"Ottr"},
           {"name":"Tonny","house": "Gryffindor", "patronus":"Stag"},
          { "name":"Harry" ,"house":"Gryffindor", "patronus":"Jack russell terrier"},
           {"name":"Syri","house": "slytherin", "patronus":None}
        ]
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")