file = open("words.txt", "w")
file.close()

file = open("words.txt", "w")
file.write("Shay")
file.close()

file = open("words.txt", "r")
file_content = file.readlines()
print(file_content)
file.close()

file2 = open("hebrew.txt", "w", encoding="utf-16")
file2.write("שלום לכולם")
file2.close()

file2 = open("hebrew.txt", "r", encoding="utf-16")
file2_content = file2.readlines()
print(file2_content)
