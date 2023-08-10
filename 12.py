my_file = open("names.txt")
names = my_file.readlines()
for name in names:
    print(f"hello {name}", end='')

my_file.close()

my_file2 = open("names.txt", "a+")
for i in range(3):
    my_file2.write(input("enter name: ") + "\n")


my_file2.seek(0)
names = my_file2.readlines()
for name in names:
    print(f"hello {name}", end='')

print("shay")
