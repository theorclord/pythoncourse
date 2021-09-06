contacts = {
    "number" : 4,
    "students" :
    [
        {"name":"Name","email":"my@email.com"},
        {"name":"Name1","email":"my2@email.com"},
        {"name":"Name2","email":"my3@email.com"},
        {"name":"Name3","email":"my1@email.com"},
    ]
}

for student in contacts["students"]:
    print(student["email"])