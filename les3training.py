my_list = [1, 2.2, "python", "dzczsd"]
print("my list")
print (my_list)

my_dict = {"key-01": "test", 2: -47.38, 425.2: 17, "key-02": 127}
print("My dict")
print(my_dict)

#my_list[index] - #доступ к элементу списка по индексу
print(my_list[0])

#my_list[-index] - #доступ к элементу списка по индексу начиная с конца
print(my_list[-4])

#my_list[start:end]  #доступ срез списка
print(my_list[2:4])

#len(my_list) - #получить длину списка
print (len(my_list))
#my_list.append(element) # добавить новый элемент в список
my_list.append(2.7)
print(my_list)
#my_dict[key] #доступ к элементу словаря по ключу
print(my_dict)
print(my_dict["key-01"])
print(my_dict[425.2])
print(my_dict["key-02"])

#my_dict[key] = value # добавить новый или изменить существующий элемент словаря
my_dict[2] =3
print(my_dict)
my_dict["new"] =7
print(my_dict)
my_dict[3.14] ="pi"
print(my_dict)

#len(my_dict)  # получить количество элементов словаря
print(len(my_dict))
#my_dict.keys() / my_dict.values() # получить список ключей / значений словаря
print(my_dict.keys())
print(my_dict.values())

list('hello')

set([1,2,2,3,3,4,5,5,5,5,6])

#Генератор списка - это выражение вида:
vlans = [f'vlan {num}' for num in range(10,20)]
print(vlans)
#https://pyneng.readthedocs.io/ru/latest/book/08_python_basic_examples/x_comprehensions.html


#В общем случае, это выражение, которое преобразует итерируемый объект в список.
# То есть, последовательность элементов преобразуется и добавляется в новый список.

#Выражению выше аналогичен такой цикл:
vlans = []
for num in range(7,11):
    vlans.append(f'vlan {num}')
print(vlans)

#В list comprehensions можно использовать выражение if. Таким образом можно добавлять в список только некоторые объекты.
#Например, такой цикл отбирает те элементы, которые являются числами, конвертирует их и добавляет в итоговый
# список only_digits:

items = ['10', '20', 'a', '30', 'b', '40', 'list_text']
print(items)
only_digits = []
for item in items:
      if item.isdigit():
            only_digits.append(int(item))
print(only_digits)

#x = 17 / 2 * 3 + 2
x=17/2*3+2
print(x)

#x = 2 + 17 / 2 * 3
x=2+(17/2*3)
print(x)

#x = 19 % 4 + 15 / 2 * 3
x=19%4+15/2*3
print(x)

#x = (15 + 6) - 10 * 4
x=(15+6)-10*4
print

#my_list=[1,2,3]
#str(my_list)
#print(my_list)

#Создать список состоящий из отдельных единичных символов, преобразовать список в строку,
# инвертировать строку и вывести на печать.
#[1,2,3][::-1]
my_list=[1,2,3]
""join(map(str, my_list[::-1]))
print(my_list)









