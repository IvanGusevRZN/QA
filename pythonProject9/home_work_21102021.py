
runing = True
while runing != "0":

    exercise = int(input("Выберите номер задания от 1 до 7 включительно: "))

    if exercise == 1:
        # Задание 1
        def speech_BillGates():
            return "“Don't compare yourself with anyone in this world…" \
                   "\nif you do so, you are insulting yourself.”" \
                   "\n\t\t\t\t\t\t\t\t\t\tBill Gates"


        print(speech_BillGates())


    if exercise == 2:
        # Задание 2
        def num_range(a, b):
            list_even = []
            for i in range(a, b + 1):
                if i % 2 == 0:
                    list_even.append(i)
            return list_even


        print("Введите диапазон целых четных чисел, "
              "\nв ответ программа выведет список четных чисел из введенного диапазона")
        start = int(input("Введите начало диапазона: "))
        stop = int(input("Введите конец диапазона: "))
        print(num_range(start, stop))


    if exercise == 3:
        print("Данное приложение в разработке, выберите из оставшихся номеров 1,2,4,5,6,7)")
        # Задание 3 оставил так как оно работает, еще в разработке
        # def figure(side_length, simbol, boolean):
        #     if boolean == 1:
        #         for i in range(side_length):
        #             print()
        #             for j in range(side_length):
        #                 print(simbol, end='  ')
        #     elif boolean == 0 and side_length % 2 != 0 and side_length % 3 != 0: # для ровного отображения размера кратного пяти
        #         for i in range(side_length):
        #             print(simbol, end='  ')
        #         print()
        #         for i in range(side_length - 2):
        #             print(simbol, ' ' * (side_length - 2), simbol, sep='    ')
        #         for i in range(side_length):
        #             print(simbol, end='  ')
        #         print()
        #     elif boolean == 0:
        #         for i in range(side_length):
        #             print(simbol, end='  ')
        #         print()
        #         for i in range(side_length - 2):
        #             print(simbol, ' ' * (side_length - 2), simbol, sep='   ')
        #         for i in range(side_length):
        #             print(simbol, end='  ')
        #         print()
        #
        # print("Прилжение отображает квадрат и принимает в качестве параметров:"
        #       "\nдлину стороны квадрата, символ и "
        #       "\nпеременную логического типа 0(квадрат пуст) или 1(квадрат заполнен) ")
        # x = int(input("Введите размер квадрата: "))
        # simbol = input("Введите символ для создания квадрата: ")
        # boolian = int(input("Введите 0(квадрат пуст) или 1(квадрат заполнен)"))
        # figure(x, '8', boolian)



    if exercise == 4:
        # Задание 4
        def my_minimum(my_list):
            min = float("inf")
            for i in my_list:
                if i < min:
                    min = i
            return min

        print('Приложение возвращает минимальное значение из пяти введеных вами чисел')
        list_num = []
        for i in range(5):
            list_num.append(int(input("Введите целое число и нажмите Enter: ")))
        print(list_num)
        print('Минимальное число из введенных является ', my_minimum(list_num))


    if exercise == 5:
        # Задание 5
        def multiplication_range(a, b):

            if a > b:
                multiplication = b
                for i in range( b +1, a + 1):
                    multiplication *= i

            if a < b:
                multiplication = a
                for i in range(a + 1, b+ 1):
                    multiplication *= i

            return multiplication


        print("Приложение для подсчета произведения целых чисел в указанном дипазоне,"
              "\nпрограмма сама определяет наименьшеее значения из введенных чисел,"
              "\nдля начала вычисления диапазона")
        a = int(input("Введите первое число диапазона: "))
        b = int(input("Введите второе число диапозона: "))
        print("Произведение =", multiplication_range(a, b))

    if exercise == 6:
        # Задание 6
        def count_num(a):
            str_num = str(a)
            if str_num[0] == '-':
                return len(str_num) - 1
            return len(str_num)


        print("Программа для посчета кличества цифр в веденном числе")
        a = input("Введите число целое число, можно отрицательное: ")
        print("Число состоит из", count_num(a), "цифр(ы)")

    if exercise == 7:
        # Задание 7
        def palindrome(a):
            s = str(a)
            if s[::] == s[::-1]:
                return print(a, "Число полиндром")
            return print(a, "Не является полиндромом")


        print("Приложение для определения числа полиндрома")
        palindrome(int(input("Введите шестизначное число полиндром: ")))

    runing = input("\nДля продолжения нажмите Enter, для выхода 0: ")
    if runing == 0:
        runing = False
