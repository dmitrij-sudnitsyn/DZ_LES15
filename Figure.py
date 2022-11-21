class Figure:
 def __ini__(self,name):
    self.name=name

 def getName(self):
    return self.name   

 def setName(self,name):
    self.name=name

 def get_square(self):
    return 0   

 def __str__(self) -> str:
    return f"Фигура {self.name}; ч площадью: {self.get_square()}"       

class RegTangle(Figure):
   pass    


  