people = [
    {"name": "John", "location": "Broad street"},
    {"name": "Mary", "location": "Freeport"},
    {"name": "Anthony", "location": "Sinkor"}
]

# def sort_people(person):
#         return person['location']

people.sort(key= lambda person: person['name'])
print(people)