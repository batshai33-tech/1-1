#클래스
#클래스란?:함수의 집합채라고 간략히 말할수있다
#함수 안에 여러 기능을 넣어 원할때마다 꺼내 쓸수 있다
#하지만 이를 고치고 싶을땐 뒤에서 함수 하나씩을 모두 꺼내와 안쪽 내용을 고쳐야하기에 힘들다
#함수만을 정리할수있는 무언가가 바로 클레스이다
#그럼 클레스는 어떡해 쓰이는지 알아보자

class Fourcal:
    def __init__(self,first,second):
        #기본적으로 self 라는 함수작동을 시킨 주인 의 이름을 지정해줘야한다
        #이를 지정하지 않는다면 누가 시킨거야? 라며 클레스 안 함수를 작동시켜도 작동알림이 가지않아
        #함수를 작동시킬수 없다
        #또한 맨처음 __init__는 외워주는것이 좋다
        #저개 뭐냐하면 클레스 함수를 실행시키고나서 종료시킬때 안에 있던 정보를 자동으로 초기화 시켜주는것이다

        #생각해봐라 1시간전 계산기 프로그램을 쓰고나서 나온 값을 초기화시키지않고 그냥 끄면
        #나중에 계산기 프로그램을 더 쓸때 곱하기를 한다하면 그 전에 있던 값까지 같이 더해 이상한 결과가 나오게 된다

        self.first = first
        #주인이 첫번째 숫자라는 상자를 만들어서 그 상자안에 값을 첫번째(매개변수)로 정의하셨어!
        self.second = second
        #주인이 두번째 숫자라는 상자를 만들어서 그 상자안에 값을 두번째(매개변수)로 정의하셨어!

    def add(self): #함수 +
        result = self.first + self.second
        #이함수는 주인님이 정의하신 첫번째 숫자와 두번째 숫자를 더하는거야!
        return result
        #이를 반환시켜!
    
    def sub(self):
        result = self.first - self.second
        #빼는것
        return result
    
    def mul(self):
        result = self.first * self.second
        #곱하는것
        return result

    def div(self):
        result = self.first / self.second
        #나눠서 나온값
        return result
    
e = Fourcal(5, 5)# 클레스 안에 있는 함수를 쓸려면 먼저 어떤 한 값을 클레스 안으로 지정해줘야한다
#모양은 -> 지정해주고싶은값 = 클레스이름(넣을 값) 이다
#이를 프린트 시켜야 클레스 안에 이 값을 넣어서 작동시킨다는걸 알려준다
print(e.add()) #함수를 작동시킬때 .(함수이름) 을 넣어서 어떤 함수를 작동시킬껀지 정의해줘야한다
#클레스 는 다시 넣지 않아도 된다 이미 넣었기 때문
#함수이기에 ()도 넣어줘야한다 물론 값만 리턴시키는것이기에 빈괄호로 써준다

# 이 클레스 안에 5와 5를 넣은 E 를 (add)함수를 이용하여 프린트 시킨것이다
#값을 바꿀려면 지정한 클레스 옆 값을 바꿔야한다
c = Fourcal(1, 2)
print(c.mul())



#원레 함수만 쓰면 고치고 싶거나 더 추가하고 싶을땐 다시 만들어서 써야했다
#근데 이를 클레스로 쓰면 클레스를 가져와서 거기안에다 추가하거나 고칠수있다!
# #클레스의 장점 #클레스가 좋은이유 #클레스
# 아무튼 이번엔 추가와 수정에 대해 알아보자

# ???: 쌤 삭제는요?
# 그건 그냥 처음부터 안만들면 되는거였잖아 고치거나 추가하는게 아니기에 원래있던 클레스에서 없에면되지

#추가
class morefourcal(Fourcal):
     def pow(self):
         result = self.first ** self.second
         return result

a = morefourcal(4, 2)
print(a.div())

#수정
class safefourcal(Fourcal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
        
a = safefourcal(4, 0)
print(a.div())