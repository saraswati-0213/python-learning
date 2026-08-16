# iterartion
# nums=[10,20,30]
# it=iter(nums)
# print(next(it))
# print(next(it))
# print(next(it))
# # print(next(it))stop itreation
# nums=[10,20,30]
# it=iter(nums)
# try:
#     while True:
#         value=next(it)
#         print(value)
# except StopIteration:
#     print("finished")
# r=range(1,5)
# it=iter(r)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# num=[1,2,3,4,5]
# it=iter(num)
# print(list(it))
# print(list(it))
# genertaor= is a special type which uses yiels keyword to producse value one by one insted of getting all value at once
# def number():
#     return 10
# result=number()
# print(result)
# def number():
#     yield 10
# Result=number()
# print(Result)
# def number():
#     yield 10
#     yield 20
#     yield 30
# g=number()
# print(next(g))
# print(next(g))
# print(next(g))
# closure
# def greet():
#     return "helo"
# x=greet
# print(x())
# def outer():
#     x=10
#     def inner():
#         return x
#     return inner
# f=outer()
# print(f())
# def multiply(x):
#     def inner(y):
#         return x*y
#     return inner
# a=multiply(2)
# b=multiply(5)
# print(a(10))
# print(b(20))
# x=10
# print(id(x))
# x=x+1
# print(id(x))new result object ko refrence kartah
# a=[1,2]
# b=a
# a.append(3)
# print(a)
# print(b)
# a=[1,2]
# b=a
# a=a+[3]
# print(a)
# print(b)
# a=[1,2]
# b=a
# a+=[3]
# print(a)
# print(b)
# def ad_item(data):
#     data.append(100)
# nums=[10,20]
# ad_item(nums)
# print(nums)
a=[10,20]
b=a.copy()
b.append(30)
print(a)
print(b)