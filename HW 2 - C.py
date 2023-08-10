season_format = "enter a number between 1 to 4"
print(f"{season_format}")
x = int(input())
print(x)
while x <= 0 or x > 4:
    print(f"Invalid number, {season_format}")
    x = int(input())
if x == 1:
    print("summer")
elif x == 2:
    print("winter")
elif x == 3:
    print("fall")
elif x == 4:
    print("spring")
