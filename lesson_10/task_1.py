class Matrix:  # создание класса
    def __init__(self, *args):
        self.args = args  # инициализатор принимает список списков в качестве args

    def __str__(self):
        tmp_matrix = ""  # временная строка
        for arg in self.args:
            for el in arg:
                for a in el:
                    if el[-1] == a:  # если элемент последний во вложенном списке - перенести строку
                        tmp_matrix += f"{str(a)}\n"  # привод элемента матрицы к строке и добавление к временной строке
                    else:
                        tmp_matrix += f"{str(a)} "
        return tmp_matrix

    def __add__(self, other):
        tmp_matrix = []  # внешний список
        for a, i in zip(*self.args, *other.args):
            inner_list = []  # вложенный список
            for el1, el2 in zip(a, i):
                inner_list.append(el1 + el2)  # добавление элемента матрицы во вложенный список
            tmp_matrix.append(inner_list)  # доавление вложенного списка во внешний
        return Matrix(tmp_matrix)  # возвращаем экземпляр класса


matrix = Matrix([[12, 23, 32], [67, 23, 87], [28, 96, 6]])
matrix2 = Matrix([[27, 574, 12], [26, 12, 89], [23, 75, 12]])
print(matrix)
print(matrix2)
matrix3 = matrix + matrix2
print(matrix3)
#  проверка класса и методов
