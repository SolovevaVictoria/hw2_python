# 1 вводится кол-во и стороны в виде 1 и 0 через пробел
'''
n = int(input())
side = input()
print(side.count('0') if side.count('1') > side.count('0') else side.count('1'))
'''

# 2 Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
'''
S, P = int(input()), int(input())
discriminant = S ** 2 - 4 * P
Flag = True
if discriminant > 0:
    x = int((S - discriminant ** 0.5) / 2)
elif discriminant == 0:
    x = S // 2
else:
    Flag = False


if Flag:
    y = S - x
    print(x, y)
else:
    print('неверные входные данные')
'''

# 3 Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n = int(input())
i = 0
st = 2 ** i
while st <= n:
    print(st, end=' ')
    i += 1
    st = 2 ** i