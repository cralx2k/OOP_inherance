#Simple (Single) Inheritance with Global and Local Variables
# Global variable
global_variable = "I am global"

class ParentClass:
    def __init__(self, parent_attr):
        self.parent_attr = parent_attr
        print("ParentClass constructor with", parent_attr)

    def method_parent(self, local_variable):
        print("Method of Parent Class. Global:", global_variable, "Local:", local_variable)

class ChildClass(ParentClass):
    def __init__(self, parent_attr, child_attr):
        super().__init__(parent_attr)
        self.child_attr = child_attr
        print("ChildClass constructor with", child_attr)

    def method_child(self, local_variable):
        print("Method of Child Class. Global:", global_variable, "Local:", local_variable)

# Example Usage
child = ChildClass('parent_attr_value', 'child_attr_value')
child.method_parent('local_to_parent')
child.method_child('local_to_child')
print('')

####################################################################################
#Multi-Level Inheritance with Global and Local Variables
# Global variable
global_variable = "I am global"

class GrandParentClass:
    def __init__(self, grandparent_attr):
        self.grandparent_attr = grandparent_attr
        print("GrandParentClass constructor with", grandparent_attr)

    def method_grandparent(self, local_variable):
        print("Method of Grandparent Class. Global:", global_variable, "Local:", local_variable)

class ParentClass(GrandParentClass):
    def __init__(self, grandparent_attr, parent_attr):
        super().__init__(grandparent_attr)
        self.parent_attr = parent_attr
        print("ParentClass constructor with", parent_attr)

    def method_parent(self, local_variable):
        print("Method of Parent Class. Global:", global_variable, "Local:", local_variable)

class ChildClass(ParentClass):
    def __init__(self, grandparent_attr, parent_attr, child_attr):
        super().__init__(grandparent_attr, parent_attr)
        self.child_attr = child_attr
        print("ChildClass constructor with", child_attr)

    def method_child(self, local_variable):
        print("Method of Child Class. Global:", global_variable, "Local:", local_variable)

# Example Usage
child = ChildClass('grandparent_attr_value', 'parent_attr_value', 'child_attr_value')
child.method_grandparent('local_to_grandparent')
child.method_parent('local_to_parent')
child.method_child('local_to_child')
print("")

#######################################################################################
#Multiple Inheritance with Global and Local Variables
# Global variable
global_variable = "I am global"

class FatherClass:
    def __init__(self, father_attr):
        self.father_attr = father_attr
        print("FatherClass constructor with", father_attr)

    def method_father(self, local_variable):
        print("Method of Father Class. Global:", global_variable, "Local:", local_variable)

class MotherClass:
    def __init__(self, mother_attr):
        self.mother_attr = mother_attr
        print("MotherClass constructor with", mother_attr)

    def method_mother(self, local_variable):
        print("Method of Mother Class. Global:", global_variable, "Local:", local_variable)

class ChildClass(FatherClass, MotherClass):
    def __init__(self, father_attr, mother_attr, child_attr):
        FatherClass.__init__(self, father_attr)
        MotherClass.__init__(self, mother_attr)
        self.child_attr = child_attr
        print("ChildClass constructor with", child_attr)

    def method_child(self, local_variable):
        print("Method of Child Class. Global:", global_variable, "Local:", local_variable)

# Example Usage
child = ChildClass('father_attr_value', 'mother_attr_value', 'child_attr_value')
child.method_father('local_to_father')
child.method_mother('local_to_mother')
child.method_child('local_to_child')
print('')

###########################################################################################
#Hierarchical Inheritance with Global and Local Variables
# Global variable
global_variable = "I am global"

class ParentClass:
    def __init__(self, parent_attr):
        self.parent_attr = parent_attr
        print("ParentClass constructor with", parent_attr)

    def method_parent(self, local_variable):
        print("Method of Parent Class. Global:", global_variable, "Local:", local_variable)

class FirstChildClass(ParentClass):
    def __init__(self, parent_attr, first_child_attr):
        super().__init__(parent_attr)
        self.first_child_attr = first_child_attr
        print("FirstChildClass constructor with", first_child_attr)

    def method_first_child(self, local_variable):
        print("Method of First Child Class. Global:", global_variable, "Local:", local_variable)

class SecondChildClass(ParentClass):
    def __init__(self, parent_attr, second_child_attr):
        super().__init__(parent_attr)
        self.second_child_attr = second_child_attr
        print("SecondChildClass constructor with", second_child_attr)

    def method_second_child(self, local_variable):
        print("Method of Second Child Class. Global:", global_variable, "Local:", local_variable)

# Example Usage
first_child = FirstChildClass('parent_attr_value', 'first_child_attr_value')
second_child = SecondChildClass('parent_attr_value', 'second_child_attr_value')
first_child.method_parent('local_to_parent')
first_child.method_first_child('local_to_first_child')
second_child.method_second_child('local_to_second_child')
