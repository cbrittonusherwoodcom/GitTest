eugene = 'master'
cole = 'not master'

people = [cole, eugene]

for person in people:
    if person == 'master':
        print("Hello, Master!")
    else:
        print("Hello, Guest!")
