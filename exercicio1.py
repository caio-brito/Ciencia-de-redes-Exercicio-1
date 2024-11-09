import matplotlib.pyplot as plt
import networkx as nx

edges = [
    ("Albuquerque", "Atlanta"),
    ("Chicago", "New York"),
    ("Chicago", "Pinhais"),
    ("Curitiba", "Atlanta"),
    ("Curitiba", "Chicago"),
    ("Curitiba", "Miami"),
    ("Curitiba", "New York"),
    ("Curitiba", "Sao Paulo"),
    ("Londrina", "Foz"),
    ("Maringa", "Albuquerque"),
    ("Maringa", "Cleveland"),
    ("Miami", "Denver"),
    ("Miami", "New York"),
    ("Miami", "Philadelphia"),
    ("Minneapolis", "Foz"),
    ("New York", "Cleveland"),
    ("New York", "Minneapolis"),
    ("Philadelphia", "Atlanta"),
    ("Phoenix", "Cleveland"),
    ("Phoenix", "Maringa"),
    ("Pinhais", "Londrina"),
    ("Ponta Grossa", "Cleveland"),
    ("Ponta Grossa", "Foz"),
    ("Ponta Grossa", "Londrina"),
    ("Sao Paulo", "Boston"),
    ("Sao Paulo", "Chicago"),
    ("Sao Paulo", "Foz"),
    ("Sao Paulo", "Londrina"),
    ("Sao Paulo", "Minneapolis"),
    ("Sao Paulo", "Ponta Grossa"),
    ("Tulsa", "Maringa"),
    ("Tulsa", "New York")
]



# Iniciando grafo
G = nx.Graph()
G.add_edges_from(edges)

# Desenhando o grafo
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, seed=42)  
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="blue", font_size=10, font_color = "white", font_weight="bold", edge_color="gray")


# Construa um grafo apropriado que represente esses relacionamentos utilizando o Networkx. 
#plt.show()

#2
#a) Considerando o menor número de conexões possível para chegar a qualquer destino, qual é o número maior número de conexões que um passageiro pode fazer em uma única viagem entre duas cidades atendidas?
print(nx.diameter(G))

#b) Qual é o coeficiente de clusterização de Curitiba? E da rede geral?
print(nx.clustering(G, nodes = "Curitiba"))

#3
#a) Adicione o atributo nos nós chamado Country, onde o valor se refere ao país onde cada cidade está localizada.

#Iniciando um dicionario para facilitar a inserção de atributos
country_attributes = {
    "Albuquerque": "EUA",
    "Atlanta": "EUA",
    "Chicago": "EUA",
    "New York": "EUA",
    "Pinhais": "Brasil",
    "Curitiba": "Brasil",
    "Miami": "EUA",
    "Sao Paulo": "Brasil",
    "Londrina": "Brasil",
    "Foz": "Brasil",
    "Maringa": "Brasil",
    "Cleveland": "EUA",
    "Denver": "EUA",
    "Philadelphia": "EUA",
    "Minneapolis": "EUA",
    "Phoenix": "EUA",
    "Ponta Grossa": "Brasil",
    "Boston": "EUA",
    "Tulsa": "EUA"
}

nx.set_node_attributes(G, country_attributes, name="Country")

# Adicionando pesos às arestas com base em origem e destino
for u, v in G.edges():
    country_u = G.nodes[u]["Country"]
    country_v = G.nodes[v]["Country"]
    
    # Se for voo internacional, peso 5
    if country_u != country_v:
        G[u][v]["weight"] = 5
    # Se for voo no mesmo país, peso 1
    else:
        G[u][v]["weight"] = 1

# Verificando se funcionou
for u, v, data in G.edges(data=True):
    print(f"{u} - {v}: {data['weight']}")

# Exportar o grafo no formato .gml
nx.write_gml(G, "rede_final.gml")
