info = {
    "key" : "value",
    "name" : "Abhi",
    "sub" : ["python","HTML","CSS"],
    "learning" : "coding",
    "age" : 21,
    "is_adult" : True,
    12 : 23
}

print(type(info))
print(info["key"])
print(info["name"])

# Agar hamko key value add krni h to haam kr sakta h 

info["name"] = "Abhishek kumar"
info["age"] = "23"


# haam aalag se null_dict bi add kr sakta h 

null_dict = {}
null_dict["dob"] = "2004"
print(null_dict)