def promax1():
    global izm
    print(round(abs(izm[0] - izm[1]), l), " < ", round(0.64 * R, l))
    print(round(abs(izm[-1] - izm[-2]), l), " < ", round(0.64 * R, l))
    if not (round(abs(izm[0] - izm[1]), l) < round(0.64 * R, l)):
        print("Промахи есть, -1 значение!")
        izm.pop(0)
        return False
    elif not round(abs(izm[-1] - izm[-2]), l) < round(0.64 * R, l):
        print("Промахи есть, - последнее значение!")
        izm.pop(-1)
        return False
    print("Промахов нет!")
    return True


def promax2():
    if (round(abs(izm[-1] - znsr), l) < round(1.67 * Ssko, l)) and \
            (round(abs(izm[0] - znsr), l) < round(1.67 * Ssko, l)):
        print("Грубых промахов нет!")
    else:
        print("Промахи есть, видимо питон не справляется вернись к пункту 3 и проверь вручную")


def sko():
    Ssko = 0
    for znach in izm:
        Ssko += (znach - znsr) ** 2
    Ssko = round((Ssko / (len(izm) - 1)) ** 0.5, l)
    return Ssko


izm = sorted(map(float, input("Введите ваши значения:\n").split()))
l = int(input("На сколько знаков после запятой округлять (я советую 8) "))
cena = float(input("Цену деления введи"))

R = round(abs(max(izm) - min(izm)), l)
print("R = ",R)

while True:
    if promax1():
        break

znsr = round(sum(izm) / len(izm), l)
print("Среднее значения", znsr)

print("Найдём среднеквадратичное отклонение 𝑆(ско)")
Ssko = sko()
print("𝑆(ско) = ", Ssko)

promax2()

Sskosr = round(Ssko/(len(izm)**0.5),l)
print("СКО среднего ", Sskosr)

slraz = round((0.51 * R),l)
slsko = round((2.8 * Sskosr),l)
print("Случайная погрешность по размаху ", slraz)
print("Случайная погрешность по СКО ",slsko )

delta = max(slraz, slsko)

polnpog = round((((delta**2) + (cena**2))**0.5),l)

print("Полная погрешность ", polnpog)
print("Относительная погрешность ", round(((polnpog/znsr)*100),l),"%")
print("ИИИИ НАКОНЕЦ")
print("-------------------")
print("ОТВЕТ!")
print(znsr, " ± ", polnpog)
