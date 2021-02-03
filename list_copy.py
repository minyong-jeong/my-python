import copy

list = [[1, 2], 1, 2, 3]
assignment = list
shallow_copy = copy.copy(list)
deep_copy = copy.deepcopy(list)

print(f"Initial List  => {list}\n")         # [[1, 2], 1, 2, 3]

list.append(4)
print("Append 4 to list.")
print(f"assignment    => {assignment}")     # [[1, 2], 1, 2, 3, 4]
print(f"shallow copy  => {shallow_copy}")   # [[1, 2], 1, 2, 3]
print(f"deep copy     => {deep_copy}\n")    # [[1, 2], 1, 2, 3]

list[0].append(3)
print("Append 3 to list[0].")
print(f"assignment    => {assignment}")     # [[1, 2, 3], 1, 2, 3, 4]
print(f"shallow copy  => {shallow_copy}")   # [[1, 2, 3], 1, 2, 3]
print(f"deep copy     => {deep_copy}")      # [[1, 2], 1, 2, 3]
