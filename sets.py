variables = {'a','b','c','d','c'}
print(variables)  # remove the repeated variables
variables.add('z')
print(variables)  # to add a new letter
b = frozenset('asdsafadgwas')
print(b)   # frozenset conversion
print({1,2,3,4} & {3,4,5,6})  # & is sign of intersection
print({1,2,3} | {2,3,4})      # | is sign of union
print({1,2,3} - {2,3,4})      # - is sign of difference
print({1,2,3,4} ^ {2,3,5})    # ^ is sign of symmetric difference
print({1,2} >= {1,2,3})       # >= is sign of superset check
print({1,2} <= {1,2,3})       # >= is sign of subset check
print( 2 in {1,2,3})          # in is for existance check
print(4 in {1,2,3})           # in is for existance check
s = {1,2,3}
s.add(4)                      # add function is to add something
print(s)
s.discard(2)                  # to remove/delete
print(s)
s.remove(1)                  # to remove/delete
print(s)
s.update({1,2})              # to update set
print(s)
print(len(s))