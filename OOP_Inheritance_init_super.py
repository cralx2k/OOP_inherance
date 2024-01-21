#Simple (Single) Inheritance with __init__
class ParentClass:
    def __init__(self):
        print("ParentClass constructor")

    def method_parent(self):
        print("Method of Parent Class")

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()  # Call the constructor of ParentClass
        print("ChildClass constructor")

    def method_child(self):
        print("Method of Child Class")

# Example Usage
child = ChildClass()
print('')

#####################################################################
#Multi-Level Inheritance with __init__
class GrandParentClass:
    def __init__(self):
        print("GrandParentClass constructor")

    def method_grandparent(self):
        print("Method of Grandparent Class")

class ParentClass(GrandParentClass):
    def __init__(self):
        super().__init__()  # Call the constructor of GrandParentClass
        print("ParentClass constructor")

    def method_parent(self):
        print("Method of Parent Class")

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()  # Call the constructor of ParentClass
        print("ChildClass constructor")

    def method_child(self):
        print("Method of Child Class")

# Example Usage
child = ChildClass()
print("")


#######################################################################
#Multiple Inheritance with __init__
class FatherClass:
    def __init__(self):
        print("FatherClass constructor")

    def method_father(self):
        print("Method of Father Class")

class MotherClass:
    def __init__(self):
        print("MotherClass constructor")

    def method_mother(self):
        print("Method of Mother Class")

class ChildClass(FatherClass, MotherClass):
    def __init__(self):
        FatherClass.__init__(self)  # Explicitly call FatherClass constructor
        MotherClass.__init__(self)  # Explicitly call MotherClass constructor
        print("ChildClass constructor")

    def method_child(self):
        print("Method of Child Class")

# Example Usage
child = ChildClass()
print("")

#####################################################################
#Hierarchical Inheritance with __init__
class ParentClass:
    def __init__(self):
        print("ParentClass constructor")

    def method_parent(self):
        print("Method of Parent Class")

class FirstChildClass(ParentClass):
    def __init__(self):
        super().__init__()  # Call the constructor of ParentClass
        print("FirstChildClass constructor")

    def method_first_child(self):
        print("Method of First Child Class")

class SecondChildClass(ParentClass):
    def __init__(self):
        super().__init__()  # Call the constructor of ParentClass
        print("SecondChildClass constructor")

    def method_second_child(self):
        print("Method of Second Child Class")

# Example Usage
first_child = FirstChildClass()
second_child = SecondChildClass()














