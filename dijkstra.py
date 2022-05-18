import heapq


INF = 1000000

def dijkstra(start_node):
    
    shortest_distance = {node: INF for node in graph}
    shortest_distance[start_node] = 0
    queue = []

    heapq.heappush(queue, (shortest_distance[start_node], start_node))
    
    while queue:
        
        current_distance, node = heapq.heappop(queue)
        
        if shortest_distance[node] < current_distance:
            continue

        
        for near_node, distance in graph[node].items():
            wieght_distance = current_distance + distance

            if wieght_distance < shortest_distance[near_node]:
                shortest_distance[near_node] = wieght_distance
                heapq.heappush(queue, (wieght_distance, near_node))

            

    return shortest_distance

# case 1 : graph in homework3

graph = {
    'A': {'A':0,  'B': 5,   'C':INF,'D': 2,  'E':4,  'F':INF},
    'B': {'A':5,  'B': 0,   'C':3,  'D': 3,  'E':INF,'F':INF},
    'C': {'A':INF,'B': 3,   'C':0,  'D': 3,  'E':4,  'F':2},
    'D': {'A':2,  'B': 3,   'C':3,  'D': 0,  'E':1,  'F':INF},
    'E': {'A':4,  'B': INF, 'C':4,  'D': 1,  'E':0,  'F':2},
    'F': {'A':INF,'B': INF, 'C':2,  'D': INF,'E':2,  'F':0}
}


# case2 : more complicated graph
'''
graph = {
    'A': {'A':0,  'B': 9,  'C':8,  'D': INF,'E':6,  'F':INF},
    'B': {'A':9,  'B': 0,  'C':3,  'D': 12, 'E':INF,'F':4},
    'C': {'A':8,  'B': 3,  'C':0,  'D': 9,  'E':1,  'F':INF},
    'D': {'A':INF,'B': 12, 'C':9,  'D': 0,  'E':5,  'F':3},
    'E': {'A':6,  'B': INF,'C':1,  'D': 5,  'E':0,  'F':6},
    'F': {'A':INF,'B': 4,  'C':INF,'D': 3,  'E':6,  'F':0}
}
'''


# case3 : graph in our notebook
'''
graph = {
    'A': {'A':0,  'B': 1,  'C':INF,'D': 1,  'E':5 },
    'B': {'A':9,  'B': 0,  'C':3,  'D': 2,  'E':INF},
    'C': {'A':INF,'B': INF,'C':0,  'D': 4,  'E':INF},
    'D': {'A':INF,'B': INF,'C':2,  'D': 0,  'E':3},
    'E': {'A':3,  'B': INF,'C':INF,'D': INF,'E':0}
}
'''






print("----------Dijkstra Algorithm----------")
start_node = input("Input start node: ")
result = dijkstra(start_node)
print("Shortest distances start from",start_node)
print(result)
