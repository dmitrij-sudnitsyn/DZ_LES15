# Создать базовый класс Фигура с методом для подсчета 
# площади. Создать производные классы: прямоугольник, 
# круг, прямоугольный треугольник, трапеция со своими 
# методами для подсчета площади.
from Figure import *
from Shape import *

# myRegTangle=RegTangle("Квадрат",4,4)
# print(myRegTangle)
# myRegTangle.set("Квадрат",6,6)
# print(myRegTangle)

# myRegTangle.set("Прямоугольник",6,10)
# print(myRegTangle)
# b=int(myRegTangle)
# print(b)

# myRightTriangle=RightTriangle("Треугольник",60,40)
# print(myRightTriangle)
# b=int(myRightTriangle)
# print(b)

# mytrapetsiya=trapetsiya("Трапеция",60,40,40,40)
# print(mytrapetsiya)
# b=int(mytrapetsiya)
# print(b)
# 60 40 40 40  1936.49

# myCircle=Circle("Круг",10)
# print(myCircle)
# b=int(myCircle)
# print(b)

def myshape_fun():
  myshape= shape("Квадрат: ",10,60) 
  myshape.save()
  lst=myshape.load()
  print(lst)
  myshape.show()


myshape_fun()  

