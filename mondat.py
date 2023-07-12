#######   1 vazifa

# def polindrom(word):
#     return word.lower() == word[::-1].lower()
#
# while True:
#     user_input = input('So\'z yozing: ')
#     if user_input.lower() == 'stop':
#         break
#     print(polindrom(user_input))
#### 2 vazifa

# def bank(money, year):
#     i = 0
#     while i < year:
#         money += money * 0.1
#         i += 1
#
#     return money
#
# while True:
#     user_money = input('Pul miqdorini kiriting: ')
#     user_year = input('Yilni kiriting: ')
#
#     if user_money.lower() == 'stop' or user_year.lower() == 'stop':
#         break
#
#     print(round(bank(int(user_money), int(user_year)), 2))

### 3 vazifa

# nums = [45, 55, 60, 37, 100, 105, 220]
#
# def get_list(array):
#     result = []
#     for item in array:
#         if item % 15 == 0:
#             result.append(item)
#
#     return result

# x = 'Global'
# y = 20
# def f1():
#     x = 'local'
#     print(x)
#
# f1()
#
# def f2():
#     global y
#     y += 5
#     print(y)
#
# f2()


# x = 30
#
# def f4():
#     x = 23
#     def f5():
#         nonlocal x
#         x *= 2
#         print(x)
#     f5()
# f4()


# lst = [item for item in range(1, 11)] # generator
# def f1(array, num):
#     result = [item * num for item in array]
#     # for item in array:
#     #     result.append(item * num)
#     return result
#
# print(f1(lst, 4))

# def f2(arr):
#     result = []
#     for item in arr:
#         if item % 2 == 0:
#             result.append(item)
#     # gen_result = [i for i in arr if i % 2 == 0]
#
#     return result
#
# print(f2([1, 2, 3, 4, 5, 6, 7, 8]))

# def get_multipy(num):
#     return num ** 2
#
# print(get_multipy(4))

# get_multipy = lambda num: num ** 2
# print(get_multipy(6))
# user_num = int(input('Son kiriting: '))

# print(get_multipy(user_num))
#
# get_mlt = lambda x, y: x * y

get_mlt = lambda x: x * 2

lst = [item for item in range(1, 16)]
result = []
for item in lst:
    result.append(get_mlt(item))
print(result)
gen_result = [get_mlt(i) for i in lst]
print(gen_result)

