# УрокNo5.Логическиеиусловныеоператоры
# Задание № 1
# num = 20 #int(input())

# if num < 0 and num /2 == 0:
#     print("отрицательное четное число")
# elif num > 0 and num /2 == 0:
#     print("положительное четное число")
# elif num > 0 and num /2 != 0:
#     print("положительное нечетное число")
# elif num < 0 and num /2 != 0:
#     print("отрицательное нечетное число")
# else:
#     print("нулевое число")


# Задание № 2
str = 'asedfoguwawes' #input()
txt = list(str)

caunt_a = 0
caunt_e = 0
caunt_i = 0
caunt_o = 0
caunt_u = 0

for item in enumerate(str):
    key, value = item
    #print(key, value)
    if 'a' == value:
        caunt_a += 1
       
    elif 'e' == value:
        caunt_e += 1
        
    elif 'o' == value:
        caunt_o += 1
        
    elif 'i' == value:
        caunt_i += 1
        
    elif 'u' == value:
        caunt_u += 1
        
        
print('count "a" = ' , caunt_a)
print('count "e" = ' , caunt_e)
print('count "o" = ' , caunt_o)
print('count "i" = ' , caunt_i)      
print('count "u" = ' , caunt_u)


print('count letters =' , len(str))

if 'a' not in txt:
    print('False- no letter - a')
elif 'e' not in txt:
    print('False -no letter - e')
elif 'i' not in txt:
    print('False -no letter - i')
elif 'o' not in txt:
    print('False- no letter - o')
elif 'u' not in txt:
    print('False -no letter - u')






# Задание № 3
# Maykl = 15
# Ivan = 11
# min = 10

# if min < Maykl and min < Ivan:
#     print(2)
# elif min < Maykl:
#     print('Maykl')
# elif min < Ivan:
#     print('Ivan')
# elif min < Maykl + Ivan:
#     print(1)
# else:
#     print(0)
