# Python3 code to demonstrate
# converting list of strings to int
# using naive method

# initializing list
test_list = ['1', '4', '3', '6', '7']

# Printing original list
print("Original list is : " + str(test_list))

# using naive method to
# perform conversion
for i in range(0, len(test_list)):
    test_list[i] = int(test_list[i])

# Printing modified list
print("Modified list is : " + str(test_list))
for i in test_list:
    print(test_list[i])