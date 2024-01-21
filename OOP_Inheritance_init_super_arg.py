#Simple (Single) Inheritance with __init__ and Arguments
class ParentClass:
    def __init__(self, parent_attr):
        self.parent_attr = parent_attr
        print("ParentClass constructor with", parent_attr)

    def method_parent(self):
        print("Method of Parent Class")

class ChildClass(ParentClass):
    def __init__(self, parent_attr, child_attr):
        super().__init__(parent_attr)  # Pass arguments to the constructor of ParentClass
        self.child_attr = child_attr
        print("ChildClass constructor with", child_attr)

    def method_child(self):
        print("Method of Child Class")

# Example Usage
child = ChildClass('parent_attr_value', 'child_attr_value')
print('')

###########################################################################################
#Multi-Level Inheritance with __init__ and Arguments
class GrandParentClass:
    def __init__(self, grandparent_attr):
        self.grandparent_attr = grandparent_attr
        print("GrandParentClass constructor with", grandparent_attr)

    def method_grandparent(self):
        print("Method of Grandparent Class")

class ParentClass(GrandParentClass):
    def __init__(self, grandparent_attr, parent_attr):
        super().__init__(grandparent_attr)  # Pass arguments to the constructor of GrandParentClass
        self.parent_attr = parent_attr
        print("ParentClass constructor with", parent_attr)

    def method_parent(self):
        print("Method of Parent Class")

class ChildClass(ParentClass):
    def __init__(self, grandparent_attr, parent_attr, child_attr):
        super().__init__(grandparent_attr, parent_attr)  # Pass arguments to the constructor of ParentClass
        self.child_attr = child_attr
        print("ChildClass constructor with", child_attr)

    def method_child(self):
        print("Method of Child Class")

# Example Usage
child = ChildClass('grandparent_attr_value', 'parent_attr_value', 'child_attr_value')
print('')

#########################################################################################################
#Multiple Inheritance with __init__ and Arguments
class FatherClass:
    def __init__(self, father_attr):
        self.father_attr = father_attr
        print("FatherClass constructor with", father_attr)

    def method_father(self):
        print("Method of Father Class")

class MotherClass:
    def __init__(self, mother_attr):
        self.mother_attr = mother_attr
        print("MotherClass constructor with", mother_attr)

    def method_mother(self):
        print("Method of Mother Class")

class ChildClass(FatherClass, MotherClass):
    def __init__(self, father_attr, mother_attr, child_attr):
        FatherClass.__init__(self, father_attr)  # Pass arguments to FatherClass constructor
        MotherClass.__init__(self, mother_attr)  # Pass arguments to MotherClass constructor
        self.child_attr = child_attr
        print("ChildClass constructor with", child_attr)

    def method_child(self):
        print("Method of Child Class")

# Example Usage
child = ChildClass('father_attr_value', 'mother_attr_value', 'child_attr_value')
print('')

#######################################################################################################
#Hierarchical Inheritance with __init__ and Arguments
class ParentClass:
    def __init__(self, parent_attr):
        self.parent_attr = parent_attr
        print("ParentClass constructor with", parent_attr)

    def method_parent(self):
        print("Method of Parent Class")

class FirstChildClass(ParentClass):
    def __init__(self, parent_attr, first_child_attr):
        super().__init__(parent_attr)  # Pass arguments to the constructor of ParentClass
        self.first_child_attr = first_child_attr
        print("FirstChildClass constructor with", first_child_attr)

    def method_first_child(self):
        print("Method of First Child Class")

class SecondChildClass(ParentClass):
    def __init__(self, parent_attr, second_child_attr):
        super().__init__(parent_attr)  # Pass arguments to the constructor of ParentClass
        self.second_child_attr = second_child_attr
        print("SecondChildClass constructor with", second_child_attr)

    def method_second_child(self):
        print("Method of Second Child Class")

# Example Usage
first_child = FirstChildClass('parent_attr_value', 'first_child_attr_value')
second_child = SecondChildClass('parent_attr_value', 'second_child_attr_value')

