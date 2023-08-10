numbers = []
i = 1
while i <= 100:
    numbers.append(i)
    i = i + 1
for number in numbers:
    if number % 7 == 0 or str(number).__contains__("7"):
        print("BOOM")
        continue
    else:
        print(number)

# for i in range(1, 101):
#     not_divided_by_seven = i % 7 != 0
#     no_seven = "7" not in str(i)
#     if not_divided_by_seven and no_seven:
#         print(i)
#     else:
#         print("BOOM")
