from collections import namedtuple,Counter,defaultdict,OrderedDict,deque,ChainMap
a = namedtuple("point",["b","c"])
ab = a(10,50)
print(ab.b)

#counter
name = "ajith"
ans = Counter(name)
print(ans)

#defaultdict
name = defaultdict(int)
name["kumar"] += 2
print(name)

#OrderedDict
a = OrderedDict()
a["Name"] = "kumar"
a["age"] = 25
print(a)

#deque
ks = deque([45,45,456])
ks.appendleft(54456)
ks.append(4)
print(ks)

#chainmap

r = {"a":1,"b":2}
d = {"b":3,"g":4}
rcb = ChainMap(r,d)
print(rcb["a"])
