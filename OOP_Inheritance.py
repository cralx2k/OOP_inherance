#Simple (Single) Inheritance
class ParentClass:
    def method_parent(self):
        print("Method of Parent Class")

class ChildClass(ParentClass):
    def method_child(self):
        print("Method of Child Class")

# Example Usage
child = ChildClass()
child.method_parent()  # Method of Parent Class
child.method_child()   # Method of Child Class
print("")

##############################################################
#Multi-Level Inheritance
class GrandParentClass:
    def method_grandparent(self):
        print("Method of Grandparent Class")

class ParentClass(GrandParentClass):
    def method_parent(self):
        print("Method of Parent Class")

class ChildClass(ParentClass):
    def method_child(self):
        print("Method of Child Class")

# Example Usage
child = ChildClass()
child.method_grandparent()  # Method of Grandparent Class
child.method_parent()       # Method of Parent Class
child.method_child()        # Method of Child Class
print("")


#############################################################
#Multiple Inheritance
class FatherClass:
    def method_father(self):
        print("Method of Father Class")

class MotherClass:
    def method_mother(self):
        print("Method of Mother Class")

class ChildClass(FatherClass, MotherClass):
    def method_child(self):
        print("Method of Child Class")

# Example Usage
child = ChildClass()
child.method_father()  # Method of Father Class
child.method_mother()  # Method of Mother Class
child.method_child()   # Method of Child Class
print("")

############################################################
#Hierarchical Inheritance
class ParentClass:
    def method_parent(self):
        print("Method of Parent Class")

class FirstChildClass(ParentClass):
    def method_first_child(self):
        print("Method of First Child Class")

class SecondChildClass(ParentClass):
    def method_second_child(self):
        print("Method of Second Child Class")

# Example Usage
first_child = FirstChildClass()
second_child = SecondChildClass()

first_child.method_parent()        # Method of Parent Class
first_child.method_first_child()   # Method of First Child Class

second_child.method_parent()       # Method of Parent Class
second_child.method_second_child() # Method of Second Child Class
