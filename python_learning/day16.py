import re
# text="I Love Python"
# result=re.search("Python",text)
# print(text)
# if result:
#     print("found")
# else:
#     print("not found")
# text="cat cut cot"
# result=re.findall(r"c.t",text)
# print(result)
# text="apple banana"
# result=re.findall(r"[z]",text)
# print(text)
text="age 21,marks 63"
# result=re.findall(r"\d",text)
# print(result)
# result=re.findall(r"\D",text)
# print(result)
# result=re.findall(r"\w",text)
# print(result)
# result=re.findall(r"\W",text)
# print(result)
# result=re.findall(r"\s",text)
# print(result)
# result=re.findall(r"\S",text)
# print(result)
result=re.findall(r"ab*")
print(result)