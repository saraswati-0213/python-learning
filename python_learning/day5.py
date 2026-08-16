# # STRING
# name="saraswati tanwar"
# father_name='moolchand'
# mother_name="""rakesh"""
# print(type(name))
# print(name[0])
# print(father_name[3])
# print(mother_name[-3])
# print(len(name))
# print(name[len(name)-1])
# print(father_name[0:5])
# print(mother_name[:3])
# print(name[2:])
# print(name[:])
# print(father_name[0:100])
# print(father_name[0:7:2])
# print(name[::-1])
# s="ABCDEFG"
# print(s[5:1:-2])
# s="python"
# print(s[0],s[-1],s[::-1])
# if s==s[::-1]:
#     print("palindrome")
# else:
#     print('not')
# print(s[1:])
# print(s[:-1])
# print(s[1:-1])
# s="python"
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.capitalize())
# v="YshiYHK"
# print(v.swapcase())
# print(v.casefold())
# u="   diksha    "
# print(u.strip())
# print(u.lstrip)
# print(u.lstrip)
# n="$$$$$diksha"
# print(n.strip("$"))
# b="python is my fav lang"
# print(b.replace("python","java"))
# s="cat cat cat"
# print(s.replace("cat","dog",2))
# print(s.split("$"))
# print(b.split(" ","-"))
# w="python-django-java-html"
# print(w.split("-",2))
# print("".join(w))
# print(w.find("yt"))
# print(w.index("py"))
# print(w.count("o"))
# s="banana"
# print(s.find("a"))
# print(s.rfind("a"))
# word="python"
# print(word[0].lower() in "iaeou")
# print(word[1].lower() in "iaeou")
# print(word[2].lower() in "iaeou")
# print(word[3].lower() in "iaeou")
# print(word[4].lower() in "iaeou")
# print(word[5].lower() in "iaeou")
# s="programming"
# print(s.count("r"))
# print(s.count("g"))
# print(s.count("m"))
word="   Madam".strip().lower()
if word==word[::-1]:
    print("palindrome")
else:
    print("not")


