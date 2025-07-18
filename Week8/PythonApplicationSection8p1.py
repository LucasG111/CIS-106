# Employee base class
class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def get_bonus(self):
        return self.salary * 0.10

# Manager derived class
class Manager(Employee):
    def get_bonus(self):
        return self.salary * 0.20

    def long_term_bonus(self):
        return self.salary * 0.50

# Ask user to enter employee info
print("Employee Info")
first = input("Enter first name: ")
last = input("Enter last name: ")
salary = float(input("Enter annual salary: "))
emp = Employee(first, last, salary)

print("\nEmployee Details:")
print("Name:", emp.first, emp.last)
print("Salary:", emp.salary)
print("Bonus (10%):", emp.get_bonus())

# Ask user to enter manager info
print("\nManager Info")
first = input("Enter manager's first name: ")
last = input("Enter manager's last name: ")
salary = float(input("Enter annual salary: "))
mgr = Manager(first, last, salary)

print("\nManager Details:")
print("Name:", mgr.first, mgr.last)
print("Salary:", mgr.salary)
print("Bonus (20%):", mgr.get_bonus())
print("Long-term Bonus (50%):", mgr.long_term_bonus())