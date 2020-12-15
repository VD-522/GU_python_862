print('Hello World, this is my first home task!')

print('Задание 1')
a = 50
b = 'метров'

print(str(a) + ' ' + b)

c = float
c = a / 3

print(c)

d = [a, 'List', 'Список']

print(d)
print(d[1])

e = (a, b, c, 'Tuple', 'Кортеж')

print(e)
print(e[3])

f = {a: b,
     c: ['Dict', 'Словарь']
}

print(f)
print(f[c])

g = input("Введите что-нибудь:\n")
print('Вы ввели ' + g)

def check_input1():
    h = input("Введите число:\n")
    try:
        h == int(h)
        print('Вы ввели ' + h)
    except ValueError:
        print(f'Вы ввели {h}, а это не число!')
        return check_input1()


check_input1()




print('Задание 2')
time_sec = ''
def check_input2():
    time_sec = input('Введите время в секундах: ')
    try:
        time_sec = int(time_sec)
        hh = time_sec // 3600
        if hh < 10:
            hh = '0' + str(hh)
        else:
            hh = str(hh)

        mm = (time_sec - int(hh) * 3600) // 60
        if mm < 10:
            mm = '0' + str(mm)
        else:
            mm = str(mm)

        ss = time_sec - int(hh) * 3600 - int(mm) * 60
        if ss < 10:
            ss = '0' + str(ss)
        else:
            ss = str(ss)

        print(f'Вы ввели: {hh}:{mm}:{ss} в секундах.')
    except ValueError:
        print(f'Вы ввели {time_sec}, а это не число!')
        return check_input2()


check_input2()




print('Задание 3')
def check_input3():
    sum_num = ''
    sum_num = input("Введите целое число:\n")
    try:
        sum_num = int(sum_num)
        print(f'Вы ввели: {sum_num}')
        sn = int(sum_num)
        snn = int(sum_num + sum_num)
        snnn = int(sum_num + sum_num + sum_num)
        magic_sum = sn + snn + snnn
        print(
            f'Если к {sum_num} прибавить {sum_num}{sum_num} и прибавить {sum_num}{sum_num}{sum_num}, будет: {magic_sum}')
    except ValueError:
        print(f'Вы ввели {sum_num}, а это не целое число!')
        return check_input3()


check_input3()



print('Задание 4')
def check_input4():
    int_positive = ''
    int_positive = input("Введите целое положительное число:\n")
    try:
        int_positive == int(int_positive)
        if int(int_positive) > 0:
            if int(int_positive) < 10:
                print(int_positive)
            else:
                int_positive = int(int_positive)
                max_figure = int_positive % 10
                int_positive = int_positive // 10
                while int_positive > 0:
                    if int_positive % 10 > max_figure:
                        max_figure = int_positive % 10
                    int_positive = int_positive // 10
                print(max_figure)
        else:
            print('Число, которое Вы ввели не положительное!')
            return check_input4()
    except ValueError:
        print(f'Вы ввели {int_positive}, это не число или оно не положительное!')
        return check_input4()


check_input4()




print('Задание 5')
def check_input5():
    revenue = ''
    costs = ''
    employees = ''
    revenue = input("Введите значение выручки:\n")
    costs = input("Введите значение издержек:\n")
    try:
        revenue == int(revenue)
        costs == int(costs)
        if int(costs) < 0:
            print('Что-то неправильно, попробуйте заново')
            return check_input5()
        else:
            balance = int(revenue) - int(costs)
            try:
                profitability = int(revenue) / int(costs) * 100
                if balance >= 0:
                    print(f'Рентабельность выручки равна {str(profitability)} процентов')
                else:
                    print(f'Фирма сработала в убыток ({-balance} у.е.)')
            except ZeroDivisionError:
                print('Фирм без издержек не бывает, повторите ввод')
                return check_input5()
    except ValueError:
        print(f'Вы ввели не число!')
        return check_input5()

    def employees_pr():
        try:
            employees = input("Введите число сотрудников:\n")
            employees == int(employees)
            if int(employees) > 0:
                profit_per_empl = balance / int(employees)
                if balance >= 0:
                    print(f'Прибыль на сотрудника составила {str(profit_per_empl)} у.е.')
                else:
                    print(f'Убытки в пересчёте на каждого сотрудника составили {str(-profit_per_empl)} у.е.')
            else:
                print('Некорректное число сотрудников')
                return employees_pr()
        except ValueError:
            print(f'Вы ввели не число!')
            return employees_pr()
    employees_pr()


check_input5()




print('Задание 6')
def check_input6():
    a = input("Введите дистанцию спортсмена в первый день:\n")
    b = input("Введите искомую дистанцию, которую должен пробежать спортсмен:\n")
    try:
        a == int(a)
        b == int(b)
        a = int(a)
        b = int(b)
        if a > 0 and b > a:
            day = 1
            distance = a
            while distance <= b:
                distance += distance * 1.1
                day += 1
            print(day)
        else:
            print('Введённые значения противоречат здравому смыслу, пожалуйста, повторите')
            return check_input6()
    except ValueError:
        print(f'Вы ввели не число!')
        return check_input6()


check_input6()

# task updated, please, review
