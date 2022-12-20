import collections 
import math

#создание основного графа
graph = dict()
graph['start'] = dict()
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = dict() 
graph['a']['end'] = 1
graph['b'] = dict()
graph['b']['a'] = 3
graph['b']['end'] = 5
graph['end'] = dict()

#стоимости весов
infinity = math.inf
costs = dict()
costs['a'] = 6
costs['b'] = 2
costs['end'] = infinity

#хеш-таблица родителей
parents = dict()
parents['a'] = 'start'
parents['b'] = 'start'
parents['in'] = None

#массив для отслеживания всех уже обработанных узлов
processed = list()

#функция
def find_lowest_cost_node(costs):
    lowest_cost = math.inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and not node in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

#алгоритм
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(f'Время кратчайшего пути - {costs['end']}')