# # x= lambda a:a*2
# # print(x(3))
# alist = ["my","name","is","sami"]
# new_list = list(map((lambda a:a.upper()),alist))
# print(new_list)

# x= lambda a:a*2
# # print(x(3))
# alist = [1,2,3,4,5,6]
# new_list = list(filter((lambda a:a%2==0),alist))
# print(new_list)

from functools import reduce 
alist = [1,2,3,4,5,6]
new_list = reduce((lambda a,b:a*b),alist)
print(new_list)