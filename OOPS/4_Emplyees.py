class Employee:
    MIN_SALARY = 20000
    CURRENCY = "Rs"
    def __init__(self, name, _salary, _performance_rating = "Average"):
        self.name = name
        self._salary = _salary
        self._performance_rating = _performance_rating
        
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            print("Cant set salary to negative")
            return

        elif new_salary < Employee.MIN_SALARY:
            print(f"You cant give salart lesser than minimum salary: ({Employee.MIN_SALARY} {Employee.CURRENCY})")
            return

        self._salary = new_salary

    @property
    def rating(self):
        return self._performance_rating
    
    @rating.setter
    def rating(self, new_rating):
        if new_rating.capitalize() in ["Poor", "Average", "Excellent"]:
            self._performance_rating = new_rating.capitalize()
        else:
            print("Enter a valid rating")
            return
        
    def calculate_bonus(self):
        rating = self.rating
        salary = self.salary
        
        bonus_dict = {"Excellent":20,"Average":5,"Poor":0}
        
        bonus_pt = bonus_dict[rating]
        return(salary + (salary*bonus_pt)/100)

emp = Employee("Alex", 60000)
emp.salary = 15000
emp.salary = -500

emp.rating = "Excellent"
emp.rating = "Good"

print(emp.calculate_bonus())