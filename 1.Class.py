# Basic Class Example
class Employee():
    EmpCount = 0

    def __init__ (self, name, id):
        self.name = name
        self.id = id
        Employee.EmpCount = Employee.EmpCount + 1

    def NumberOfEmployees (self):
        print ("Number of employees: " + str (Employee.EmpCount))


    def Display (self):
        print ("Name of the employee is: " + self.name)
        print ("ID of the employee is: " + str (self.id))

JaffaEm = Employee ("Jaffa", 8988)
JaffaEm.Display()
DaffaEm = Employee ("Daffa", 564500)
DaffaEm.Display()
DaffaEm.NumberOfEmployees()
print (JaffaEm.EmpCount)
