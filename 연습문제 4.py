# 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 리스트로 변환하는 함수를 작성

my_list = [100,200,300]
def VAT(my_list) :
    result = []
    for var in my_list :
        result.append(int(var * 1.1))
    return result
print(VAT(my_list))


