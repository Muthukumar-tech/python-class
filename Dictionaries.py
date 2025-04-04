thedict = {
    "Brand" : "ford",
    "model" : "endeavour",
    "year" : 2024,
    "price" : "28 lakh"
}
print(thedict)
#get
y = thedict["Brand"]
print(y)
#print Keys Values
print(thedict.keys())
#print Values
print(thedict.values())
#print Itemd Values
print(thedict.items())
#change Values
thedict["model"] = "figo"
print(thedict)
#update values
thedict.update({"price":"8 Lakh"})
print(thedict)
#Add
thedict["expiry"] = "20.03.2045"
print(thedict)
#remove
thedict.pop("expiry")
print(thedict)

#loop
for i in thedict.values():
    print(i)
for d in thedict.keys():
    print(d)

for x,y in thedict.items():
    print(x,y)
van = {
    "model" : "20 seter",
    "company" : "SML",
    "year" : 2019,
    "price" : "40 lakh"
}
mydict = van.copy()
print(mydict)
dicymy = dict(thedict)
print(dicymy)
#nested
myfamily = {
    "son 1" : {
        "name" : "Emil",
        "age" : 20,
        "fav Color" : "red"
        },
    "son 2" : {
        "name" : "john",
        "age" : 40,
        "fav Color" : "yellow"
        }
    }
print(myfamily)
print(myfamily["son 1"]["name"])

