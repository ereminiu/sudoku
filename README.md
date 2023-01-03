# sudoku

1) Создание Судоку

![image](https://user-images.githubusercontent.com/111375726/210331501-26d7f73b-62f2-4ba3-a323-d55d7076c88d.png)

Алгоритм генерации случайной сетки (gen.py GridGenerator)
  * Создается базовая сетка (init_grid())
  
    ![image](https://user-images.githubusercontent.com/111375726/210332466-6a3dc400-b61a-4fc0-91bf-6e794d08c766.png)
  
  * Базовая сетка перемешивается по определенным правилам (shuffle) - поменять соседние районы (3 идущих подряд квадрата 3x3 вертикально или горизонтально) (swap_box_h, swap_box_v), поменять строки из одного района (swap_rows), поменять столбцы из одного района (swap_cols)
  
    ![image](https://user-images.githubusercontent.com/111375726/210333908-55af0942-b81d-4c0b-9f2e-9bba9ea5c6ab.png)

* Из получившейся сетки вычеркивается N клеток (58 hard mode, 51 medium mode, >= 46 easy mode) так, чтобы получившееся судоку все еще имело решение (функия remove_cells)
   
    ![image](https://user-images.githubusercontent.com/111375726/210335217-2c74bae5-b5df-49c4-a8b7-a9c6ea6e7ff7.png)

2) Решение Судоку 
 
 * solver.py Solver(grid), grid - заданная сетка
 
  ![image](https://user-images.githubusercontent.com/111375726/210337017-7a1a562a-87b5-4642-bf72-bc43dceefade.png)
