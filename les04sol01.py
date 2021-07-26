

my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
for element in my_list:
    if element < 5:
        new_list.append(element)
print(new_list)