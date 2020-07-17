list_a = [10, 20 ,30]
list_b = [10, 20, 30]

if list_a is list_b:
    print('list_a is list_b')

else:
    print('list_a is not list_b')

print(id(list_a))
print(id(list_b))