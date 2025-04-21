from collections import namedtuple,Counter,defaultdict,OrderedDict,deque,ChainMap

point = namedtuple('point',['x','y'])
pointValue = point(10,20)
print(pointValue.y)

# counter
name = 'sanjai'
value = Counter(name)
print(value)

# defaultdict - A dictionary that provides a default value for missing keys.
dd = defaultdict(int)
dd['apple'] += 5
print(dd)  

# orderedDict - Maintains insertion order
a = OrderedDict()
a["name"] = "aaaa"
a["age"] = 5
print(a)


#deque - A double-ended queue optimized for fast appends and pops from both ends.

dq = deque([45,3,67,1])
dq.appendleft(11)
dq.append(10)
print(dq)

# chainMap - used to group multiple dictionaries

n1 = {"a":1,"b":2}
n2 = {"c":3,"d":4}

cm = ChainMap(n1,n2)

print(cm['d'])
