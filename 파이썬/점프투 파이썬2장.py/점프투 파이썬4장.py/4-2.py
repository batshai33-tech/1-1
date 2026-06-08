# input()(사용자의 입출력)

#우린 전까지 미리 코드 안에다가 수를 써서 출력했다
#하지만 당연히도 게임에서 닉네임을 정하거나 만든 함수안에 원하는 값을 넣을때
#사용자가 직접 입력하기도 한다
#이를 우리는 input() 으로 해결을 할것이다

a = input()
print(a)

#()안에다가 미리 프롬포트를 쓸수도있다

b = input("숫자를 입력해주세요 :")
print(b)
c = input("이름을 입력해주세요 :")
print(c)

#그리고 input() 은 모든수를 문자열로받는다 주의하자
print(type(b))
#숫자를 입력해도 문자열로 나오는걸 볼수있따

#이번엔 사용자에게 입력받은 값을 더해보자

a = input()
b = input()
print(a + b)
# 하지만 인풋으로 입력받은 값은 문자열이기에 3 과 4를 입력하면 "34" 가 나온다
#이를 숫자형으로 형을 변환시켜보자

c = (int(input("첫번째 숫자를 입력해주세요 :")))
d = (int(input("두번째째 숫자를 입력해주세요 :")))
print(c + d)

#정수뿐만아니라 다른형식으로도 변환할수있다
height = input("키를 입력하세요(cm) :")
height = float(height)
print(height / 100)

#근데 따로바꾸기엔 너무 길지않나? 이걸 한줄로 바꿀수도 있다
age = int(input("나이를 입력해주세요 :"))
print(type(age))
print(age)

#이제 입력은 됬고 프린트를 좀더 자새히 알아보고 정리해보자

# 숫자형,문자형,리스트를 입력받을수 있는건 다들알꺼다
print(123)
print("hello wolrd")
print([1, 2, 3])
#이제 추가적으로 알 사항을 알려주겠다
#1.따음표로 둘러싸인것과 + 는 똑같다 이걸한번 실행해보자
print("Life" "is" "to" "short")
print("Life" + "is" + "to" + "short")
#그대로 "삶은 너무 짦아"가 모두 붙여져서 출력되었다 

#그렇다면 이걸 나눠서 출력할순 없는걸까?
print("Life","is","to","short")
#이대로 실행하면 공백이 추가된걸 알수있다
#이는 공백 사이사이 마다 (,)따음표를 추가했기 때문이다

#그럼 나누지말그 그 사이에다 뭔가 다른걸 넣어서 출력시킬순 없을까?
#이는 sep 매개변수를


#그럼 프린트의 대해서도 배웠으니 실습으로 간단한 계산기를 만들어보자
num1 = input()
num2 = input()
num1 = int(num1)
num2 = int(num2)
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
#input()은 무조껀 문자열로 받는다는걸 꼭 기억하자

