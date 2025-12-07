# We use this config for tests and visualisation
# Repeat the process to calculate the average time and what method is better for you
# You can change this values

#For graph:
num_nodes = 10
probability = 0.1
directed: True / False

#Bencmark settings:
sizes = [20, 50, 100, 150, 200]

#Visualisation:
visualization_settings= {
    'matrix_cmap': 'Blues',     
    'node_color': 'lightblue',  
    'edge_color': 'gray',       
    'node_size': 700,           
    'arrowsize': 20,            
    'with_labels': True         
}

# Налаштування заголовків графіків 
titles= {
    'matrix': "Матриця суміжності",
    'graph': "Візуалізація графу (список суміжності)",
    'benchmark': "Аналіз часу побудови графу"
}
