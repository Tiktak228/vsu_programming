from collections import deque
name = {
    "Akakii": ["Lyda", "Sasha"],
    "Lyda": ["Sveta", "Daniil"],
    "Sasha": ["Katia", "Dima", "Vlad"]
}
def doter(x):
    return not len(x) % 2 and x[0] == "D"

a = deque(name["Akakii"])
b = []
while name:
    person = a.popleft()
    if person not in b:
        if doter(person):
            print(person)
            break
        else:
            a += name.get(person, [])
        b.append(person)
