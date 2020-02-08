# 특정 숫자에 대한 구구단
def specific_mult_table(n):
    for i in range(1, 10):
        print("{} x {} = {}".format(n, i, n*i))

# 전체 구구단
def whole_mult_table():
    for i in range(1, 10):
        specific_mult_table(i)

mode = input("모드를 선택하십시오.\n1. 특정 구구단, 2. 전체 구구단\n> ")
if int(mode) == 1:
    # 특정 구구단 실행
    while True:
        n = input("몇 단을 출력하시겠습니까?\n> ")
        print()
        # 에러 처리 (Error Handling)
        try:
            n = int(n)
            if n >= 1 and n <= 9:
                break
            else:
                print("1 ~ 9 사이의 정수를 입력해야 합니다.\n")
        except:
            print("1 ~ 9 사이의 정수를 입력해야합니다.\n")
            continue
    specific_mult_table(n)
elif int(mode) == 2:
    # 전체 구구단 실행
    whole_mult_table()
else:
    print("모드를 잘못 입력하였습니다.")
    