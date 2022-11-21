class Figure:
 def __init__(self,name):
    self.name=name

 def getName(self):
    return self.name   

 def setName(self,name):
    self.name=name

 def getQuare(self):
    return 0   

 def __str__(self) -> str:
    return f"Фигура {self.name}; c площадью: {self.getQuare()}"       

class RegTangle(Figure):
  def __init__(self, name,a,b):
    self.a,self.b=a,b
    super().__init__(name)

  def set(self, name,a,b):
    self.a,self.b=a,b
    super().setName(name)
    

  def getStoronA(self):
     return self.a

  def getStoronB(self):
     return self.b

  def setStoronA(self,a):
    self.a=a

  def getStoronB(self,b):
    self.a=b

  def getQuare(self):  
     return self.a*self.b


  