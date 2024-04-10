
from collections import defaultdict
import heapq

def uniform_cost_search(goal, start):
    global graph, cost
    
    # Initialize answer list with infinity values for each goal node
    answer = [float('inf')] * len(goal)
    
    # Initialize priority queue (heap) with start node and its cost so far
    queue = [(0, start)]
    
    # Set to keep track of visited nodes
    visited = set()
    
    # Continue search while there are nodes in the queue
    while queue:
        # Pop the node with the lowest cost so far from the queue
        cost_so_far, current = heapq.heappop(queue)
        
        # If the node is already visited, skip it
        if current in visited:
            continue
        
        # Mark the current node as visited
        visited.add(current)
        
        # If the current node is one of the goal nodes
        if current in goal:
            # Find the index of the current node in the goal list
            index = goal.index(current)
            # If the cost to reach the current goal node is still infinity
            if answer[index] == float('inf'):
                # Update the cost to the cost so far
                answer[index] = cost_so_far
        
        # If all goal nodes have been reached, exit the loop
        if all(answer[i] != float('inf') for i in range(len(goal))):
            break
        
        # Iterate over neighbours of the current node
        for neighbour, edge_cost in graph[current]:
            # If the neighbour has not been visited
            if neighbour not in visited:
                # Calculate the total cost to reach the neighbour
                total_cost = cost_so_far + edge_cost
                # Push the neighbour into the queue with its total cost
                heapq.heappush(queue, (total_cost, neighbour))
    
    # Return the list of minimum costs to reach each goal node
    return answer

# Define the graph as a defaultdict of lists to store neighbours and their costs
graph = defaultdict(list)
graph[0].append((1, 2))
graph[0].append((3, 5))
graph[3].append((1, 5))
graph[3].append((6, 6))
graph[3].append((4, 2))
graph[1].append((6, 1))
graph[4].append((2, 4))
graph[4].append((5, 3))
graph[2].append((1, 4))
graph[5].append((2, 6))
graph[5].append((6, 3))
graph[6].append((4, 7))

# Define the goal node(s)
goal = [6]

# Call the uniform cost search function with the goal node(s) and start node
answer = uniform_cost_search(goal, 0)

# Print the minimum cost from start node to goal node(s)
print("Minimum cost from 0 to 6 is =", answer[0])
