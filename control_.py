#사용값을 받아
data = input("값을 입력하세요")
#2 입력값에 100 더함
data_2 = int(data) + 100
#2-1 100을 더할때, 데이터타입 변환(문자->숫자)
#3 더한 값 150초과, 사용자 입력값을 출력
if data_2 > 150:
    print(data)
#4. 더한값이 150이하인경우 값이 모자랍니다 출력
elif data_2 <=150:
    print("값이 모자랍니다")





if 5<x and x<10:
    print(x)

else:
    print("no")

#and, or 연산자
apple='사과'
banana='감자'

if apple == '사과' or banana=='바나나':
    print("문자열이 정확합니다.")

var = [1,2,3]
if 찾고자 하는 요소 in 변수:
    print("숫자 3이 var 변수에 있습니다.")


#입력받기
#입력받은 값이 fruit에 요소로 있는지 확인

text=input("과일을 입력하세요")
fruit=["사과","포도","홍시"]
if text in fruit:
    print("정답입니다")
else:
    print("오답입니다")

text=input("과일과 계절을 입력하세요")
fruit={"봄":"딸기", "여름":"토마토", "가을":"사과"}
if text in fruit.keys():
    print("정답입니다")
else:
    print("오답입니다")


data=input("메세지를 입력하세요")
data_2=(len(data))
if data_2 <= 20:
    print("50원 입니다.")
if data_2> 20:
     print("100원 입니다."


