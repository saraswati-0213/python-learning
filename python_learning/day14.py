# class student:   class
    # pass
# s1=student() object creation call
# class Student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def update_marks(self,new_marks)
#         self.mark=new_marks
# s1=Student("saraswati",21,90)
# print(s1.name)
# print(s1.marks)
# s2=Student.update_marks(70)
# print(s2.new)
# class BankAccount:
#     def __init__(self,balance):
#         self.balance=balance
#     def deposit(self,amount):
#         if amount<= 0:

#             raise "value must be positive"
#         self.balance+=amount
# account=BankAccount(1000)
# account.deposit(1000)
# print(account.balance)
        
# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length*self.width
# r1=Rectangle(10,5)
# result=r1.area()
# print(result)
# class variable/instance variable
# class Student:
# class varibale
#     school_name="ABC school" 
#     def __init__(self,name,marks):
#         self.name=name instance varible
#         self.marks=marks
# s1=Student("riya",90)
# print(s1.marks)
# print(s1.name)
# print(s1.school_name)
# object counting using class variable
# class Student:
#     count=0
#     def __init__(self,name):
#         self.name=name
#         Student.count+=1
# s1=Student("riya")
# s2=Student("khusi")
# s3=Student("ritila")
# print(Student.count)
        
# class Student:
#     school="ABC school"
#     @classmethod
#     def show_school(cls):
#         print(cls.school)
# Student.show_school()
# class Caculator:
#     @staticmethod
#     def add(a,b):
#         return a+b
# print(Caculator.add(3,5))
# class Student:
#     school="ABC school"
#     count=0
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         type(self).count+=1
#     def show_Details(self):
#         print("name:",self.name)
#         print("marks",self.marks)
#         print("school",self.school)
#     @classmethod
#     def change_school(cls,new_School):
#         cls.school=new_School
#     @classmethod
#     def total_student(cls):
#         return cls.count
#     @staticmethod
#     def valid_marks(marks):
#         return 0<=marks<=100
# s1=Student("rahul",30)
# s2=Student("riya",70)
# s1.show_Details()
# print(Student.total_student())
# Student.change_school("xyz School")
# print(s1.school)
# print(s2.school)
# print(Student.valid_marks(150))
# class employee:
#     def show(self):
#         print("am a employee")
# class developer(employee):
#     pass
# s=developer()
# s.show()
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Student(person):
#     def __init__(self, name, age,course):
#         super().__init__(name, age)
#         self.course=course
# s=Student("riya",21,"js")
# print(s.name)
# class Animal:
#     def sound(self):
#         print("animal sleeps")
# class dog(Animal):
#     def sound(self):
#         print("dog bark")
# d=dog()
# d.sound()overing

# class Animal:
#     def sound(self):
#         print("animal sleeps")
# class dog(Animal):
#     def sound(self):
#         super().sound()
#         print("dog bark")
# d=dog()
# d.sound()
# single omheritance-one parent/one child
# class Animal:
#     def eat(self):
#         print("eating")
# class dog(Animal):
#     def sound(self):
#         print("dog bark")
# d=dog()
# d.sound()
# d.eat()
# multilevel inheritance-grandparent/parent/child
# class person:
#     def show_person(self):
#         print("person")
# class employee(person):
#     def show_employee(self):
#         print("employee")
# class developer(employee):
#     def show_Developer(self):
#         print("developer")
# d=developer()
# d.show_Developer()
# d.show_employee()
# d.show_person()

# hierarchical-one parent/multiple child

# class Animal:
#     def sound(self):
#         print("animal sleeps")
# class dog(Animal):
#     def bark(self):
#         print("dog bark")
# class cat(Animal):
#     def meow(self):
#         print("meow")
# d=dog()
# c=cat()
# d.sound()
# c.meow()
# d.bark()

# multiple-multiple parents/one chils

# class Animal:
#     def sound(self):
#         print("animal sleeps")
# class lion:
#     def eat(self):
#         print("eating meat")
# class cat(Animal,lion):
#     def cute(self):
#         print("cute")
# d=cat()

# d.cute()
# d.eat()
# polymorpishm

# class cat:
#     def sound(self):
#         print("animal sleeps")
# class dog:
#     def sound(self):
#         print("dog bark")
# d=dog()
# c=cat()
# d.sound()
# c.sound()
# class Animal:
#     def sound(self):
#         print("animal sleeps")
# class dog(Animal):
#     def sound(self):
#         print("dog bark")
# class cat(Animal):
#     def sound(self):
#         print("meow")
# animals=[Animal(),dog(),cat()]
# for animal in animals:
#     print(animal.sound())
# print(len("python"))
# print(len(["a","A","B",1,2]))
# print(10+20)
# print("hello"+"python")
# class circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius*self.radius
# class rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         return self.length*self.breadth
# class sqaure:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return self.radius*self.radius
# areas=[circle(14),sqaure(4),rectangle(3,4)]
# for area in areas:
#     print(area.area())
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __str__(self):
        return f"{self.name}-{self.marks}"
s=student("diksja",78)
print(s)