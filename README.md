# sudoku

(Scroll down for english description)

1. Генерируется судоку, имеющее одно решение (gen.py)
2. На кнопку пробел судоку решается (solver.py)

1.1) Создаие случайного судоку

![image](https://user-images.githubusercontent.com/111375726/210331501-26d7f73b-62f2-4ba3-a323-d55d7076c88d.png)

1.2) Алгоритм генерации случайной сетки (gen.py GridGenerator)
  * Создается базовая сетка (init_grid())
    ![image](https://user-images.githubusercontent.com/111375726/210332466-6a3dc400-b61a-4fc0-91bf-6e794d08c766.png)
  
  * Базовая сетка перемешивается по определенным правилам (shuffle) - поменять соседние районы (3 идущих подряд квадрата 3x3 вертикально или горизонтально) (swap_box_h(), swap_box_v()), поменять строки из одного района (swap_rows), поменять столбцы из одного района (swap_cols)
    ![image](https://user-images.githubusercontent.com/111375726/210333908-55af0942-b81d-4c0b-9f2e-9bba9ea5c6ab.png)
