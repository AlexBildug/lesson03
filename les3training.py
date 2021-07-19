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
