arr = [12, 5, 8, 21, 3, 17]

# Task: এই array-এর মধ্যে সবচেয়ে বড় সংখ্যাটি বের করো।

largest = arr[0]

for i in arr:
    if i>largest:
        largest = i

print(largest)


arr2 = [12, 5, 8, 21, 3, 17]

# এই array-এর সবচেয়ে ছোট সংখ্যাটি বের করো।

lowest = arr2[0]

for i in arr2:
    if i<lowest:
        lowest = i

print(lowest)


arr3 = [10, 20, 5, 15, 30]

# এই array-এর সবগুলো সংখ্যার যোগফল বের করো।

total = 0

for i in arr3:
    total = total + i

print(total)

arr4 = [12, 5, 8, 21, 3, 17, 10, 6]

# এই array-তে কয়টি even number আছে সেটা বের করো।

count = 0
for i in arr4:
    if i%2==0:
        count  = count + 1

print(count)


arr5 = [10, 25, 7, 18, 30, 42]
target = 42

# Task: target array-এর মধ্যে আছে কিনা খুঁজে বের করো। 
# output: found or not found 

found = False

for i in arr5:

    if i == target:
        found = True

if found == True:
    print("Found")

else:
    print("Not Found")


arr6 = [10, 20, 30, 40, 50]

# output [50, 40, 30, 20, 10]

rev = []

for i in arr6:
    rev.insert(0,i)

print(rev)


arr7 = [10, 25, 7, 18, 30, 42, 15]
# Task: Array-এর second largest number বের করো।

largest = arr7[0]
second_largest = arr7[0]

for i in arr7:
    # if largest>second_largest and second_largest<i:
    #         second_largest = i

    if i>largest:
        second_largest = largest
        largest = i

print(second_largest)


arr8 = [2, 5, 8, 12, 15, 100]
# Check if Array is Sorted
is_sorted = True

for i in range(len(arr8)-1):
    if arr8[i]>arr8[i+1]:
        is_sorted = False

print(is_sorted)

arr9 = [2, 5, 2, 8, 2, 10, 5, 2]
target = 2

# Task: target কতবার array-তে আছে সেটা বের করো।

count = 0
for i in arr9:
    if i == target:
        count = count+1

print(count)

arr10 = [15, 8, 23, 42, 7, 19]
target = 42
index = None
# Task: target কোন index-এ আছে সেটা বের করো।

for i in range(len(arr10)):
    if arr10[i] ==target:
        index = i
        break

print(index)

arr11 = [10, 20, 30, 40, 50, 60]

# Task: Array-এর প্রতিটি element-এর সাথে তার index print করো।

for i in range(len(arr11)):
    print("index ",i,":",arr11[i])


arr12 = [-5, 10, -2, 8, 0, -7, 15, 3]

# Task: Array-তে কয়টি positive number আছে সেটা বের করো।
positive_counter = 0
for i in arr12:
    if i>=0:
        positive_counter = positive_counter + 1

print(positive_counter)


arr13 = [-5, 10, -2, 8, 0, -7, 15, 3]

# Task: Array-এর মধ্যে সবচেয়ে ছোট positive number বের করো।

positive_num = [x for x in arr13 if x>0]

small_number = positive_num[0]

for i in positive_num:
    if i<small_number:
        small_number = i
print(small_number)

arr14 = [10, 20, 30, 40, 50]
# Task: Array-এর সবচেয়ে বড় এবং সবচেয়ে ছোট সংখ্যার মধ্যে difference বের করো।
longest_num = arr14[0]
smallest_num = arr14[0]
for i in arr14:
    if i>longest_num:
        longest_num = i
    if i<smallest_num:
        smallest_num=i
difference = longest_num - smallest_num
print(difference)
