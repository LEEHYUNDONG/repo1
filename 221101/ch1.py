## python basic
'''
expresion 객체 - 1개의 타입을 가진 것, 이름을 부여할 수 있음.
'A' if a > 100 else 'B' -> expression 임.


lambda a, b : expr 

lambda param_lst : expr
'''

def func(a, b):
    return a + b


print("a + b =", func(10, 12))


# lambda 예시
lb = lambda a, b : a + b

print(lb(1, 2))

# 두 lst의 합을 구하는 식 작성
lst1 = [1, 2 , 3, 4, 5]
lst2 = [3, 6, 9, 12, 15]
print(list(map(lambda a, b : a + b, lst1, lst2)))

# zip, list comprehension 으로 리스트의 합 구하기
print([a+b for a, b in zip(lst1, lst2)])
print([sum(x) for x in zip(lst1, lst2)])


# 1의 자리 숫자를 0으로 바꿔라
age = [2333, 4532, 38, 51]
print([i - i%10 for i in age])


'''
simple statement
compound statement
'''

def stmtFn(a):
    return "a는 5보다 크다" if a> 5 else "a는 5보다 작다"

print(stmtFn(10))
###############################################################


