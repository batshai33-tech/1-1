#Q1 (아니 틀림 샤갈)
#"shirt" 와 "need" 가 출력 될것이다

#과거의 나여 위에것은 틀렸다
#최신식 컴퓨터언어는 코드를 위에서부터 밑으로 읽는다 
#거기서 가장먼저 참의 조건이 되는것은 "shirt" 임으로 "shirt" 만 출력된다

#Q2
result = int(0)
i = int(1)
while i <= int(1000):
    if i % int(3):
        result += i
    i += int(1)

print(result)

#Q3
i = 0
while True:
    i += 1
    if i >= 5:break
    print(i * '*')

#Q4

for i in range(0, 101):
    print(i)


#Q5 
A = [70, 60, 55, 75 ,95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
a = total / 10
print (a)

#Q6 
num = [1, 2, 3, 4, 5]
result = [n * 2 for n in num if n % 2]
print(result)
