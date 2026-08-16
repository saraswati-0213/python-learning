# #conditional statement
# age=19
# if age>18:
#     print("adult")
# # is-else:is we havw to check 2 posibilites
# age=19
# if age>18:
#     print("adult")
# else:
#     print("not adult")
# # elif
# marks=45
# if marks>=90:
#     print("grade A")
# elif marks>=80:
#     print("grade B")
# else:
#     print("fail")
# age=21
# marks=75
# if age>=18 and age<=25 and marks>=60:
#     print("eligible")
# else:
#     print("not eligible")
# username="diksha"
# password="1234"
# if username=="diksha" and password=="1234":
#     print("correct")
# else:
#     print("inccoreect")
# day="monday"
# if day=="monday" or day=="tuesday":
#     print("weekend")
# else:
#     print("working day")
# nested if 
# age=22
# has_id=True
# if age>=18:
#     if has_id:
#         print("entry allowed")
#     else:
#         print("id required")
# else:
#     print("underage")
# a=23
# b=24
# if a>b:
#     print("A is greater")
# elif b>a:
#     print("B is greater")
# else:
#     print("both are eqaul")
# a=23
# b=24
# c=34
# if a>b and a>c:
#     print("A is greater")
# elif b>a and b>c:
#     print("B is greater")
# elif c>a and a>b:
#     print("c is greater")
# else:
#     print("3 of them are eqaul")
# year=2000
# if year%400==0 or (year%100==0 and year%4==0):
#     print("leap year")
# else:
#     print("not")
# num=55
# if num%5==0 and num%11==0:
#     print("divisble by both")
# else:
#     print("not")
# num=15
# if num%5==0 or num%3==0:
#     print("divisble by both")
# else:
#     print("not")
# num=55
# a=num%3==0
# b=num%5==0
# if (a or b) and not(a and b):
#     print("one of them")
# else:
#     print("noth or niether")
# simple calculator
# a=10
# b=4
# oprator="*"
# if oprator=="+":
#     print(a+b)
# elif oprator=="-":
#     print(a-b)
# elif oprator=="*":
#     print(a*b)
# elif oprator=="/":
#     print(a/b)
# elif oprator=="%":
#     print(a%b)
# else:
#     print("invalid opratoe")
# a=4
# b=3
# c=7
# if(a==b==c):
#     print("equilateral")
# elif a==b or b==c or a==c:
#     print("isosceles")
# else:
#     print("scalene")
# ternary
# num=8
# result="even" if num%2==0 else "odd"
# print(result)
################ MATCH CASE
# choice=2
# match choice:
#     case 1:
#         print("add")
#     case 2:
#         print("update")
#     case 3:
#         print("delete")
#     case 4:
#         print("invalid")
# x=0
# if x:
#     print("ture")
# else:
#     print("false")

# x=[]
# if x:
#     print("ture")
# else:
#     print("false")
# x=None
# if x is None:
#     print("missing")
# else:
#     print("available")
# a=23
# b=12
# c=11
# if a<b and a<c:
#     print("a is smaller")
# elif b<a and b<c:
#     print("b is smaller")
# elif c<b and c<a:
#     print("c is smaller")
# else:
#     print("equal")
amount=6000
if amount>=5000:
    discount=amount*0.20
    final_amount=amount-discount
    print(final_amount)
elif amount>=2000:
    discount=amount*0.10
    final_amount=amount-discount
    print(final_amount)
else:
    print("no discount")




