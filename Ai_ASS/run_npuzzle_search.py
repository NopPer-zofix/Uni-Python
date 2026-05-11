from search import dfs, bfs, ucs, astar
from npuzzle import NPuzzleProblem, print_state


def print_states(states):
    for i, state in enumerate(states):
        print(f"State {i}:")
        print_state(state)
        print()


def run_search(name, search_function, problem):
    print(f"=== {name} on NPuzzleProblem ===")

    try:
        result = search_function(problem)
        print(result)
        print()

        if hasattr(result, "states"):
            print("Path of states:")
            print_states(result.states)

    except NotImplementedError:
        print(f"{name} not implemented yet.")
    except Exception as e:
        print(f"{name} raised an error: {type(e).__name__}: {e}")

    print("-" * 40)
    print()


def main():
    # Change this state to try other puzzles
    initial_state = [
        [1, 2],
        [0, 3]
    ]

    problem = NPuzzleProblem(initial_state)

    print("Initial state:")
    print_state(problem.initial_state)
    print()

    run_search("DFS", dfs, problem)
    run_search("BFS", bfs, problem)
    run_search("UCS", ucs, problem)
    run_search("A*", astar, problem)


if __name__ == "__main__":
    main()