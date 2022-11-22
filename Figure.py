import math
class Figure:
 def __init__(self,name):
    self.name=name
    self.guare=0

 def getName(self):
    return self.name   

 def setName(self,name):
    self.name=name


 def getQuare(self):
    self.guare=0
    return self.guare

 def __str__(self) -> str:
    return f"Фигура {self.name}; c площадью: {self.getQuare()}"       


# Класс прямоугольник
class RegTangle(Figure):
  def __init__(self, name,a,b):
    self.a,self.b=a,b
    self.guare=a*b
    super().__init__(name)

#  Переопределяем вывод данных по прямоугольнику   
  def __str__(self) -> str:
    return f"Фигура {self.name};  со сторонами {self.getStoronA()}Х{self.getStoronA()} имеет площадь площадью: {self.getQuare()}"       

  def __int__(self):
   try:
    return int(self.guare)
   except ValueError:
    return print(f"Значение {self.guare} не численное")

  def set(self, name,a,b):
    self.a,self.b=a,b
    self.guare=a*b
    super().setName(name)
    

  def getStoronA(self):
     return self.a

  def getStoronB(self):
     return self.b

  def setStoronA(self,a):
    self.a=a
    super().guare=a*self.b

  def getStoronB(self,b):
    self.a=b
    super().guare=self.a*b


  def getQuare(self):  
     self.guare=self.a*self.b
     return self.guare

# Класс круг
class Circle(Figure):
  def __init__(self, name,r):
   self.r=r
   super().__init__(name)     
 
  def __str__(self) -> str:
   return f"Фигура {self.name};  с радиусом {self.r} имеет площадь площадью: {self.getQuare()}" 

  def __int__(self):
   try:
    return int(self.guare)
   except ValueError:
    return print(f"Значение {self.guare} не численное")

 
  def set(self,name,r):
   self.r=r
   super().__init__(name) 

  def getR(self):
   return self.r

  def setR(self,r):
   self.r=r
   
  def getQuare(self):  
     self.guare=3.13*self.r*self.r
     return self.guare

# Класс прямоугольный треугольник
class RightTriangle(RegTangle):
   def __init__(self, name, a, b):
     super().__init__(name, a, b)

   def __str__(self) -> str:
     return f"Фигура {self.name};  с длиной катетом А {self.getStoronA()} и катетом {self.getStoronA()} имеет площадь площадью: {self.getQuare()}"       

   def __int__(self):
     return super().__int__()  

   def getQuare(self):  
     self.guare=self.a*self.b/2
     return self.guare
   

class trapetsiya(RegTangle):   
   def __init__(self, name, a, b,d,c):
     self.c=c
     self.d=d     
     super().__init__(name, a, b)
     p=(self.a+self.b+self.c+self.d)/2
     sa=(self.a+self.b)/(abs(self.a-self.b))
     sb=math.sqrt((p-self.a)*(p-self.b)*(p-self.a-self.c)*(p-self.a-self.b))
     self.guare=sa*sb


   def getA(self):
    return self.a

   def getB(self):
    return self.b

   def getC(self):
    return self.c

   def getD(self):
    return self.d

   def getQuare(self):
    #  формула Герона
    p=(self.a+self.b+self.c+self.d)/2
    sa=(self.a+self.b)/(abs(self.a-self.b))
    sb=math.sqrt((p-self.a)*(p-self.b)*(p-self.a-self.c)*(p-self.a-self.b))
    self.guare=sa*sb
    return self.guare

   def __str__(self) -> str:
     return f"Фигура {self.name};  с длиной сторон {self.getA()} , {self.getB()} , {self.getD()} , {self.getC()} имеет площадь площадью: {self.getQuare()}"    

   def __int__(self):
     return super().__int__()  
     

     



  