# Q1
a = 80
b = 75
c = 55
print((a + b + c) / 3)

# Q2
# 2로 나누었을때 떨어진다면 짝수 아니라면 홀수다
a = 13
print(a % 2 == 0)
# False 가 나오니 13은 홀수이다

# Q3
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# Q4
print(pin[7])

# Q5 #틀렸엇다
a = "a:b:c:d"
b = a.replace(':', '#')
print(b)

# Q6
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# Q7 #틀렸엇다
a = ['Life', 'it', 'to', 'short']
b = " ".join(a)
print(b)

# Q8 #틀렸엇다
t1 = (1,2,3)
t2  = (4,)
print(t1 + t2)

# Q9
#아마 3번째 경우가 오류가 날것이다
#딕셔너리에선 뷸부분은 리스트로 쓸수있지만
#키 부분은 리스트로 못쓴다
#이때 오류가난다

# Q10 #틀렸었다
a = {'A':90, 'B':80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
a = [set(a)]
b = [list(a)]
print(b)

# Q12
a = b = [1, 2, 3]
a[1] = 4
print(b)
#b 값도 똑같이 1, 4, 3 이 된다
#전에 설명한듯이 a 갑을 복사해 b 에 넣어도 객체 이름은 다르다했다
#하지만 이는 a 를 b 로 지정한것이기에
#a 가 영향을 받으면 b 도 똑같이받는다
#그리고 객체만 따로지 값은 .copy()를 하면 똑같아진다