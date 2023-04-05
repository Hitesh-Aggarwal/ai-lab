# visited = []

import copy

def search(graph, start_node):
    cost = 1000
    q = []
    q.append([start_node, 0, []])
    # visited.append([start_node, 0])
    while q:
        node, dist, parents = q.pop(0)
        if len(parents) == (len(graph[0]) - 1):
            if (dist < cost):
                print("Path:")
                for i in parents:
                    print(i, end=" ")
                print(node)
                cost = dist
        successors = []
        temp = copy.deepcopy(parents)
        if node not in parents:
            temp.append(node)
        for i in range(len(graph[node])):
            if i != node and i not in parents:
                successors.append(
                    [i, dist + graph[node][i], temp],
                )
        for s in successors:
            if s not in q:
                q.append(s)
    return cost


def main():
    graph = []
    graph.append([0, 10, 15, 20])
    graph.append([10, 0, 35, 25])
    graph.append([15, 35, 0, 30])
    graph.append([20, 25, 30, 0])
    # start_node = input("Enter starting node: ")
    start_node = 0
    cost = search(graph, int(start_node))
    print(f"Minimum cost of travelling: {cost}")


if __name__ == "__main__":
    main()
