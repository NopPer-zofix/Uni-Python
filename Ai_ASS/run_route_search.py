from search import dfs, bfs, ucs, astar
from route_finding import RouteFindingProblem, print_state
from route_data_small import ROADS, LOCATIONS, DEFAULT_START, DEFAULT_GOAL


def print_states(states):
    for i, state in enumerate(states):
        print(f"State {i}:")
        print_state(state)
        print()


def run_search(name, search_function, problem):
    print(f"=== {name} on RouteFindingProblem ===")

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
    # Change these to try different route-finding problems
    initial_state = DEFAULT_START
    goal_state = DEFAULT_GOAL

    problem = RouteFindingProblem(
        ROADS,
        LOCATIONS,
        initial_state,
        goal_state
    )

    print("Initial state:")
    print_state(problem.initial_state)
    print("Goal state:")
    print_state(problem.goal_state)
    print()

    run_search("DFS", dfs, problem)
    run_search("BFS", bfs, problem)
    run_search("UCS", ucs, problem)
    run_search("A*", astar, problem)


if __name__ == "__main__":
    main()