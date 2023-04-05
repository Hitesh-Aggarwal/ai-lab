import copy


def isEqual(s, g):
    for elem in s:
        if elem not in g:
            return 0
    return 1


def is_in_list(s, list):
    for i in range(len(list)):
        if isEqual(list[i], s):
            return 1
    return 0


def generate_children(start):
    children = []
    for i in range(len(start)):
        if len(start[i]) != 0:
            box = start[i].pop()
            for j in range(len(start)):
                if j != i:
                    start[j].append(box)
                    if not is_in_list(start, children):
                        children.append(copy.deepcopy(start))
                    start[j].pop()
            start[i].append(box)
    return children


def search(start, goal):
    q = []
    visited = []
    q.append(start)
    while q:
        node = q.pop(0)
        if isEqual(node, goal):
            print("Reached goal")
            return visited
        visited.append(node)
        states = generate_children(node)
        for i in range(len(states)):
            if not is_in_list(states[i], visited) and not is_in_list(states[i], q):
                q.append(states[i])
    print("Can't reach goal")
    return visited


def main():
    start = [["A"], ["B", "C"], []]
    goal = [[], [], ["A", "B", "C"]]
    visited = search(start, goal)
    print(len(visited))


if __name__ == "__main__":
    main()

