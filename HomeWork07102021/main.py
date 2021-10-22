runing = True
while runing != 0:

    hoome_work = input("Выбирите задание для проверкки"
                       "\nцифра 1 - первое задание"
                       "\nцифра 2 - второе задание"
                       "\n")
    if hoome_work == "1":

        expression = input("Приложение для \"+\" сложения, \"-\" вычитания, \"*\" умножения и \"/\" деления."
                           "\nВведите арифметическое выражение (пример 23+12): ")

        if expression.find("+") != -1:                                # метод find при нахождении символа "+" будет равен 0, если не найдет то -1
            expression_list = expression.split("+")                   # методом сплит превращаем строку в список с двумя индексами разделяя через "+"
            print(int(expression_list[0]) + int(expression_list[1]))  # складываем индексы при этом приводим командой
                                                                      # int(expression_list[0]) строковый индекс к числу чтобы выполнить сложение

        if expression.find("-") != -1:
            expression_list = expression.split("-")
            print(int(expression_list[0]) - int(expression_list[1]))

        if expression.find("*") != -1:
            expression_list = expression.split("*")
            print(int(expression_list[0]) * int(expression_list[1]))

        if expression.find("/") != -1:
            expression_list = expression.split("/")
            print(int(expression_list[0]) / int(expression_list[1]))

    if hoome_work == "2":

        import random  # подключаем библиотеу рандом

        print("В списке целых, заполненном случайными числами,"
              "\nопределить минимальный и максимальный элементы, "
              "\nпосчитать количество отрицательных элементов, "
              "\nпосчитать количество положительных элементов, "
              "\nпосчитать количество нулей\n")
        list = []
        for i in range(10):
            list.append(random.randint(-1000, 1000))  # random.randint(-1000, 1000) задает диапазон выборки рандомных чисел
        print("Список целых числел ",list)

        summa_positive = 0
        summa_negative = 0
        summa_zero = 0
        minimum = float('inf')
        maximum = float('-inf')
        for i in list:
            if i < 0:
                summa_negative += 1
            elif i > 0:
                summa_positive += 1
            elif i == 0:
                summa_zero += 1
            if i < minimum:
                minimum = i
            if i > maximum:
                maximum = i

        print("Минимальное значение равно = ", minimum)
        print("Максимальное значение = ", maximum)
        print("Количество отрицательных чисел = ", summa_negative)
        print("Количество положительных чисел = ", summa_positive)
        print("Количество нулей = ", summa_zero)

    runing = int(input("\nДля продолжения нажмите 5, для выхода 0: "))
    if runing == 0:
        runing = False