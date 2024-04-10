import heapq

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def astar(graph, start, goal):
    queue = [(0, start, [])]  # (total_cost, current_node, path)
    visited = set()
    
    while queue:
        total_cost, current, path = heapq.heappop(queue)
        
        if current == goal:
            return path + [current]
        
        if current in visited:
            continue
        
        visited.add(current)
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                neighbor_cost = graph[current][neighbor]
                heapq.heappush(queue, (total_cost + neighbor_cost + heuristic(neighbor, goal), neighbor, path + [current]))
    
    return None

# Example usage
graph = {
    (0, 0): {(1, 0): 1, (0, 1): 1},
    (1, 0): {(0, 0): 1, (2, 0): 1},
    (0, 1): {(0, 0): 1, (0, 2): 1},
    (2, 0): {(1, 0): 1, (2, 1): 1},
    (0, 2): {(0, 1): 1}
}

start_node = (0, 0)
goal_node = (2, 1)

path = astar(graph, start_node, goal_node)
if path:
    print("Path found:", path)
else:
    print("No path found.")
