#A Class is a "blueprint" for creating objects.
# Creating a class
class Dog():

    def __init__(self,name,age):
        #attributes
        self.name = name
        self.age = age

    #Adding method
    def bark(self):
        return("Woof")

    def speak(self,sound):
        return "{} says {}".format(self.name,sound)



#Instantiation of objects

Dog1 = Dog("Max",9)
# Dog2 = Dog("Tom",5)
Dog3 = Dog("Boxer",6)
# print(type(Dog1))
# #print(Dog1.animal_kind)
# # calling the methods
# print(Dog1.bark())
# print(Dog2.bark())
# # printing the attributes
#print(Dog1.name)
# print("{} is {} years old".format(Dog1.name,Dog1.age))
print(Dog3.speak("Hi"))


