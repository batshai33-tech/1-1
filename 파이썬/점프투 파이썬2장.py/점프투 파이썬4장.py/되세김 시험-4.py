# 우리는 4-3 부터 4까지 건너뛰고 1 과 2만 하였기때문에 이만 연습할것이다

#Q1
def is_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False
print(is_odd(32))

#Q2
def avg_number(*args):
    result = 0
    for i in args:
        result += i
    return result / (len(args))

print(avg_number(1, 2))
print(avg_number(1, 2, 3, 4, 5))

#Q3
input1 = int(input())
input2 = int(input())

total = input1 + input2
print(total)

#Q4
print("you" "need" "python")
print("you" + "need" + "python")
print("you", "need", "python")
print("".join(["you" "need" "python"]))
#1 번과 2 번은 띄어쓰기가 없다
#4 번은 join 함수를 썻다지만 띄어쓰기가 없는 따음표이기에 똑같이 붙여서 나온다
#3 번은 (,)를 썻기에 (,) 를 쓰면 띄어쓰기가 된다 그럼으로 3번만 출력이 다르다