#function
# def reverse_string(text):
#     rev=" "
#     for ch in text:
#         rev=ch+rev
#     return rev
# print(reverse_string("diksha"))
# def palindrome(text):
#     rev=" "
#     for ch in text:
#         rev=ch+rev
#     return text == rev
# print(palindrome("yes"))
# def greet():
#     print("heelo")
# greet()
# def greet(name):
#     print("hello",name)
# greet("diksha")
# def add(a,b):
#     return a+b,a-b,a*b
# add,sub,mul=add(4,5)
# print(add)
# print(sub)
# print(mul)
# def text():
#     return 10
# print(text())
# def text():
#     print("S")
#     return 10
#     print("H")
# print(text())
# def check(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"
# print(check(6))
# def sqaure(num):
#     return num*num
# print(sqaure(4))
# def test(a):
#     print(a*2)
# x=test(5)
# print(x)
# def count_vowel(text):
#     count=0
#     for ch in "aeiou":
#         count+=1
#     return count
# print(count_vowel("education"))
# def add(*args):
#     print(args)
# add(10,20,30)
######################### LAMBDA function
# sqaure=lambda x:x*x
# print(sqaure(5))
# add=lambda x,y:x+y
# print(add(2,3))
# double=lambda x:x*2
# print(double(5))
# total=lambda x,y,u,i,o:x+y+u+i+o;
# print(total(2,34,5,6,7))
# check=lambda num:"even" if num%2==0 else "odd"
# print(check(6))
# map
# data=["10","20","30"]
# result=map(int,data)
# print(list(result))
# list compreshion
# num=[2,3,4,5,6]
# result=[nums*2 for nums in num]
# print(result)
# num=[2,3,4,5,6]
# result=[nums**2 for nums in num]
# print(result)
# chars=[ch for ch in "python"]
# print(chars)
# rsuke=[x for x in range(1,11) if x>5]
# print(rsuke)


##########exception handling
try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("cent divided by zero")
print("program cpmpleted")