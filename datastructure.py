#lists are written with square brackets
#list can have any datatype in it
mylist= [1,2,3,4,2.3,'hello', [2, ['hi',4, 5], 6]] #sublist list inside another list
mylist2= [0,'world']
#accessing elements of list
mylist[0]
'''print(mylist[1:8])
print(mylist[6][1][1])
print(mylist[5][3:5]) #getting individual value of a string

#change the element of the list

mylist[0]=45
mylist[1:3]=[90, [4,5]] #changing multiple values in a list at once
mylist[1:4]=[0, 1] #replaces all index in between with single value 0
print(mylist)

#removing list items
mylist.remove([2, ['hi', 4, 5], 6])
mylist.pop()
mylist[0]=2
mylist.append(True)
print(mylist)
del mylist
i=7
while i>5:
    print(i)
    i=i-1
'''
##TUPLES
'''1.tuples are used to store multiple items in a single variable
    2. Items are unchangeable/immutable and allows duplicate values
    '''
'''mytuple=(2, 3.4, 'tuplr', True, [2,3], ('hi', 6.7))
print(mytuple[0:4])

#mytuple.append(3) does not have any function called append, as it cannot be changed
print(mytuple)

#adding an element in tuples
#by type conversions
mylist3= list(mytuple)
mylist3.append(70)
mytuple=tuple(mylist3)
print(mytuple)

mylist4= [2, 2, 3.4, 'tuple', True, [2,3], ('hi', 7.5)]
#mylist4[6][1]=50 shows error as tuple inside a list is also immutable
#strings are also immutable
print(mylist4)
'''
#SET
''' Sets are immutable, and doesn't allow duplicate values
    can be written with curly brackets'''
#myset= {2, 2, 3.4, 'tuple', True, [2,3], ('hi', 7.5)} will not allow list inside sets
myset= {2, 2, 3.4, 'tuple', True, ('hi', 7.5)} #prints only 1 of the 2's
#convert a tuple into a set to remove all duplicate values
print(myset)