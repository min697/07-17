# 구구단 함수 작성. 매개변수 입력에 따라 해당 구구단을 하면에 출력
def print_mul_numbers(x):
    print("[", x, "]단")
    for i in range(1,10):
        print(x,"x",i, "=", x*i )

print_mul_numbers(23)


