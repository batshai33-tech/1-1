#튜플(tuple)

#튜플은 리스트와 거의 유사하다
#하나 다른점이라면 리스트와 다르게 값을 추가,수정,삭제 가 불가능하다는것이다
#보통 리스트는 []를 쓰지만 튜플은 ()로 쓴다 (아니면 안쓰고도 가능하다)
#튜플을 한번 써보자
t1 = (1, 2, 'a', 'b')
t2 = 3, 4, 'c', 'd'
print(t1)
print(t2)
#여기서 삭제 추가 수정을해보자
#del t1[0]

#  File "/Users/gimbeomgyu/1-1/2-3.py", line 9, in <module>
#    del t1[0]
#        ~~^^^
#TypeError: 'tuple' object doesn't support item deletion
#이렇게 오류가 날것이다
#아까도 이야기했지만 튜플은 값을,추가,수정,삭제를 하지못한다 이로인해 오류가난다

#튜플을 다룰수있는방법은 인덱싱,슬라이싱,더하기곱하기,길이구하기까지는 가능하다
print(t1[0]) #인덱싱
print(t1[:2]) #슬라이싱
print(t1 + t2) #더하기
print(t2 * 3) #곱하기(문자열끼리는 불가)
print(len(t1)) #길이구하기 (lensth)

