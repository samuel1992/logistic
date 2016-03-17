# coding: utf-8
from eve import Eve
from flask import request, jsonify
from bson import json_util
from pymongo import MongoClient
import dijkstra
import pymongo
import json

# Definindo minha conexao com o banco de dados mongoDb
client = MongoClient('mongodb://localhost:27017')

# Definindo meu database
db = client.logistic

# Definindo minha collection do database
collection = db.maps

# Instanciando a app do EVE
app = Eve()
#Habilitando debug para que o server detecte alterações em tempo de execuçao
app.debug=True



@app.route('/maps/shortest', methods=['GET'])
def getCollection():
    mapName = request.args.get('map')
    origin = request.args.get('origin') #Ponto de origem
    destiny = request.args.get('destiny') #Ponto final (chegada)
    price = request.args.get('price')
    autonomy = request.args.get('autonomy')
    steps = [] # Lista que ira ser preenchida com todos os passos do caminho
    dictPaths = {} # Dicionario com o valor de todos as rotas
    graph = dijkstra.Graph() # Lib que faz o grafico de vertex para calcular o dijkstra
    vertex = [] # Lista de vertex
    try:
        map = collection.find_one({'title':mapName})
    except:
        response = jsonify({'response':'The passed map does not exists or is blank'})
        response.status_code = 400
        return response
    
    # Fazendo a iteração para preencher uma lista
    # de vertex que serão usado na lib Graph()
    for vert in map['routes']: 
        vertex.append(vert['origin'])
        vertex.append(vert['destiny'])

    # Iterando nos vertex setando para que nao se repitam
    for i in list(set(vertex)):
        graph.add_vertex(i)

    # Adicionando os vertexa lib Graph
    for vert in map['routes']:
        dictPaths[vert['origin']+vert['destiny']] = vert['distance']
        graph.add_edge(vert['origin'],vert['destiny'],vert['distance'])

    # Verificando se os pontos existem
    if origin not in vertex : 
        response = jsonify({'response': 'The parameter origin does not contain on map %s'
                            % mapName})
        response.status_code = 400
        return response
    if destiny not in vertex : 
        response = jsonify({'response': 'The parameter destiny does not contain on map %s'
                            % mapName})
        response.status_code = 400
        return response

    dijkstra.dijkstra(graph, graph.get_vertex(origin), graph.get_vertex(destiny))
    target = graph.get_vertex(destiny)
    path = [target.get_id()]
    dijkstra.shortest(target, path)

    a = 0
    while a < (len(path[::-1])-1):
        steps.append(path[::-1][a]+path[::-1][a+1])
        a=a+1

    total = 0
    for i in steps:
        total = total + dictPaths[i]

    # Apenas formatando a lista para utf-8
    pathList = []
    for i in path[::-1]:
        pathList.append(i.encode('utf-8'))
    
    
    # Fazendo o calculo do custo nessa rota de menor distancia
    cost = float(total) / float(autonomy) * float(price)

    response = []
    response.append({'Path': '%s' % pathList})
    response.append({'Total KM' : '%.2f' % total})
    response.append({'Cost' : '%.2f' % cost})
    return jsonify(data=response)


if __name__ == '__main__':
    app.run()

