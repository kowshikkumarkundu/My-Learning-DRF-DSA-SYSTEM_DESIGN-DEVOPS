from array import *

value = array('i',[1,2,3,3,4,5]) # i = type of the array i stand for integar

# we can iterate every iteam by for loop

for i in range(0,len(value)):
    print(value[i], end=" ")

print("\n")
# another way of iterate

for i in value:
    print(i,end=",")

print("\n")
# if we want to store decimal
decimal = array("d",[2.3,5,.6])

for i in decimal:
    print(i,end=",")

print("\n")
# if we want to store string
# string = array("u",["ko","ku"])

# for i in string:
#     print(i,end=",")

# we can know the array typecode
print(decimal.typecode)


# if we want to  reverse our array
value.reverse()

for i in value:
    print(i,end=',')

print("\n")

# we can insert any item in our array by insert function

value.insert(0,100) #variable_name.insert(index_num,value)

for i in value:
    print(i,end=',')

print("\n")
# we can add item at the end by append function

value.append(500)

for i in value:
    print(i,end=',')

print("\n")

# we can update value also

# value[index_number] = value
value[1] = 101

for i in value:
    print(i,end=',')

print("\n")

# we can copy array

copyArray = array(value.typecode,(i for i in value))
print("copy of value array \n")
for i in copyArray:
    print(i,end=',')

print("\n")

# we can pop any item of a array
print("------------ pop item from copyArray ---------")
copyArray.pop() #  --> this will delete the last item
copyArray.pop(1) # --> this will delete the 1 index value
for i in copyArray:
    print(i,end=',')

print("\n")

#we can remove by giving value using remove
print("------------ remove item from copyArray by value---------")
copyArray.remove(3)
for i in copyArray:
    print(i,end=',')

print("\n")

#------------------slicing-----------
# new_variable = slicing_variable[start_index : end_index]
print("Slicing copyArray")
slice_array = copyArray[2:5]

for i in slice_array:
    print(i,end=',')

print("\n")

print("reverse array by slicing")
rev_by_slice = copyArray[::-1]
for i in rev_by_slice:
    print(i,end=',')

print("\n")

# we can find out index number by giving value
print(value,'\n')
print("know index by giving value")

indexing = value.index(1)

print(indexing)
