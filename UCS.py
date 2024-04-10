import heapq

def uniform_cost_search(graph, start, goal):
    queue = [(0, start, [])]  # (cost, node, path)
    visited = set()
    
    while queue:
        cost, node, path = heapq.heappop(queue)
        
        if node in visited:
            continue
        
        visited.add(node)
        path = path + [node]
        
        if node == goal:
            return path
        
        for neighbor, neighbor_cost in graph.get(node, {}).items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + neighbor_cost, neighbor, path))
    
    return None

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2},
    'C': {'D': 3},
    'D': {'E': 1},
    'E': {}
}

start_node = 'A'
goal_node = 'E'
result = uniform_cost_search(graph, start_node, goal_node)
print("Path found:", result)
