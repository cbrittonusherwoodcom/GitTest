eugene = 'master'
cole = 'not master'

people = [cole, eugene]

for person in people:
    if person == 'master':
        print("Hello, Master!")
    elif person == 'not master':
        print("Hello, Loser!")
    else:
        print("Hello, Stranger!")

print('goober')