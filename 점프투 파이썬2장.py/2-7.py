# 불 자료형(True, False)
# 불 자료형은 참과 거짓을 나타내는 자료형이다
# 참은 True 거짓은 False로 표현한다

a = True
b = False
q = [1, 2, 3]
w = (1, 2, 3)
e = set([1, 2, 3])
r = {1 : 'hi', 2 : 'bye'}
print(type(a)) #a 라는 변수의 자료형을 출력한다 -> bool 반환
print(type(b)) #b 라는 변수의 자료형을 출력한다 -> bool 반환
print(type(q)) 
print(type(w))
print(type(e))
print(type(r))
# 불 자료형은 주로 조건문과 반복문에서 사용된다
# 조건문과 반복문은 나중에 3장에서 배울것이니 지금은 불 자료형이 참과 거짓을 나타내는 자료형이라는것만 알아
print(1 > 2) #1이 2보다 큰지 비교한다 -> False 반환
print(1 < 2) #1이 2보다 작은지 비교한다 -> True 반환
print(1 == 2) #1이 2와 같은지 비교한다 -> False 반환
print(1 != 2) #1이 2와 다른지 비교한다 -> True 반환

# 불 자료형을 이용해서 참과 거짓을 어떡해 구분할까
# 이제 활용하는 법의 대해 알아보자
# 출력 앞에다 bool() 함수를 붙여서 불 자료형으로 변환할수있다
print(bool(True)) #0은 참이 아니다 -> False 반환
print(bool()) #1은 참이다 -> True 반환


# 자료형에 참과 거짓있어???
# 이렇게 생각할수도 있지만 참과 거짓은 분명 있다
# 이는 중요하며 실제로도 자주쓰이니 알아두자

#다음은 자료형의 참과 거짓을 구분하는 기준을 알아보자
#먼저 참과 거짓을 구분하는 코드는 bool(참과 거짓을 나눌 값) 을 프린트하면 알수있다

#1. 숫자형은 0이 참이 아니고 나머지는 참이다
print(bool(0)) #0은 참이 아니다 -> False 반환
print(bool(1)) #1은 참이다 -> True 반환
print(bool(-1)) #-1은 참이다 -> True 반환
#2. 문자열은 빈 문자열이 참이 아니고 나머지는 참이다
print(bool('')) #빈 문자열은 참이 아니다 -> False 반환
print(bool('Hello')) #빈 문자열이 아니므로 참이다 -> True 반환
#3. 리스트, 튜플, 딕셔너리, 집합은 빈 자료형이 참이 아니고 나머지는 참이다
print(bool([])) #빈 리스트는 참이 아니다 -> False 반환
print(bool(())) #빈 튜플은 참이 아니다 -> False 반환
print(bool({})) #빈 딕셔너리는 참이 아니다 -> False 반환
print(bool(set())) #빈 집합은 참이 아니다 -> False 반환
#4. None은 참이 아니다
print(bool(None)) #None은 참이 아니다 -> False 반환
#5. 그 외의 모든 것은 참이다
print(bool(0.0)) #0.0은 참이 아니다 -> False 반환
print(bool([0])) #[0]은 빈 리스트가 아니므로 참이다 -> True 반환
print(bool((0,))) #(0,)은 빈 튜플이 아니므로 참이다 -> True 반환
print(bool({'a': 1})) #{'a': 1}은 빈 딕셔너리가 아니므로 참이다 -> True 반환
print(bool(set([0]))) #set([0])은 빈 집합이 아니므로 참이다 -> True 반환    
