######   mutable/immutable ####
# s="python"
# # s[0]="j" so we cant change directly 
# # print(s)
# s="j"+s[1:]
# print(s)
# data=(10,[20,30])
# data[1].append(40)
# print(data)
# a=[1,2,3]
# b=a
# b.append(4)
# print(a)
# print(b)
# a=[1,2,3]
# b=[1,2,3]
# print(a==b,a is b) is comapre object identity and == checks value of variable
##### TYPE CONVERSIOn #####
# print(int(-34.9))
# print(int("34"))
# truthy /falsy
# name="python"
# if name:
#     print("value exits")
# a=10
# b=3.5
# c=a+b
# print(c) implicit type conversion
# a=[1,2]
# b=a.copy()
# b.append(3)
# print(a)
# print(b)
# a=[1,2]
# b=a
# b=[10,20]
# print(a,b)
# x="pyython"
# print(bool(x))
# print(bool("False"))
# x=int(5.6)
# print(x)
# x=int(-5.6)
# print(x)
# data=(10,[20,30])
# data[1].append(40)
# print(data)
# a="heelo"
# b=a
# a=a+" "+"python"
# print(a,b)
# a=[1,2]
# b=a
# a+=[3]
# print(b)
######### PRACTICE QUESTION #####
# celcuius=float(input("enter celcuis"))
# f=(celcuius*9/5)/32
# print(f)
# minuts=int(input("enter minutes"))
# seconds=minuts*60*60
# print(seconds)
# seconds=int(input("enter seconds"))
# minuts=seconds//60
# remaining_seconds=seconds%60
# print(f"minutes:{minuts} and remaing seconds:{remaining_seconds}")
# num=123456
# last3Digit=num%1000
# print(last3Digit)
# num=9876
# result=num//1000
# print(result)
a=[10,20]
b=a
c=a.copy()
c.append(40)
b.append(30)
print(a,b,c)
