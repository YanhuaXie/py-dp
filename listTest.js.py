

# common list functions
list1 = [1, 2, 3, 4, 'Yanhua']
print(list1)

list1.append('Xie')
print(list1)

list1.pop()
print(list1)

list1.insert(1, 'Xie')
print(list1)

list1.remove('Xie')
print(list1)

# list1.reverse()

# list1.sort()

list2 = [2] * 10 + list1
print(list2)

print(list1[1::2])

# copy a list without changing the original one - three ways
list3 = list1.copy()
list3 = list(list1)
list3 = list1[:]

list1.append('Xie')
print(list1)
print(list3)

# calculate x^n
list4 = [1, 2, 3, 4, 5, 6]
listPow = [i ** 2 for i in list4]
print(listPow)

