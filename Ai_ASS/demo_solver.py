from math import inf
from search import SearchResult, Node, extract_solution
from npuzzle import NPuzzleProblem, print_state

def demo_solver(problem):
    """
    Demo solver for one tiny predefined instance only.

    It does NOT perform search.
    It simply follows a hardcoded action sequence while creating Node objects.
    """
    start = problem.initial_state

    known_solutions = {
        ((1, 2, 3),
         (4, 6, 0),
         (7, 5, 8)): ["Left", "Down", "Right"],

        ((1, 2, 3),
         (4, 8, 5),
         (7, 0, 6)): ["Up", "Right", "Down"],
    }

    if start not in known_solutions:
        return SearchResult([], [], 0, inf, [])

    actions_to_apply = known_solutions[start]

    current_node = Node(start, parent=None, action=None, path_cost=0)
    expanded_order = []

    for action in actions_to_apply:
        expanded_order.append(current_node.state)   # current node is being expanded
        successors = problem.get_successors(current_node.state)

        next_state = None
        for a, s in successors:
            if a == action:
                next_state = s
                break

        if next_state is None:
            return SearchResult([], [], 0, inf, expanded_order)

        new_depth = current_node.depth + 1
        new_cost = current_node.path_cost + problem.step_cost(current_node.state, action, next_state)
        current_node = Node(
            state=next_state,
            parent=current_node,
            action=action,
            depth=new_depth,
            path_cost=new_cost
        )

    if not problem.is_goal(current_node.state):
        return SearchResult([], [], 0, inf, expanded_order)

    actions, states = extract_solution(current_node)
    return SearchResult(actions, states, current_node.depth, current_node.path_cost, expanded_order)


def main():
    print("=============================================================================")
    print("Demo that creates the Nodes and SearchResult output for a predefined solution")
    print("=============================================================================\n")

    problem = NPuzzleProblem([
        [1, 2, 3],
        [4, 6, 0],
        [7, 5, 8],
        ])

    print("Initial state:")
    print_state(problem.initial_state)
    print()

    solution = demo_solver(problem)
    print("Solution:")
    print(solution)

    
if __name__ == "__main__":
    main()