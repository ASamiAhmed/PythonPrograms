a=[1,2,3]
b=a
a[0]=6
print(b)

a=[1,2,3]
b=a.copy()
a[0]=6
print(b)

a=[1,2,3]
b=a[:]
a[0]=6
print(b)

a=[1,2,3]
b=list(a)
a[0]=6
print(b)

import copy
a=[1,2,3]
b=copy.copy(a)
a[0]=6
print(b)