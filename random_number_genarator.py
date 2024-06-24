from random import choice
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
list_n = [a, b, c, d, e, f, g, h, i]
main = '88019'
for i in range(0, 1001):
    number = choice(list_n)
    number1 = choice(list_n)
    number2 = choice(list_n)
    number3 = choice(list_n)
    number4 = choice(list_n)
    number5 = choice(list_n)
    number6 = choice(list_n)
    number7 = choice(list_n)
    print(f'{main}{number}{number1}{number2}{number3}{number4}{number5}{number6}{number7}')
