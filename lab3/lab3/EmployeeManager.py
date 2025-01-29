

from Employee import Employee



class EmployeeManager:
    def __init__(self, listOfWorkers):

        self.listOfWorkers = listOfWorkers

    def addNew(self, name, age, salary):

        self.listOfWorkers.append(Employee(name, age, salary))
    def showEmpl(self):
        return self.listOfWorkers
    def elimWork(self, startAge, endAge):
        for i in self.listOfWorkers:
            if i.age >= startAge or i.age <= endAge:
                self.listOfWorkers.remove(i)
listOfWorkers = []
emplManager = EmployeeManager(listOfWorkers)
emplManager.showEmpl()
emplManager.addNew("work1", 25, 2550)
emplManager.showEmpl()