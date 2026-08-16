# print("*",end="")
# print("*",end="")
# print("*",end="")
# ****
# ****
# ****
# ****
# n=4
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print()
# #################rectaangle
# n=3
# m=5
# for i in range(3):
#     for j in range(5):
#         print("*",end="")
#     print()
################ traingle
# num=5
# for i in range(1,num+1):
#     for j in range(i):
#         print("*",end="")
#     print()
# n=5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()    
# 1
# 22
# 333 
# 4444
# 55555    
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end="")
#     print()
# 1
# 12
# 123
# 1234
# n=4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# revse
# n=5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# 1
# 21
# 321
# 4321
# n=4
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()
# 1
# 23
# 456
# 78910
# n=5
# num=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(65+j),end="")
#     print()
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(i+64),end="")
#     print()
# n=5
# for row in range(1,n+1):
#     for space in range(n-row):
#         print(" ",end=" ")
#     for star in range(row):
#         print("*",end=" ")
#     print()
# n=5
# for i in range(1,n+1):
#     for star in range(n-i+1):
#         print("*",end=" ")
#     for space in range(i-1):
#         print(" ",end=" ")
#     print()
# n=5
# for i in range(1,n+1):
#     for space in range(i-1):
#             print(" ",end=" ")
#     for star in range(n-i+1):
#         print("*",end=" ")
    
    # print()
# pyraminf half
n=5
for row in range(1,n+1):
    for space in range(n-row):
        print(" ",end=" ")
    for star in range(2*row-1):
        print("*",end=" ")
    print()
for row in range(n-1,0,-1):
    for space in range(row-1):
        print(" ",end=" ")
    for star in range(2*(n-row)+1):
        print("*",end=" ")
    print()

                                      
