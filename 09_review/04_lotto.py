from random import sample

def gen_lotto_bonus():
    return sample(range(1, 46), 7)

def gen_lotto():
    return sample(range(1, 46), 6)

def lotto_sample(n):
    result = []
    for _i in range(n):
        result.append(gen_lotto())
    return result

def count(data, answer):
    one = 0
    two = 0
    thr = 0
    fou = 0
    fiv = 0
    s2 = set(answer[:-1])

    for elem in data:
        s1 = set(elem)
        intersection = s1 & s2
        num = len(intersection)
        if num == 6:
            one += 1
        elif num == 5:
            if answer[-1] in s1:
                two += 1
            else:
                thr += 1
        elif num == 4:
            fou += 1
        elif num == 3:
            fiv += 1

    return (one, two, thr, fou, fiv)

def calc(n, result):
    (one, two, thr, fou, fiv) = result
    total = n * 5000
    total -= fou * 50000 + fiv * 5000
    one_total = total * 0.75
    two_total = total * 0.125
    thr_total = total * 0.125
    if one == 0:
        print("1등은 없습니다.")
    else:
        print("1등 당첨금은 {}입니다.".format(one_total / one))
    if two == 0:
        print("2등은 없습니다.")
    else:
        print("2등 당첨금은 {}입니다.".format(two_total / two))
    if thr == 0:
        print("3등은 없습니다.")
    else:
        print("3등 당첨금은 {}입니다.".format(thr_total / thr))

def main():
    n = 10000000
    answer = gen_lotto_bonus()
    data = lotto_sample(n)
    result = count(data, answer)
    print(result)
    calc(n, result)

if __name__=="__main__":
    main()
