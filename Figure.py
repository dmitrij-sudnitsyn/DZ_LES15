class Figure:
 def __init__(self,name):
    self.name=name
    self.guare=0

 def getName(self):
    return self.name   

 def setName(self,name):
    self.name=name

 def getQuare(self):
    return self.guare

 def __str__(self) -> str:
    return f"Фигура {self.name}; c площадью: {self.getQuare()}"       

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
     return self.guare


  