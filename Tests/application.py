eugene = 'cyber security analyst II'
cole = 'not cyber security analyst II'
joe = 'unc'
# this is because Joe is old

people = [cole, eugene]

for person in people:
    if person == 'cyber security analyst II':
        print("Hello, Eugene!")
    elif person == 'not cyber security analyst II':
        print("Hello, Loser!")
    else:
        print("Hello, old dude :/")

