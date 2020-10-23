# 10th Meeting, learn about Dictionary and Tupple
thisdict = {
   "brand": "Ford",
    "model": "Mustang",
    "year" : 1980
}
thisdict["year"] = 2018
print(thisdict)


# Try to create Dictionay on list
phone = [{
        "name": "Luke Skywalker",
        "role": "Jedi",
        "email": "luke@gmail.com",
        },
        {
        "name": "Padme Amidala",
        "role": "Princesses",
        "email": "pade@gmail.com",
        },
        {
        "name": "Han Solo",
        "role": "Pilot",
        "email": "solo@gmail.com",
        }
    ]

     
phone = {"John Doe": 2199898989, "Max Speed": 78878787}

for i, v in phone.items():
    print(f"Name: {i}, phone: {v}")


# Learn about Tupple

tp = ("Draft","Progress","Done")
print(tp)

ls = list(tp)
