import time
from binary_search_tree import BinarySearchTree
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# runtime before = 26.53
# Polynomial O(n^c)



# runtime after = .39
# log(n)

bst = BinarySearchTree('names')

for name in names_1:
    bst.insert(name)

for name in names_2:
    if bst.contains(name):
        duplicates.append(name)


# stretch solution
# # define a dictionary 
# names_2_dict = {}

# # Confirm names are in the list
# for name in names_2:
#     names_2_dict[name] = True

# # Confirm name is in the list
# # and if it is in the name 2 dict
# # if so, append
# for name in names_1:
#     if name in names_2_dict:
#         duplicates.append(name)

# # runtime after = 0.018
# # Linear O(n)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
