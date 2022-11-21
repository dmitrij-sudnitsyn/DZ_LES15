# Создать базовый класс Фигура с методом для подсчета 
# площади. Создать производные классы: прямоугольник, 
# круг, прямоугольный треугольник, трапеция со своими 
# методами для подсчета площади.
from Figure import *

myRegTangle=RegTangle("Квадрат",4,4)
print(myRegTangle)
myRegTangle.set("Квадрат",6,6)
print(myRegTangle)
myRegTangle.set("Прямоугольник",6,10)
print(myRegTangle)