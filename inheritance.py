# %%
abs(-1*22.3)
ascii('a>>>')

# %%
# single inheritance
class parent:
    def __init__(self):
        print('parent')
        

class child(parent):
    def __init__(self):
        print('child')
        parent.__init__(self)
        #super.__init__(self)
        

obj=parent()
obj1=child()


# %%
# multilevel inheritance

class parent:
    def __init__(self):
        print('parent')
        

class son(parent):
    def __init__(self):
        print('child')
        parent.__init__(self)


class grandson(son):
    def __init__(self):
        print('grandson')
        son.__init__(self)
        

obj1=grandson()


# %%
#hierarchical inheritance

class parent:
    def __init__(self):
        print('parent')
        

class child1(parent):
    def __init__(self):
        print('child 1')
        parent.__init__(self)
        #super.__init__(self)

class child2(parent):
    def __init__(self):
        print('child 2')
        parent.__init__(self)
        #super.__init__(self)
        


obj1=child1()
obj2=child2()



# %%

class parent:BoxesA[:,0],BoxesB[:,0]2')
        parent.__init__(self)
        #super.__init__(self)
        


obj1=child1()
obj2=child2()
obj11=grandson1()


# %%
''' class parent:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print(x+y)
        
    def __init__(self):
        print('parent')
    

class child(parent):
    def __init__(self):
        print('child')
        

obj=parent(10,20)
obj1=child()
 '''


class parent:

    def __init__(self):
        print('parent')
        
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print(x+y)
        
    
    

class child(parent):
    def __init__(self):
        print('child')
        

obj=parent(10,20)
obj1=child()


# %%
class person():
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name,self.id)

class emp(person):
    def print(self):
        print("Emp class called")

emp_details=emp("yuva",102)
emp_details1=person("raj",101)
try:
    emp_details.print()
    emp_details1.print()

    emp_details.display()
    emp_details1.display()
except:
    print("no attribute error")


# %%
# Python program to demonstrate
# hybrid inheritance


class School:
	def func1(self):
		print("This function is in school.")


class Student1(School):
	def func2(self):
		print("This function is in student 1. ")


class Student2(School):
	def func3(self):
		print("This function is in student 2.")


class Student3(Student1,Student2,School):
	def func4(self):
		print("This function is in student 3.")


# Driver's code
object = Student3()
object.func1()
object.func2()
object.func3()


# %%



