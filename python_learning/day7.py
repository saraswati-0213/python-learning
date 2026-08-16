# numbers=(1,2,3,4)
# print(type(numbers))
# print(numbers[2])
# print(numbers[0:2])
# numbers[0]=100
# print(numbers) it cant add because of immutable
# t=(1,2,3)

# t=t+(4,)
# print(t) new crete
# s=(1,2,3,4,5,5)
# print(s.count(5))
# print(s.index(2))
# print(3 in s)
# print(len(s))
# print(min(s))
# print(max(s))
# tuple packing
# name="diksha"
# age=21
# course="btech"
# student=course,age,name
# print(student)
##### set
# skills={"python","django","html"}
# skills.add("js")
# print(skills)
# skills.update(["sql","git"])
# print(skills)
# skills.remove("python")
# print(skills)
# skills.discard("js")
# print(skills)
# a={1,2,3}
# b={1,2,5,6,7}
# result= sorted(b)
# print(b)
# print(a.union(b))

# b=a.copy()
# b.add(4)
# print(a,b)
# SET COMPREHNSION
# sqaure={x*x for x in range(5)}
# print(sqaure)
# s={1,2}
# x=s.add(3)
# print(x)
# print(s)
# questions
# nums=[10,20,10,20,30,40,30]
# freq={}
# for num in nums:
#     freq[num]=freq.get(num,0)+1
# print(freq)
# unique=list(set(nums))
# print(unique)
# print(len(set((nums))))
# word="banana"
# freq={}
# for ch in word:
#     freq[ch]=freq.get(ch,0)+1
# print(freq)
swntence="python java python java python java"
word=swntence.split()
freq={}
for wor in word:
    freq[wor]=freq.get(wor,0)+1
print(freq)

    

print(word)
