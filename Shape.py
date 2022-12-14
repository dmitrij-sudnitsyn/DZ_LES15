# Создайте базовый класс Shape для рисования плоских
# фигур.
# Определите методы:
# ■■ Show() — вывод на экран информации о фигуре;
# ■■ Save() — сохранение фигуры в файл;
# ■■ Load() — считывание фигуры из файла.

class shape:
 def __init__(self,name,a,b) -> None:
   self.name=name
   self.a=a
   self.b=b

 def show(self):
   print(f"show Фигура {self.name} {self.a} {self.b}")

 def save(self):
   with open("figura.txt","w") as f:
    f.write(f"Фигура {self.name} {self.a} {self.b}")

    # print(f"Фигура {self.name} {self.a} {self.b}")

 def load(self):
   with open("figura.txt","r") as f:
    return f.readlines()

#   Определите производные классы:
# ■■ Square — квадрат, который характеризуется коорди-
# натами левого верхнего угла и длиной стороны;


# ■■ Rectangle — прямоугольник с заданными координа-
# тами верхнего левого угла и размерами;

class Rectangle(shape):
  def __init__(self, name, a, b) -> None:
    super().__init__(name, a, b)
  def show(self):
    print(f"show Фигура {self.name} {self.a} {self.b}")
       
# ■■Circle — окружность с заданными координатами цен-
# тра и радиусом;
# ■■ Ellipse — эллипс с заданными координатами верхнего
# угла описанного вокруг него прямоугольника со сто-
# ронами, параллельными осям координат, и размерами
# этого прямоугольника.
# Создайте список фигур, сохраните фигуры в файл,
# загрузите в другой список и отобразите информацию о
# каждой из фигур.
# Домашнее задание  

   