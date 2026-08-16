# recurion
# def countDown(n):
#     if n==0:
#         return
#     print(n)
#     countDown(n-1)
# countDown(5)
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))
def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)
print(sum(5))