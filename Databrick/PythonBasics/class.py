"""
--------------------------------BASICS--------------------------------
Class 
-> CLass is a blueprint for creating objects -> ? attributes, methods

Why is self needed?
It lets you access and modify the attributes and methods of the current object.
Without self, the method would not know which object’s data you are trying to access or modify.

----------------------------------------------------------------------
"""

class demo:
    schoolName = "KV"         # class variable ( common for objects)

    def __init__(self,name):  # constructor
        self.name = name      # assigning the attribute to the objects
        self.schoolName = "NotreDam"
    
    def name_print(self):     # method
        print(f"\nSchool Name : {demo.schoolName}")   # calling class Variable
        print(f"\nName : {self.name}",end="\n\n")     # calling object Variables
 
    def whatisyourName(self):
        print("\nWelcome.")
        self.name_print()      # calling one method from another method

if __name__ == "__main__":
    myName = demo("Lakshman")  # myName is the object
    myName.whatisyourName()


# example 2 


class Person:
    schoolName = "KV"
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"\nName : {self.name}")


class student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def display(self):
        super().display()
        print(f"Student id : {self.student_id}")
        print(f"School Name : {super().schoolName}")

s1 = student("Ram", 90)
s1.display()

s2 = Person("Lakshman")
s2.display()





