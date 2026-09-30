# একটি integer n এবং একটি digit d দেওয়া থাকবে। n-এর মধ্যে d কতবার আছে সেটা recursion দিয়ে বের করো।

# Input: 5825252
# d = 2

# Output: 4

# Input: 11123411
# d = 1

# Output: 5

# Base case = ?
# Smaller problem = ?
# Current answer = ?

def countDigit(input,digit):

    if input == 0:
        return 0
    
    if input%10 == digit:
        return 1 + countDigit(input//10,digit)
    else:
        return countDigit(input//10,digit)
    

print(countDigit(11123411,1))