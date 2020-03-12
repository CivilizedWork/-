x = 0
x = x + 1


def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff')


def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1


a = 4
x = 3
y = (x + a/x) / 2
print(y)
x = y
y = (x + a/x) / 2
print(y)
x = y
y = (x + a/x) / 2
print(y)
x = y
y = (x + a/x) / 2
print(y)
x = y
y = (x + a/x) / 2
print(y)
x = y
y = (x + a/x) / 2
print(y)

import math
def mysqrt(a, x,):
    while True:
        y = (x + a/x) / 2
        if abs(y - x) < 0.000000000000000001:
            break
    x = y
    return y


def test_square_root(a, x):
    my_ans = mysqrt(a, x)
    math_ans = math.sqrt(a)
    diff = abs(my_ans - math_ans)
    print(a, my_ans, math_ans, diff)


print('a    mysqrt(a)    math.sqrt(a)    diff')
print('-    ---------    ------------    ----')
test_square_root(1, 1)
test_square_root(2, 2)
test_square_root(3, 2)
test_square_root(4, 2)
test_square_root(5, 2)
test_square_root(6, 2)
test_square_root(7, 2)
test_square_root(8, 2)
test_square_root(9, 2)

import math


def eval_loop():
    ans = ''
    while True:
        print('Please enter your words:\n')
        word = input()
        if word == 'done':
            return ans
            break
        ans = eval(word)
        print(ans)


print(eval_loop())







import math

def eval_loop():
    ans = ''
    while True:
        print('Please enter your words:\n')
        word = input()
        if word == 'done':
            return ans
            break
        ans = eval(word)
        print(ans)


print(eval_loop())