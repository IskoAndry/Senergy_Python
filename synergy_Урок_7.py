# Урок N 7. Строки
# Задание № 1
# str = "sak"

# if str[0::] == str[::-1]:
#     print("YES")
# else:
#     print("NO")

# Задание № 2

str1 = "Python is a great language!, said Fred. I ever remember having this much fun before."

for i in str1:
    if i == " ":
        print(i, end="")

print("==========================================")
lst = str1.split(" ")
res = "".join(lst)
print("строка без пробелов" + res)

print(len(str1))
