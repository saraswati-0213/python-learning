# loop
# for i in range(5):
#     print(i)
# nums=[1,2,3,4,5,6]
# for i in nums:
#     print(i)
# data=(1,2,3,4)
# for item in data:
#     print(item)
# a={10,2,3,4}
# for i in a:
#     print(a)
# student={
#     "name":"diksha",
#     "age":21,
#     "course":"js"

# }
# for x in student.values():
#     print(x)
################# range: loops m number genreate krne ke liye use hoti h
# for i in range(1,6):
#     print(i)
# for i in range(1,10,2):
#     print(i)
# for i in range(0,10,2):
#     print(i)
# for i in range(10,0,-1):
#     print(i)
# num=5
# for i in range(1,11):
#     # print(num,"*",i,"=",num*i)
#     print(f"{num}*{i}={num*i}")
# sum=0
# for i in range(1,11):
#     if i%2==0:
#         sum+=i

# print(sum)
# num=[1,2,3,4,5,6,7]
# count=0
# sum=0
# for i in num:
#     if i%2==0:
#         sum+=i

#         count+=1
        
# print(count,sum)
# fact=1
# for i in range(1,6):
#     fact*=i
# print(fact)
# i=1
# while i<=5:
#     print(i)
#     i+=1
# num=1
# i=1
# while i<=10:
#     print(f"{num}*{i}={num*i}")
#     i+=1
# digit extraction
# num=5678
# while num>0:
#     digit=num%10
#     print(digit)
#     num=num//10
# num=5678
# sum=0
# while num>0:
#     digit=num%10
#     sum=digit+sum
#     num=num//10
#     print(sum)
# num=5678
# sum=0
# reverse=0
# while num>0:
#     digit=num%10
#     reverse=reverse*10+digit
#     # sum=digit+sum
#     num=num//10
#     print(reverse)
# num=5678
# sum=0
# reverse=0
# while num>0:
#     digit=num%10
#     reverse=reverse*10+digit
#     # sum=digit+sum
#     num=num//10
#     print(reverse)
# if reverse==num:
#     print("palindrome")
# else:
#     print("not")
# word="education"
# count=0
# for ch in word:
#     if ch in "aeiou":
#         count+=1
# print(count)
# word="Hello World"
# count=0
# for ch in word.lower():
#     if ch.isalpha() and ch not in "aeiou":
#         count=count+1
# print(count)
# word="banana"
# freq={}
# for ch in word:
#     freq[ch]=freq.get(ch,0)+1
# print(freq)
# num=[10,20,30,40,20,304]
# largest=num[0]
# for i in num:
#     if i > largest:
#         largest=num
# print(largest)
# smallest=num[0]
# for i in num:
#     if i < smallest:
#         smallest=num
# print(smallest)
# word="python"
# rev=""
# for ch in word:
#     rev=ch+rev
# print(rev)
# for i in range(1,101):
#     print(i)
# for i in range(1,101):
#     if i%2==0:
#         print(i)
# for i in range(0,101,2):
    
#     print(i)
# num=3
# sum=0
# for i in range(1,num):
#     sum+=num
# print(sum)

# text="python is tgh"
# words=text.split()
# result=""
# for word in words:
#     result=result+word[::-1]+" "
# result=result.strip().capitalize()
# print(result)
# for i in range(1,6):
#     if i==3:
#         break
#     print(i)
# nested loop
# for i in range(3):
#     for j in range(2):
#         print(i,j)
# for i in range(1,4):
#     for j in range(1,3):
#         print(i,j)
# num=7
# if num<=1:
#     print("not prime")
# else:
#     for i in range(2,num):
#         if num%2==0:
#             print("not prime")
#             break
#     else:
#         print("prime")
# text="hello world"
# for ch in text:
#     if ch==" ":
#         continue
#     print(ch)
text="hello123world"
count=0
for ch in text:
    if not ch.isdigit():
        continue
    count+=1
print(count)