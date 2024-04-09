
# code will be removed soon

def uniform_cost_search(goal, start):
    global graph, cost
    answer = []
    queue = []
    for i in range(len(goal)):
        answer.append(10**8)
        queue.append([0, start])
        visited = {}
        count = 0
    while (len(queue) > 0):
        queue = sorted(queue)
        p = queue[-1]
        del queue[-1]
        p[0] *= -1
        if (p[1] in goal):
            index = goal.index(p[1])
            if (answer[index] == 10**8):
                count += 1
                if (answer[index] > p[0]):
                    answer[index] = p[0]
                    del queue[-1]
                    queue = sorted(queue)
        if (count == len(goal)):
            return answer
        if (p[1] not in visited):
            for i in range(len(graph[p[1]])):
                queue.append([(p[0] + cost[(p[1], graph[p[1]][i])]) * -1, graph[p[1]][i]])
                visited[p[1]] = 1
    return answer




graph, cost = [[] for i in range(8)], {}
graph[0].append(1)
graph[0].append(3)
graph[3].append(1)
graph[3].append(6)
graph[3].append(4)
graph[1].append(6)
graph[4].append(2)
graph[4].append(5)
graph[2].append(1)
graph[5].append(2)
graph[5].append(6)
graph[6].append(4)
cost[(0, 1)] = 2
cost[(0, 3)] = 5
cost[(1, 6)] = 1
cost[(3, 1)] = 5
cost[(3, 6)] = 6
cost[(3, 4)] = 2
cost[(2, 1)] = 4
cost[(4, 2)] = 4
cost[(4, 5)] = 3
cost[(5, 2)] = 6
cost[(5, 6)] = 3
cost[(6, 4)] = 7
goal = []
goal.append(6)
answer = uniform_cost_search(goal, 0)

print("Minimum cost from 0 to 6 is = ", answer[0])




# THE CODE IS REPLACED WITH THIS NEW CODE


# from collections import defaultdict
# import heapq

# def uniform_cost_search(goal, start):
#     global graph, cost
    
#     # Initialize answer list with infinity values for each goal node
#     answer = [float('inf')] * len(goal)
    
#     # Initialize priority queue (heap) with start node and its cost so far
#     queue = [(0, start)]
    
#     # Set to keep track of visited nodes
#     visited = set()
    
#     # Continue search while there are nodes in the queue
#     while queue:
#         # Pop the node with the lowest cost so far from the queue
#         cost_so_far, current = heapq.heappop(queue)
        
#         # If the node is already visited, skip it
#         if current in visited:
#             continue
        
#         # Mark the current node as visited
#         visited.add(current)
        
#         # If the current node is one of the goal nodes
#         if current in goal:
#             # Find the index of the current node in the goal list
#             index = goal.index(current)
#             # If the cost to reach the current goal node is still infinity
#             if answer[index] == float('inf'):
#                 # Update the cost to the cost so far
#                 answer[index] = cost_so_far
        
#         # If all goal nodes have been reached, exit the loop
#         if all(answer[i] != float('inf') for i in range(len(goal))):
#             break
        
#         # Iterate over neighbours of the current node
#         for neighbour, edge_cost in graph[current]:
#             # If the neighbour has not been visited
#             if neighbour not in visited:
#                 # Calculate the total cost to reach the neighbour
#                 total_cost = cost_so_far + edge_cost
#                 # Push the neighbour into the queue with its total cost
#                 heapq.heappush(queue, (total_cost, neighbour))
    
#     # Return the list of minimum costs to reach each goal node
#     return answer

# # Define the graph as a defaultdict of lists to store neighbours and their costs
# graph = defaultdict(list)
# graph[0].append((1, 2))
# graph[0].append((3, 5))
# graph[3].append((1, 5))
# graph[3].append((6, 6))
# graph[3].append((4, 2))
# graph[1].append((6, 1))
# graph[4].append((2, 4))
# graph[4].append((5, 3))
# graph[2].append((1, 4))
# graph[5].append((2, 6))
# graph[5].append((6, 3))
# graph[6].append((4, 7))

# # Define the goal node(s)
# goal = [6]

# # Call the uniform cost search function with the goal node(s) and start node
# answer = uniform_cost_search(goal, 0)

# # Print the minimum cost from start node to goal node(s)
# print("Minimum cost from 0 to 6 is =", answer[0])
