stationery =("Books","Notes","pen","Pencil")
print(stationery[0:3])
print(type(stationery))
item = list(stationery)
item[1] = "Eraser"
stationery = tuple(item)
print(stationery)
add = ("noate",)
stationery += add
print(stationery)


