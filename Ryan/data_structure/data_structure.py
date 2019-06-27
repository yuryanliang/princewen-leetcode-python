# Array
from collections import defaultdict

b = [1, 2, 3]
a = [0] * 5
a_2d = [[0] * 5 for _ in range(10)]
a_3d = [[[0] * 5 for _ in range(10)] for _ in range(15)]
1 == 1

# Dynamic Array
a = []
a.append(1)
a.append(3)
a.append(4)

del a[-1]
x = a[:-1]  # make a copy
y = a[0]

# HashTable
a = dict()
a["key1"] = 3
a["key2"] = 8
if "key1" in a:
    print("key 1 in a")

for key in a:
    value = a[key]
    print("value:", value)

for k, v in a.items():
    print("k: ", k, ", v: ", v)

# Priority queue / Min heap
import heapq

q = [2, 1, 4, 5]
heapq.heapify(q)
heapq.heappush(q, 10)
x = q[0]
y = heapq.heappop(q)

#Set/ String/ Order
a=[2, 1, 2, 3]
b=set(a)

a=set([1,2,3])
b=list(a) #set to list

x=12345
s=str(x)

s="12345"
x=int(s)

c='9'
x=ord(c)-ord('0')
x=int(c)

s=''.join(['1']*5)
l=list(s)
l[1]='h'
s=''.join(l)
s=s[0:1]+'h'+s[2:]

s+=" hello"

1==1

# defaultdict
dict_lambda=defaultdict(lambda:12)
print(dict_lambda["soso"]) # result is 12

dict_list=defaultdict(list)
print(dict_list["d"]) # result is []

