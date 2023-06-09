# Ao-star algorithm

edge_cost = 1


def node_cost(heuristic, children):
    cost = {}
    if "OR" in children:
        or_children = children["OR"]
        for child in or_children:
            cost[child] = heuristic[child] + edge_cost
    if "AND" in children:
        and_children = children["AND"]
        cost["AND"] = 0
        for child in and_children:
            cost["AND"] += heuristic[child] + edge_cost
    return cost


def cost(heuristic, tree):
    nodes = list(tree.keys())
    nodes.reverse()
    print(nodes)
    for node in nodes:
        parent_cost = node_cost(heuristic, tree[node])
        print(parent_cost)
        heuristic[node] = min(list(parent_cost.values()))


def main():
    start = "a"

    heuristic = {"a": 50, "b": 6, "c": 12, "d": 10, "e": 4, "f": 4, "g": 5, "h": 7}

    tree = {
        "a": {"OR": ["d"], "AND": ["b", "c"]},
        "b": {"OR": ["g", "h"]},
        "d": {"AND": ["e", "f"]},
    }
    cost(heuristic, tree)
    print("Cost of traversal:", heuristic[start])


if __name__ == "__main__":
    main()
