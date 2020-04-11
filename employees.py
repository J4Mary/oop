class Employee:
    def __init__(self, name, surname, email, telephone, salary):
        self.name=name
        self.surname=surname
        self.email=email
        self.telephone=telephone
        self.salary=salary
    def work(self):
        return "I come to the office."
    def check_salary(self, days):
        return days*self.salary
    def __str__(self):
        return self.__class__.__name__+': '+self.name+' '+self.surname

    def __lt__(self, other):
        return self.salary<other.salary
    def __gt__(self, other):
        return self.salary > other.salary
    def __eq__(self, other):
        return self.salary == other.salary
    def __le__(self, other):
        return self.salary <= other.salary
    def __ge__(self, other):
        return self.salary >= other.salary
    def __ne__(self, other):
        return self.salary != other.salary

class Recruiter(Employee):
    def __init__(self, name, surname, email, telephone, salary, hired_this_month):
        super().__init__(name, surname, email, telephone, salary)
        self.hired_this_month=hired_this_month
    def work(self):
        string = super().work()
        return string[:-1] +" and start hiring"

class Programmer(Employee):
    def __init__(self, name, surname, email, telephone, salary, tech_stack, closed_this_month):
        super().__init__(name, surname, email, telephone, salary)
        self.tech_stack=tech_stack
        self.closed_this_month=closed_this_month
    def work(self):
        string=super().work()
        return string[:-1]+" and start coding"
    def __lt__(self, other):
        return len(self.tech_stack)<len(other.tech_stack)
    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)
    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)
    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)
    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)
    def __ne__(self, other):
        return len(self.tech_stack) != len(other.tech_stack)
    def __add__(self, other):
        return Programmer(self.name, self.surname, self.email, self.telephone, self.salary, list(set(self.tech_stack)|set(other.tech_stack)), self.closed_this_month+other.closed_this_month)

programmer1=Programmer("Mary","Grey","a@gmail.com","1234567890",100, ['Python','PHP','database','C++'], 3)
programmer2=Programmer("Max","Grey","m@gmail.com","1234567890",90, ['PHP','database','C++','JS'], 1)
print(programmer1.work())
print(programmer1.__str__())
print(programmer1<programmer2)
print(programmer1!=programmer2)
alfa=Programmer('Lera', 'Brown', 'l@gmail.com', '98765431', 120, [], 0)
alfa=alfa + programmer1 +programmer2
print(alfa.tech_stack)