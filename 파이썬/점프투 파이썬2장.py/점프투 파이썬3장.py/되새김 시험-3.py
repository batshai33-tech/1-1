#Q1 (틀렸엇다))

#파이썬같은 경우 코드를 위에서부터 밑으로 읽는다 
#거기서 가장먼저 참의 조건이 되는것은 "shirt" 임으로 "shirt" 만 출력된다

#Q2
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print (result)

#Q3
i = 0
while True:
    i += 1
    if i >= 5:break
    print(i * '*')

#Q4

for i in range(1, 101):
    print(i)


#Q5 
A = [70, 60, 55, 75 ,95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
a = total // 10
print (a)

#Q6 
num = [1, 2, 3, 4, 5]
result = [n * 2 for n in num if n % 2]
print(result)
# 리스트 컴프리핸션