class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def annual_salary(self):
        return 12*self.salary
        
        
employee1=employee("Samirican",2341)
print("Your annual salary is ",employee1.annual_salary())
