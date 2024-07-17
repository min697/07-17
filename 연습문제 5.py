# 홀수/짝수 핀별기 함수. 매개변수 입력에 따라 홀수 또는 짝수를 자동으로 판변하는 함수를 작성
# 반환되는 값은 '홀수' 또는 '짝수'

def 자동 (a) :
    if a % 2 == 1 :
        result = "홀수"
    elif a % 2 == 0 :
        result = "짝수"
    return result

x= 자동(int(input("숫자를 입력하세요.")))
print(x)