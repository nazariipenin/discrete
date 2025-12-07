import time
import networkx as nx
import matplotlib.pyplot as plt
from graph_builder import GraphBuilder


class GraphVisualizer:
    def __init__(self, builder: GraphBuilder):
        self.builder = builder  # Зберігаємо об'єкт для роботи з графом

    # Візуалізація
    def visualize_matrix(self):
        if self.builder.adj_matrix is None:
            self.builder.to_matrix()    # Генеруємо матрицю суміжності якщо вона ще не створена

        plt.imshow(self.builder.adj_matrix, cmap='Blues')  # Відображаємо матрицю кольорами
        plt.title("Матриця суміжності")
        plt.xlabel("Вершини")
        plt.ylabel("Вершини")
        plt.colorbar(label="Ребро")
        plt.show()  # Показуємо графік

    # Візуалізація
    def visualize_list(self):
        if self.builder.adj_list is None:
            self.builder.to_list()   # Генеруємо список суміжності якщо він не створений

        G = nx.DiGraph()     # Створюємо орієнтований граф
        G.add_nodes_from(range(self.builder.n)) # Додаємо вузли до n-1
        G.add_edges_from(self.builder.edges)    # Додаємо ребра

        pos = nx.spring_layout(G, seed=42)      # Розташування вузлів

        nx.draw(
            G, pos,     # Малюємо граф та встановлюємо параметри візуалізації
            with_labels=True,
            node_color='lightblue',
            edge_color='gray',
            node_size=700,
            arrowsize=20
        )
        plt.title("Візуалізація графу (список суміжності)")
        plt.show()   # Показуємо графік


    # Аналіз часу побудови
    def measure_and_plot_time(self, sizes, probability):
        matrix_times = []
        list_times = [] #сюди записуємо час побудови відповідних графів

        print(f"\n{'=' * 40}")
        print(f"Початок тестування швидкодії (p={probability})")
        print(f"{'=' * 40}")

        for n in sizes:
            # Створюємо граф
            builder = GraphBuilder(n, probability)

            # Час формування матриці сміжності

            start = time.perf_counter() # Записує час початку побудови
            builder.to_matrix() # Починає побудову
            end = time.perf_counter() # викликає функцію яка рахує час

            m_time = end - start  # Зберігаємо час у змінну
            matrix_times.append(m_time)

            #Час формування списку сміжності

            start = time.perf_counter()
            builder.to_list()
            end = time.perf_counter()

            l_time = end - start  # Зберігаємо час у змінну
            list_times.append(l_time) # викликає функцію яка рахує час
            # Прінт в термінал
            print(f"Розмір n={n:<5} | Матриця: {m_time:.6f} с | Список: {l_time:.6f} с")

        print(f"{'=' * 40}\n")

        # Побудова графіка часу
        plt.plot(sizes, matrix_times, marker='o', label="Матриця суміжності")
        plt.plot(sizes, list_times, marker='s', label="Список суміжності")
        plt.xlabel("Кількість вершин (n)")
        plt.ylabel("Час виконання (сек)")
        plt.title(f"Аналіз часу побудови графу (p={probability})")
        plt.legend()
        plt.grid(True)
        plt.show()


num_nodes = 10
probability = 0.7

# Створюємо граф для демонстрації
builder = GraphBuilder(num_nodes, probability)
print("Edges:", builder.get_edges())

print("\nMatrix:")
for row in builder.to_matrix():
    print(row)

print("\nAdjacency List:")
for node, neighbors in builder.to_list().items():
    print(f"{node} -> {neighbors}")

visualizer = GraphVisualizer(builder)

# Закоментовано, щоб не заважало графікам часу, розкоментуйте за потреби:
visualizer.visualize_matrix()
visualizer.visualize_list()

# Перевіряємо час побудови для різних розмірів графів
sizes = [20, 50, 100, 150, 200]
visualizer.measure_and_plot_time(sizes, probability)

