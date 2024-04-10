from collections import defaultdict
import heapq

def uniform_cost_search(goal, start, graph):
    answer = [float('inf')] * len(goal)
    queue = [(0, start)]
    visited = set()
    
    while queue:
        cost_so_far, current = heapq.heappop(queue)
        if current in visited:
            continue
        visited.add(current)
        
        if current in goal:
            index = goal.index(current)
            if answer[index] == float('inf'):
                answer[index] = cost_so_far
        
        if all(answer[i] != float('inf') for i in range(len(goal))):
            break
        
        for neighbour, edge_cost in graph[current]:
            if neighbour not in visited:
                heapq.heappush(queue, (cost_so_far + edge_cost, neighbour))
    
    return answer

graph = defaultdict(list)
graph[0] = [(1, 2), (3, 5)]
graph[3] = [(1, 5), (6, 6), (4, 2)]
graph[1] = [(6, 1)]
graph[4] = [(2, 4), (5, 3)]
graph[2] = [(1, 4)]
graph[5] = [(2, 6), (6, 3)]
graph[6] = [(4, 7)]

goal = [6]

answer = uniform_cost_search(goal, 0, graph)

print("Minimum cost from 0 to 6 is =", answer[0])
