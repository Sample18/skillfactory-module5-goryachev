# печатаем поле в консоль
a = "  0 1 2\n0 - - -\n1 - - -\n2 - - -"
win_a = list(a)
i = 0
print(a)
while i < 9:
    i = i + 1
# Вводим номер поля для помещения туда нового значения
    b = input('Введите номер поля по оси Y и X в виде "YX":')
    if b == "00":
        c = input('Введите Х или 0:')
        a = a[:10] + c.lower() + a[11:]
        win_a = list(a)
        print(a)
    elif b == "10":
        c = input('Введите Х или 0:')
        a = a[:12] + c.lower() + a[13:]
        win_a = list(a)
        print(a)
    elif b == "20":
        c = input('Введите Х или 0:')
        a = a[:14] + c.lower() + a[15:]
        win_a = list(a)
        print(a)
    elif b == "01":
        c = input('Введите Х или 0:')
        a = a[:18] + c.lower() + a[19:]
        win_a = list(a)
        print(a)
    elif b == "11":
        c = input('Введите Х или 0:')
        a = a[:20] + c.lower() + a[21:]
        win_a = list(a)
        print(a)
    elif b == "21":
        c = input('Введите Х или 0:')
        a = a[:22] + c.lower() + a[23:]
        win_a = list(a)
        print(a)
    elif b == "02":
        c = input('Введите Х или 0:')
        a = a[:26] + c.lower() + a[27:]
        win_a = list(a)
        print(a)
    elif b == "12":
        c = input('Введите Х или 0:')
        a = a[:28] + c.lower() + a[29:]
        win_a = list(a)
        print(a)
    elif b == "22":
        c = input('Введите Х или 0:')
        a = a[:30] + c.lower() + a[31:]
        win_a = list(a)
        print(a)
    else:
        print('Вы ввели неверный номер поля!')
# Проверка победы по горизонтали
    if win_a[10:15:2] == ['x', 'x', 'x']:
        print('Крестики победили!!!')
        break
    elif win_a[18:23:2] == ['x', 'x', 'x']:
        print('Крестики победили!!!')
        break
    elif win_a[26::2] == ['x', 'x', 'x']:
        print('Крестики победили!!!')
        break
    elif win_a[10:15:2] == ['0', '0', '0']:
        print('Нолики победили!!!')
        break
    elif win_a[18:23:2] == ['0', '0', '0']:
        print('Нолики победили!!!')
        break
    elif win_a[26::2] == ['0', '0', '0']:
        print('Нолики победили!!!')
        break
# Проверка победы по вертикали
    elif win_a[10:27:8] == ['x', 'x', 'x']:
        print('Крестики победили!!!')
        break
    elif win_a[12:29:8] == ['x', 'x', 'x']:
        print('Крестики победили!!!')
        break
    elif win_a[14::8] == ['x', 'x', 'x']:
        print('Крестики победили!!!')
        break
    elif win_a[10:27:8] == ['0', '0', '0']:
        print('Нолики победили!!!')
        break
    elif win_a[12:29:8] == ['0', '0', '0']:
        print('Нолики победили!!!')
        break
    elif win_a[14::8] == ['0', '0', '0']:
        print('Нолики победили!!!')
        break
# Проверка победы на искосок с лева на право
    elif win_a[10::10] == ['x', 'x', 'x']:
        print('Крестики победили!!!')
        break
    elif win_a[10::10] == ['0', '0', '0']:
        print('Нолики победили!!!')
        break
# Проверка победы на искосок с права на лево
    elif win_a[14:27:6] == ['x', 'x', 'x']:
        print('Крестики победили!!!')
        break
    elif win_a[14:27:6] == ['0', '0', '0']:
        print('Нолики победили!!!')
        break
