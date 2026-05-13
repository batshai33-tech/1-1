#숫자열
print(10 + 3) #더하기
print(10 - 3) #빼기
print(10 * 3) #곱하기
print(10 / 3) #나누기
print(10 % 3) #나머지
print(10 ** 3) #제곱
print(10 // 3) #몫


#문자열
a = "hello wolrd"
b = 'hello 김범규'
c = '''Life is 
to surt'''
d = """you need
Python"""
print(a)
print(b)
print(c)
print(d)
print('hi'+"Python")
print(a * 3)
print(len("hello"))
e = len(d)
print(e)
print("hello\nworld") #줄바꿈
print("hello\tworld") #간격
print("hello\\world") # \ 그 자체
print("hello \'w\'orld") #작은따음표(') 그 자체
print("hello \"w\"orld") #큰따음표(") 그 자체


#인덱싱 & 슬라이싱
#모든 코드는 숫자를 0부터 센다 
#그니까 문자열의 1번째자리 = 0 이다
a = "Python"
print(a[0]) #Python 에 1번째 자리 문자
print(a[-1]) #Python 에 6번째자리(뒤에서 첫번째자리) 문자
print(a[0:3]) #Python 에 1번째 자리부터 3번째 자리까지의 문자
print(a[2:]) #Python 에 3번째 자리부터 끝까지
print(a[:3]) #Python 에 처음부터 3번째 자리까지


#포메팅
name = "김범규"
age = 17
birth = "10년 5월 14일"
year = 2026
print(f"재 이름은 {name} 이고요 생일이 {birth}인지라 {year}기준으로 나이는 {age}살 입니다")

#리스트
a = [1, 2, 3, 4, 5] #리스트는 [](대괄호) 를씀
print(a)
#인덱싱
print(a[0])
print(a[-1])
#슬라이싱
print(a[0:3])
print(a[2:])
print(a[:3])
b = "12345"
#[,] 없는
#값수정
a[0] = 99
print(a)
#값삭제
del a[0]
print(a)
#리스트 서로 더하기
print([1, 2] + [3, 4])
#리스트 곱하기
print([0] * 3)
print([1, 2] * 3)
#리스트 길이 구하기
print(len([1, 2, 3]))

#리스트 주요 함수
#기본적으로 함수를 쓰는 방법 (정의한 자료형.함수)
a = [3, 1, 2] #리스트 만들기
a.append(4) #끝에 값 추가
print(a)
a = [3, 1, 2]
a.insert(0, 9) #(위치, 값) 0번 위치에 값 삼입
print(a)
a = [3, 1, 2]
a.remove(3) #값 3 제거
print(a)
a = [3, 1, 2]
print(a.pop()) #마지막 값 출력후 삭제
a = [3, 1, 2]
a.sort() #리스트 오름차순 정렬(숫자열)
print(a)
a = [3, 1, 2]
a.reverse() #리스트 뒤집기
print(a)
a = [3, 1, 2]
print(a.count(1)) #(값)이 리스트에 얼마나 있는지
a = [3, 1, 2]
print(a.index(2)) #2의 인덱스 위치
a = [3, 1, 2]
a.extend([5, 6]) #리스트 이어붙이기 [1, 2, 3] => [1, 2, 3, 4, 5]
print(a)
b = a #복사가아님 b에다 a를 넣는다
b = a[:] #복사임 a 의 처음부터 끝까지의 값을 b에 넣는다
#1번 a 는 사라짐
#2번 a 에 처음부터 끝까지를 b에다 넣는것이라 사라지지않음