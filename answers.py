# QUESTION 1: Create an empty list called my_list.
my_list = []

# QUESTION 2: Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("After append:", my_list)  

# QUESTION THREE: nsert the value 15 at the second position in the list
my_list.insert(2, 15)

print("After insert:", my_list)  

#QUESTION 4 : Extend my_list with another list: [50, 60, 70].
my_list2 = [50, 60, 70]

my_list.extend(my_list2)

print("After extend:", my_list)

#QUESTION 5: Remove the last element from my_list
del my_list[-1]

print("After deletion:", my_list)

#QUESTION 6: Sort my_list in ascending order.
my_list.sort()

print("Sorted list in ascending order:", my_list)

#QUESTION 7: Find and print the index of the value 30 in my_list.
index_30 = my_list.index(30)

print("Index 30:", index_30)

