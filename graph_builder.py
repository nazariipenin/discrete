import random

class GraphBuilder:              # Клас граф
    def __init__(self, n, p, directed=True):
        self.n = n
        self.p = p
        self.directed = directed
        self.edges = []
        self._generate_graph()
        self.adj_matrix = None
        self.adj_list = None

    def _generate_graph(self):    # Функція для генерації графу
        self.edges = []
        for i in range(self.n):   # Для генерації використовуємо модель випадкового графа Ердеша — Реньї
            for j in range(self.n):
                if i == j:
                    continue
                if random.random() < self.p:
                    self.edges.append((i, j))

    def get_n(self):
        return self.n

    def get_edges(self):
        return self.edges

    def to_matrix(self):    # Створення матриці суміжності
        mat = [[0]*self.n for _ in range(self.n)]
        for u, v in self.edges:
            mat[u][v] = 1
        self.adj_matrix = mat
        return mat

    def to_list(self):      # Створення списку суміжності
        adj = {i: [] for i in range(self.n)}
        for u, v in self.edges:
            adj[u].append(v)
        for i in range(self.n):
            adj[i].sort()
        self.adj_list = adj
        return adj


# Окремі функції з можливістю переходу від одного виду до іншого

# ---ПЕРЕХІД ВІД СПИСКУ ДО МАТРИЦІ СУМІЖНОСТІ---
def list_to_matrix(adj_list):

    n = len(adj_list)

    # Створюємо порожню матрицю n×n
    matrix = [[0] * n for _ in range(n)]

    # Заповнюємо 1 там, де є ребра
    for u, neighbors in adj_list.items():   # u - номер вершини, neighbors - список усіх "сусідів" вершини u
        for v in neighbors:             # Проходимо по кожному "сусіду"
            matrix[u][v] = 1

    print("\nМатриця суміжності:")     # Виводимо матрицю в термінал
    for row in matrix:
        print(row)
    print()

    return matrix



# ---ПЕРЕХІД ВІД МАТРИЦІ ДО СПИСКУ СУМІЖНОСТІ---
def matrix_to_list(adj_matrix):

    n = len(adj_matrix)
    adj_list = {i: [] for i in range(n)}   # Створює порожній список, куди будемо додавати "сусідів"

    for i in range(n):    # Проходимо по рядках матриці
        for j in range(n):       # Проходимося по стовпцях рядка
            if adj_matrix[i][j] == 1:    # Якщо 1 - зв'язок існує, якщо 0 - зв'язку немає, пропускаємо
                adj_list[i].append(j)

    print(f"Список суміжності: {adj_list}")   # Виводимо у термінал список суміжності
    return adj_list


# Приклади для тестування:
# 1:
list_to_matrix({
    0: [1, 3],
    1: [],
    2: [1],
    3: [0, 2]
})

# 2:
matrix_to_list([
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [1, 0, 1, 0]
])