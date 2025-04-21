import random
stationeryitems = ["pen","pencil","books","Notes"]
number = [ 1,2,3,4,5,6,7,8,9]
print(random.random())
print(random.randint(124,4652))
print(random.uniform(5.5,5.4))
print(random.choice(stationeryitems))
print(random.choices(stationeryitems,k=3))
print(random.sample(stationeryitems,4))
random.shuffle(number)
print(number)
