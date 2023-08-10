def addition(int1, int2):
    sum1 = int1 + int2
    return sum1


def space(str1, str2):
    sentence = f"{str1} {str2}"
    return sentence


a, b = input(), input()
print(addition(a, b))
c, d = input(), input()
print(space(c, d))

