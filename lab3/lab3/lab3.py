# class Pojazd:
#     def __init__(self, marka):
#         self.marka = marka
#     def opis(self):
#         return f"pojazd marki {self.marka}"
#
# class Samochod(Pojazd):
#     def __init__(self, marka, model, rok):
#         super().__init__(marka)
#
#         self.model = model
#         self.rok = rok #constructor
#
#     def opis(self):
#         return f"samochod   {self.marka} {self.rok} {self.model}"
#
#
#
# #twozenie obiektu
# samochod1 = Samochod("marka1", "model1", 1990)
# print(samochod1.opis())
from abc import ABC, abstractmethod

# class Zwierze(ABC):#abstract class
#     @abstractmethod
#     def dzwiek(self):
#         pass
# class Lew(Zwierze):
#     def dzwiek(self):
#         return f"lew wydaje glos"
#
# lew1 = Lew()
# print(lew1.dzwiek())

#ZAD1