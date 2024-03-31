people = [
    {"name": "John", "location": "Broad street"},
    {"name": "Mary", "location": "Freeport"},
    {"name": "Anthony", "location": "Sinkor"}
]

def sort_people(person):
        return person['name']
people.sort(key=sort_people)
print(people)