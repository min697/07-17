# 문자메세지 길이 판별함수.
# 문자 메시지 길이에 따라 문자 요금이 결정되는 프로그램을 작성하시오.
def length(a) :
    b = len(a)
    if b <= 20 :
        print("50원")
    else :
        print("100원")


a = input("입력")
# 길이가 20 이하이면 50원이며, 20 을 초과하면 100원이다.
# 사용자로부터 문자메시지를 입력받아서 문자 요금을 반환하는 코드

length(a)

# 교수님
def find_len(x):
    result = 0
    if result <= 20 :
        result=50
    elif len(x) > 20:
        result = 100
    return result
text = input("문자 메시지를 입력해주세요.")
var = find_len(text)
print(var)