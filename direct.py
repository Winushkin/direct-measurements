def promax_grubiy():
    global izm
    print(* izm)
    print(round(abs(izm[0] - izm[1]), l), " < ", round(0.64 * R, l))
    print(round(abs(izm[-1] - izm[-2]), l), " < ", round(0.64 * R, l))
    if not (round(abs(izm[0] - izm[1]), l) < round(0.64 * R, l)):
        print("Промахи есть, -1 значение!\n")
        izm.pop(0)
        return False
    elif not round(abs(izm[-1] - izm[-2]), l) < round(0.64 * R, l):
        print("Промахи есть, - последнее значение!\n")
        izm.pop(-1)
        return False
    print("Промахов нет!\n")
    return True


def promax_sko():
    print(round(abs(izm[-1] - znsr), l), "<", round(1.67 * Ssko, l))
    print(round(abs(izm[0] - znsr), l), "<", round(1.67 * Ssko, l))
    if (round(abs(izm[-1] - znsr), l) < round(1.67 * Ssko, l)) and \
            (round(abs(izm[0] - znsr), l) < round(1.67 * Ssko, l)):
        print("промахов нет!\n")
    else:
        print("Промахи есть, видимо питон не справляется вернись к пункту 3 и проверь вручную\n")


def sko():
    Ssko = 0
    for znach in izm:
        Ssko += (znach - znsr) ** 2
    Ssko = round((Ssko / (len(izm) - 1)) ** 0.5, l)
    return Ssko

izm = list(map(float, input("Введите ваши значения:\n").split()))
l = int(input("На сколько знаков после запятой округлять (я советую 8) "))
cena = float(input("Цену деления введи: "))

print("1) Берем результаты измерений")
print(*izm, "\n")

print("2) Упорядочим выборку")
izm.sort()
print(*izm, "\n")

print("3) Найдем размах выборки")
R = round(abs(max(izm) - min(izm)), l)
print(f"R = |{izm[-1]} - {izm[0]}| =", R, "\n")

print("4) Проверим на грубые промахи по СКО")
while True:
    if promax_grubiy():
        break

print("5) Расчитаем среднее значение")
znsr = round(sum(izm) / len(izm), l)
print("Среднее значения", znsr, "\n")

print("6) Найдём среднеквадратичное отклонение 𝑆(ско)")
Ssko = sko()
print("𝑆(ско) = ", Ssko, "\n")

print("7) Проверим на промахи")
promax_sko()

print("8) Найдем ско среднего:")
Sskosr = round(Ssko/(len(izm)**0.5),l)
print("СКО среднего ", Sskosr, "\n")

print("9) Найдем случайную погрешность по размаху и ско")
slraz = round((0.51 * R),l)
slsko = round((2.8 * Sskosr),l)
print("Случайная погрешность по размаху ", slraz)
print("Случайная погрешность по СКО ",slsko )
print(f"{slsko} = {slraz}\n")
delta = max(slraz, slsko)

print("10) Найдем полную погрешность:")
polnpog = round((((delta**2) + (cena**2))**0.5),l)
print("Полная погрешность ", polnpog)
print("Относительная погрешность ", round(((polnpog/znsr)*100),l),"%")

print("ОТВЕТ!")
print(znsr, " ± ", polnpog)
