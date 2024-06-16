#Name: Irhan Iftikar
#Date: June 2024
#Description: Simple program that represents an introduction to object-oriented programming in Python
#Source: Followed the following playlist link - https://youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&si=S_QsGzy4mxbQEaQL

#Defines a class called "Employee" relating to information about an employee
class Employee:

    #Defines class variables that apply to the entire Employee class, unless overwritten by specific instance variable
    num_of_employees = 0
    company_employed_at = "The Great Company"
    yearly_raise = 1.04

    #Function initializes (shown by 'init') the Employee class with entry parameters. "Self" is included as the first parameter relating to any specific instance of the class.
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + "." + last + "@company.com"
        Employee.num_of_employees += 1

    #Defines a regular method 'full_name' of Employee class that returns the full name of any one employee. Only takes self as parameter.
    #Uses property decorator so when full_name is called, parentheses aren't needed (calls full_name instead of full_name() )
    @property
    def full_name(self):
        return("{} {}".format(self.first, self.last))
    
    #Another regular method of Employee class that applies a yearly raise and saves it to the employee's salary
    def apply_raise(self):
        self.salary = int(self.salary * self.yearly_raise)

    #Defines a class method that defines or redefines a class variable, in this case, yearly raise. Convention is first parameter taken is 'cls'
    @classmethod #Uses class method decorator
    def set_yearly_raise(cls, yearly_raise):
        cls.yearly_raise = yearly_raise

    #Another class method that allows an employee to be inputted from user as one string rather than individual parameters
    @classmethod
    def input_from_string(cls, employee_string):
        first, last, pay = employee_string.split("-")
        return cls(first, last, pay)
    
    #Defines a static method - is similar to a class method as both belong to the entire class, but doesn't take any keyword parameters
    #Static method that finds out if a day is a workday
    @staticmethod #Static method decorator
    def is_workday(day): 
        if day == "Saturday" or day == "Sunday":
            return("{} is not a workday.".format(day))
        else:
            return("{} is a workday.".format(day))
    
    #Method that returns a printable representation of an object - included as a conventional standard for debugging
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.salary)
    
    #Method that represents a class object as a string - included as a conventional standard for string representation
    def __str__(self):
        return "{} - {}".format(self.full_name, self.email)

#Defines a subclass "Manager" that inherits from class "Employee"  
class Manager(Employee):  

    #Class variable specific to Manager class
    yearly_raise = 1.10

    #Initializes the Manager class - adds in the parameter of college to Manager subclass not included in Employee class
    def __init__(self, first, last, salary, college): 
        super().__init__(first, last, salary)  #Passes parameters of first, last, and salary to the init method of Employee class (inheritance)
        self.college = college

#Defines a subclass "CEO" that inherits from class "Employee"
class CEO(Employee):

    #Class variable specific to CEO class
    yearly_raise = 1.50

    def __init__(self, first, last, salary, college, employees = None): 
        super().__init__(first, last, salary) #Inheritance to the Employee class
        self.college = college
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee): #Regular method that adds an employee to those that the CEO oversees
        if employee not in self.employees:
            self.employees.append(employee)

    def print_employees(self):        #Regular method that prints the employees that the CEO oversees
        for employee in self.employees:
            print("Employee: ", employee.full_name)

#Defines instances of classes Employee, Manager, and CEO. Doesn't need to include "self" as a parameter as it is automatically passed
employee_1 = Employee("Mark", "Roberts", 100)
employee_2 = Employee.input_from_string("Adam-Smith-150")
manager_1 = Manager("John", "Doe", 200, "Duke") 
ceo = CEO("Big", "Boss", 500, "Harvard", [employee_1, employee_2])

#Example calls from the methods from the three classes
print(employee_2.__str__())
print(manager_1.full_name)
print(employee_2.full_name)
print("Number of employees :", Employee.num_of_employees)
print(Employee.is_workday("Tuesday"))
manager_1.apply_raise()             #Applies raise to manager_1 and then prints the updated salary
print(manager_1.salary)
print(ceo.college)
print(ceo.email)
ceo.print_employees()
print(issubclass(CEO, Employee))    #Asks if class CEO is a subclass of class Employee (True)
Employee.set_yearly_raise(1.06)     #Redefines class variable of yearly_raise to 1.06 by calling on class method
employee_1.apply_raise()            
print(employee_1.salary)