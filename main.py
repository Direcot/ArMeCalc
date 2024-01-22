i = 0
s = 0
p = 0
while True:
    m = int(input(">>"))
    if m <= 5 or m >= 2:
        if m == 0:
            break
        s += m
        i+=1
    if m > 5 or m < 2:
        print("Введено неверное значение")
a = round(s/i, 2)
if a*100%100 >= 60:
    p = (a*100 // 100)+1
else:
    p = a*100 // 100
print("Среднее арифметическое:",a)
print("Предпологаемая оценка:",int(p))