# 1. Найти НОК двух чисел
""" def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if a == 0 or b == 0:
        return a | b
    return gcd(b, a % b)
 
a, b = map(int, input().split(maxsplit=1))
print(a * b // gcd(a, b)) """

# 2. Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141

""" k = 1
x = 0
for k in range(1, 100000):
    x = x+4*((-1)**(k+1))/(2*k-1)
print(round(x, 3)) """

# 3. Составить список простых множителей натурального числа N

""" number = int(input("Введите число: "))
list_simple = []
simple = 2
while number > 1:
    if number % simple == 0:
        list_simple.append(simple)
        number = number/simple
    else:
        simple += 1
print(list_simple) """

# 4. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

""" lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}") """

#5. Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа
""" fo=open("out.txt", "w")
with open("out.txt", "r") as fi:
    for stri in fi:
        if len(stri)>0:
            arr=stri.split()
            tmp=" "
            for s in arr:
                if int(s)%2 != 0:
                    tmp+=s+" "
            fo.write(tmp+"\n")
        else:
            fo.write("\n")
fo.close() """