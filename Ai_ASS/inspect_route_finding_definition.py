from route_finding import RouteFindingProblem
from route_data_small import ROADS, LOCATIONS, DEFAULT_START, DEFAULT_GOAL


def show_header(title):
    print("=" * len(title))
    print(title)
    print("=" * len(title))
    print()


def main():
    show_header("Route-finding definition inspection")

    problem = RouteFindingProblem(ROADS, LOCATIONS, DEFAULT_START, DEFAULT_GOAL)

    # You can change this test state and run the script again.
    test_state = "Elm"

    print(f"Initial state: {problem.initial_state}")
    print()

    print(f"Test state: {test_state}")
    print()

    print(f"Goal state: {problem.goal_state}")
    print()

    print("Goal test results:")
    try:
        print("is_goal(test_state):", problem.is_goal(test_state))
        print("is_goal(goal_state):", problem.is_goal(problem.goal_state))
    except NotImplementedError:
        print("is_goal(state): function not implemented yet.")
    print()

    print("Successors of test_state:")
    try:
        successors = problem.get_successors(test_state)

        for action, next_state in successors:
            try:
                cost = problem.step_cost(test_state, action, next_state)
                print(f"Action: {action}   Cost: {cost}   Next state: {next_state}")
                print()
            except NotImplementedError:
                print(f"Action: {action}   Next state: {next_state}")
                print("step_cost(state, action, next_state) not implemented yet.")
                print()

    except NotImplementedError:
        print("get_successors(state) not implemented yet.")
    print()

    print("Heuristic value for test_state:")
    try:
        value = problem.heuristic(test_state)
        print(value)
    except NotImplementedError:
        print("heuristic(state) not implemented yet.")


if __name__ == "__main__":
    main()