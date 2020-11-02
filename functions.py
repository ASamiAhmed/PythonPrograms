def func(name = "sir"):
    return f'hello {name}'

name=input("enter name: ")
returned_value = func(name)
print(returned_value)

print(func())

