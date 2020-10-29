  
print("Введите сумму, границы первого промежутка и границы второго промежутка на одной строке через пробел")
s, l1, r1, l2, r2 = map(int, input().split())
success = True

x1 = l1
x2 = 0

if x1 + r2 < s:
    # Значит, если увеличить х2 на максимум
    # x1 + x2 всё равно меньше s
    x2 = r2

    # Если r1 + r2 меньше s
    # тогда s больше максимально возможной суммы иксов
    if s > r1 + x2:
        print("Нет таких иксов")
        success = False
    else:
        # Иначе ищем х1 такой, чтобы x1 + x2 = s
        x1 = s - r2
else:
    # Здесь мы понимаем, что x1 + r2 > s
    # Два варианта: 1. s меньше минимальной суммы иксов
    #               2. s возможно получить суммой иксов
    
    # Проверяем первый варииант
    if s < l1 + l2:
        print("Нет таких иксов")
        success = False
    else:
        # Здесь s можно получить суммой иксов
        x2 = s - x1

if success:
    print("x1 = {}\nx2 = {}".format(x1, x2))