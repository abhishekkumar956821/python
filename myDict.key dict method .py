#method mydict.key

student = {
    "name": "Lavish",
    "marks": 88.8,
    "city": "Delhi",
    "age": 21,
    "course": "B.Tech",
    "subjects" : {
        "Python": 95,
        "HTML": 92,
        "CSS": 90
    }

    
}
print(student.keys())
print(type(student.keys()))
print(list(student.keys()))
print(len(student.keys()))