list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = []

for x in list1:
    if x in list2:
        common.append(x)

print(common)
