class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def View(self):
        return f"pracownik \t{self.name} wiek \t{self.age} wynagrodzenie \t{self.salary}"
