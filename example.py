# 4. More Control Flow Tools

# a, b = 0, 1
# while a < 1000:
#     print(a, end=',')
#     a, b = b, a+b
# # 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,

# i = ['a', 'b', 'c', 'd']
# print(i[1:])

# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status


# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

# prompt = 'ye'

# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)

# ask_ok(prompt)

# i = 5

# def f(arg=i):
#     print(arg)

# i = 7
# f()

# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L

# L()

# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])

# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")


# def pos_only_arg(arg, /):
#     print(arg)

# def pos_only_arg(*, arg):
#     print(arg)

# pos_only_arg(arg=2)
# pos_only_arg(2)


# def foo(name, /, **kwds):
#     return 'name' in kwds

# res = foo(5, **{'name': 1})
# print(res)


# def print_something():
#     '''kgjsdkfhgsdfgkjsdfg

#     l;fgjdsgkljsdlfkjgsdf
#     '''
#     pass

# print(print_something.__doc__)


### 5. Data Structures

list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = ['b', 'c', 'd']

# list1.append('k')
# print(list1)
# ['a', 'b', 'c', 'd', 'e', 'f', 'k']


# list1.append(list2)
# print(list1)
# prideda prie pirmo listo kita lista liste. Pvz:
# Pvz.: ['a', 'b', 'c', 'd', 'e', 'f', ['b', 'c', 'd']]


# list1.extend(list2)
# print(list1_ 
# Pvz.: ['a', 'b', 'c', 'd', 'e', 'f', 'b', 'c', 'd']


# list1.insert(2, list2)
# print(list1)
# ['a', 'b', ['b', 'c', 'd'], 'c', 'd', 'e', 'f']


# list1.remove('c')
# print(list1)
# # ['a', 'b', 'd', 'e', 'f']

# print(list1)
# list1.pop(2)
# print(list1)
# # ['a', 'b', 'd', 'e', 'f']


# squares = []
# for x in range(10):
#     squares.append(x**2)


# print(squares)
# # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# squares = [x**2 for x in range(10)]
# print(squares)
# # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# a = 3
# b = a**2
# print(b)

# print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))

# print(combs)
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# print([ y for x in [1,2,3] for y in [1,2,3]])

# print(['labas' for i in range(5)])
# # ['labas', 'labas', 'labas', 'labas', 'labas']


# vec = [[1,2,3], [4,5,6], [7,8,9]]
# listo = [num for elem in vec for num in elem]
# print(listo)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# >>> vec = [[1,2,3], [4,5,6], [7,8,9]]
# >>> [num for elem in vec for num in elem]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]



# a = set('abracadabra')
# b = set('alacazam')

# print(a)
# print(b)                                  # unique letters in a
# print(a - b)                              # letters in a but not in b
# print(a | b)                              # letters in a or b or both
# print(a & b)                              # letters in both a and b
# print(a ^ b)                              # letters in a or b but not both


# def contact(*args, sep='+'):
#     return sep.join(args)

# print(contact('earth', 'mars', 'venus'))
# print(contact('lapas', 'labas', 'venus', sep='+'))


# def make_incrementor(n):
#     return lambda x: x + n

# fo = make_incrementor(42)

# print(fo(0))
# print(fo(10))
# #42
# #52

# def calc(n):
#     return lambda x: x + n
# fo = calc(42)
# print(fo(10))

# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)
# # {'r', 'd'}


# tel = {'jack': 4098, 'sape': 4139}
# print(tel)


# for i in reversed(range(10)):
#     print(i)
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0

# for i in range(5, 10, 2):
#     print(i)

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(set(basket)):
#     print(f)

# listo = ['a', 'd', 'a', 'c', 'b']
# for i in sorted(set(listo)):
#     print(i)


# addtwo = lambda x: x + 2 
# print(addtwo(50))


# def addtwo(b):
#     return lambda x: x + b

# a = addtwo(50)
# print(a(5))


# def calc(a):
#     return lambda c: c * a


# res = calc(3)
# print(res(5))


