# 145list = [145, 12, 12, "World", True, [12, 33]]
# print(list)
#
# numbers = [1, 55, 46, 46, 4645, 487]
# print("Первоначальное значение списка", numbers)
# numbers[0] = 222
# print("Новое содежание списка", numbers)
# print(len(numbers))
# del numbers[2]
# print(numbers[-1])
# list.append(5)
# print(list)
# list.insert(2,444)
#
# mylist = []
# for i in range(5):
#     mylist.append(i+1)
# print(mylist)
#
# mylist = []
# for i in range(5):
#     mylist.insert(0,i+1)
# print(mylist)

# list = [1,2,4,56]
# summa = 0
# for i in range(len(list)):
#     summa += list[i]
# print(summa)

# list = [1,2,4,56]
# print(list)
# list[0], list[4] = list[4],list[0]
# print(list)

# list = [1,2,4,56]
# summa = 0
# for i in range(-1,-4):
#     summa += list[i]
# print(summa)
# #
# list = [1,2,4,56]
# summa = 0
# for i in list:
#     summa += i
# print(summa)

list= input("Введите предложение: ")
new_list = list.split()
my_list = []
for i in range(len(new_list)):
    my_list.insert(0,i)
print(my_list)

