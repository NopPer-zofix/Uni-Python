from npuzzle import NPuzzleProblem, print_state


def show_header(title):
    print("=" * len(title))
    print(title)
    print("=" * len(title))
    print()


def main():
    show_header("NPuzzle definition inspection")

    problem = NPuzzleProblem([
        [1, 0, 3],
        [4, 2, 5],
        [7, 8, 6]
    ])

    # You can change this test state and run the script again.
    test_state = (
        (7, 2, 4),
        (5, 0, 6),
        (8, 3, 1)
    )

    print("Initial state:")
    print_state(problem.initial_state)
    print()

    print("Test state:")
    print_state(test_state)
    print()

    print("Goal state:")
    print_state(problem.goal_state)
    print()

    print("Goal test results:")
    print("is_goal(test_state):", problem.is_goal(test_state))
    print("is_goal(goal_state):", problem.is_goal(problem.goal_state))
    print()

    print("Successors of test_state:")
    successors = problem.get_successors(test_state)
    for action, next_state in successors:
        cost = problem.step_cost(test_state, action, next_state)
        print(f"Action: {action}   Cost: {cost}")
        print_state(next_state)
        print()

    print("Heuristic value for test_state:")
    try:
        value = problem.heuristic(test_state)
        print(value)
    except NotImplementedError:
        print("heuristic(state) not implemented yet.")


if __name__ == "__main__":
    main()