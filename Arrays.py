from array import array
a = array('d', [1.1, 3.5, 4.5])
print(a)
print(type(a))
for x in a:
    print(x)

print("**************************")


numbered_list=[2,4,5,3,44,55,322,44,43]
numbered_array=array('i',numbered_list)
i=0
for x in numbered_array:
    print("value of numbered_array[",i,"]:",x)
    i=i+1
print("*************************")

print(numbered_array[0:5])

numbered_array.append(897)

print(numbered_array[5:10])


odd=array('i',[1,3,5])
even=array('i',[2,4,6])

numbers=array('i')
numbers=odd+even

print("numbers:",numbers)

del numbers[5]
numbers.append(33)
print("numbers:",numbers)
