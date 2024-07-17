# 학점 변화기 함수, 점수구간에 해당하는 학점이 아래와 같이 정의되어있다.

# 사용자로부터 스코어를 입력 받아 학점으로 환산하여 반환하는 함수을 작성
def score(s) :
    if 81 <= s <= 100:
        print("A")
    elif 61 <= s <= 80:
        print("B")
    elif 41 <= s <= 60:
        print("C")
    elif 21 <= s <= 40:
        print("D")
    elif 0 <= s <= 20:
        print("E")
sc = int(input("점수를 입력하세요"))

score(sc)
