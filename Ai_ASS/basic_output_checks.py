from math import isclose
from numbers import Number

from npuzzle import NPuzzleProblem
from route_finding import RouteFindingProblem
from route_data_small import ROADS, LOCATIONS, DEFAULT_START, DEFAULT_GOAL
from search import Node, expand, dfs, bfs, ucs, astar


def check_search_result_shape(name, result):
    required = ["actions", "states", "depth", "cost", "expanded_order"]

    for attr in required:
        if not hasattr(result, attr):
            print(f"{name}: FAILED")
            print(f"Returned object is missing attribute: {attr}")
            return False

    ok = True

    if not isinstance(result.actions, list):
        print(f"{name}: FAILED")
        print("SearchResult.actions should be a list.")
        ok = False
    else:
        for action in result.actions:
            if not isinstance(action, str):
                print(f"{name}: FAILED")
                print("Each element of SearchResult.actions should be a string.")
                ok = False
                break

    if not isinstance(result.states, list):
        print(f"{name}: FAILED")
        print("SearchResult.states should be a list.")
        ok = False
    else:
        for state in result.states:
            if not isinstance(state, tuple):
                print(f"{name}: FAILED")
                print("Each element of SearchResult.states should be a state object (for NPuzzleProblem, a tuple).")
                ok = False
                break

    if not isinstance(result.depth, int):
        print(f"{name}: FAILED")
        print("SearchResult.depth should be an int.")
        ok = False

    if not isinstance(result.cost, Number):
        print(f"{name}: FAILED")
        print("SearchResult.cost should be a number.")
        ok = False

    if not isinstance(result.expanded_order, list):
        print(f"{name}: FAILED")
        print("SearchResult.expanded_order should be a list.")
        ok = False
    else:
        for state in result.expanded_order:
            if not isinstance(state, tuple):
                print(f"{name}: FAILED")
                print("Each element of SearchResult.expanded_order should be a state object (for NPuzzleProblem, a tuple).")
                ok = False
                break

    if isinstance(result.actions, list) and isinstance(result.depth, int):
        if result.depth != len(result.actions):
            print(f"{name}: FAILED")
            print("SearchResult.depth should be equal to len(SearchResult.actions).")
            ok = False

    if ok:
        print(f"{name}: passed.")
    return ok


def check_expand_output():
    problem = NPuzzleProblem([
        [1, 2],
        [0, 3]
    ])

    root = Node(problem.initial_state)

    children = expand(problem, root)

    if not isinstance(children, list):
        print("expand(problem, node): FAILED")
        print("expand(...) should return a list.")
        return

    for child in children:
        if not isinstance(child, Node):
            print("expand(problem, node): FAILED")
            print("Each child returned by expand(...) should be a Node.")
            return

        if child.parent is not root:
            print("expand(problem, node): FAILED")
            print("Each child should have the given node as its parent.")
            return

        if child.depth != root.depth + 1:
            print("expand(problem, node): FAILED")
            print("Each child should have depth parent.depth + 1.")
            return

        if not isinstance(child.action, str):
            print("expand(problem, node): FAILED")
            print("Each child should store an action string.")
            return

        if not isinstance(child.path_cost, Number):
            print("expand(problem, node): FAILED")
            print("Each child should store a numeric path cost.")
            return

    print("expand(problem, node): passed.")


def safe_run(title, fn):
    print(f"--- {title} ---")
    try:
        fn()
    except NotImplementedError:
        print(f"{title}: not implemented yet.")
    except AssertionError as exc:
        print(f"{title}: FAILED")
        print(exc)
    except Exception as exc:
        print(f"{title}: ERROR ({type(exc).__name__})")
        print(exc)
    print()


def check_npuzzle_basics():
    problem = NPuzzleProblem([
        [1, 2],
        [0, 3]
    ])

    # Interface checks
    state = ((1, 0), (3, 2))
    successors = problem.get_successors(state)

    if not isinstance(successors, list):
        print("NPuzzleProblem.get_successors(state): FAILED")
        print("get_successors(state) should return a list.")
        return

    for item in successors:
        if not isinstance(item, tuple) or len(item) != 2:
            print("NPuzzleProblem.get_successors(state): FAILED")
            print("Each successor should be a pair: (action, next_state).")
            return

        action, next_state = item

        if not isinstance(action, str):
            print("NPuzzleProblem.get_successors(state): FAILED")
            print("The first element of each successor should be an action string.")
            return

        if not isinstance(next_state, tuple):
            print("NPuzzleProblem.get_successors(state): FAILED")
            print("The second element of each successor should be a puzzle state.")
            return

    print("NPuzzleProblem.get_successors(state): passed.")

    if successors:
        action, next_state = successors[0]
        cost = problem.step_cost(state, action, next_state)

        if isinstance(cost, Number):
            print("NPuzzleProblem.step_cost(...): passed.")
        else:
            print("NPuzzleProblem.step_cost(...): FAILED")
            print("step_cost(...) should return a number.")
            return

    # Heuristic checks
    try:
        h1 = problem.heuristic(((2, 3), (1, 0)))
        h2 = problem.heuristic(((0, 1), (3, 2)))
    except NotImplementedError:
        print("NPuzzleProblem.heuristic(state): not implemented yet.")
        print()
        return

    if not isinstance(h1, Number) or not isinstance(h2, Number):
        print("NPuzzleProblem.heuristic(state): FAILED")
        print("heuristic(state) should return a number.")
        print()
        return

    # Hardcoded value check:
    # For ((2, 3), (1, 0)), Manhattan distance should be 4
    if h1 != 4:
        print("NPuzzleProblem.heuristic(state): FAILED")
        print("Expected heuristic(((2, 3), (1, 0))) == 4")
        print()
        return

    # Non-constant check
    if h1 == h2:
        print("NPuzzleProblem.heuristic(state): FAILED")
        print("Heuristic returned the same value for two different states.")
        print()
        return

    print("NPuzzleProblem.heuristic(state): passed.")
    print()


def check_route_finding_basics():
    problem = RouteFindingProblem(ROADS, LOCATIONS, DEFAULT_START, DEFAULT_GOAL)

    successors = None

    # is_goal checks
    try:
        start_is_goal = problem.is_goal(DEFAULT_START)
        goal_is_goal = problem.is_goal(DEFAULT_GOAL)

        assert isinstance(start_is_goal, bool), "is_goal(state) should return True or False."
        assert isinstance(goal_is_goal, bool), "is_goal(state) should return True or False."
        assert start_is_goal is False, "The initial state should not be the goal in the small route map."
        assert goal_is_goal is True, "The goal state should be recognised as a goal."

        print("RouteFindingProblem.is_goal(state): passed.")
    except NotImplementedError:
        print("RouteFindingProblem.is_goal(state): not implemented yet.")
    except AssertionError as exc:
        print("RouteFindingProblem.is_goal(state): FAILED")
        print(exc)

    # get_successors checks
    try:
        successors = problem.get_successors(DEFAULT_START)

        assert isinstance(successors, list), "get_successors(state) should return a list."
        assert len(successors) > 0, "get_successors(state) returned an empty list for the initial state."

        for item in successors:
            assert isinstance(item, tuple) and len(item) == 2, "Each successor should be a pair: (action, next_state)."
            action, next_state = item
            assert isinstance(action, str), "The first element of each successor should be an action string."
            assert isinstance(next_state, str), "The second element of each successor should be a city name string."
            assert action == f"go({next_state})", (
                f'Expected action "go({next_state})" for successor state "{next_state}".'
            )

        print("RouteFindingProblem.get_successors(state): passed.")
    except NotImplementedError:
        print("RouteFindingProblem.get_successors(state): not implemented yet.")
    except AssertionError as exc:
        print("RouteFindingProblem.get_successors(state): FAILED")
        print(exc)

    # step_cost checks
    if successors:
        try:
            first_action, first_state = successors[0]
            cost = problem.step_cost(DEFAULT_START, first_action, first_state)

            assert isinstance(cost, Number), "step_cost(state, action, next_state) should return a number."
            assert cost == 3, "For the small route map, the cost from Arbor to Brook should be 3."

            print("RouteFindingProblem.step_cost(...): passed.")
        except NotImplementedError:
            print("RouteFindingProblem.step_cost(...): not implemented yet.")
        except AssertionError as exc:
            print("RouteFindingProblem.step_cost(...): FAILED")
            print(exc)
    else:
        print("RouteFindingProblem.step_cost(...): skipped because get_successors(state) is not available.")

    # heuristic checks
    try:
        h_start = problem.heuristic("Arbor")
        h_other = problem.heuristic("Cedar")

        assert isinstance(h_start, Number), "RouteFindingProblem.heuristic(state) should return a number."
        assert isinstance(h_other, Number), "RouteFindingProblem.heuristic(state) should return a number."
        assert isclose(h_start, 8.06225774829855, rel_tol=1e-9, abs_tol=1e-9), (
            'For the small route map, the heuristic at "Arbor" should be 8.06225774829855.'
        )
        assert h_start != h_other, "The heuristic should not return the same value for two different states."

        print("RouteFindingProblem.heuristic(state): passed.")
    except NotImplementedError:
        print("RouteFindingProblem.heuristic(state): not implemented yet.")
    except AssertionError as exc:
        print("RouteFindingProblem.heuristic(state): FAILED")
        print(exc)


def check_search_function_interfaces():
    tiny_puzzle = NPuzzleProblem([
        [1, 2],
        [0, 3]
    ])

    for name, fn in [("dfs(problem)", dfs), ("bfs(problem)", bfs), ("ucs(problem)", ucs), ("astar(problem)", astar)]:
        try:
            result = fn(tiny_puzzle)
            check_search_result_shape(name, result)
        except NotImplementedError:
            print(f"{name}: not implemented yet.")
        except Exception as exc:
            print(f"{name}: FAILED")
            print(f"Raised an unexpected exception: {exc}")
        print()


def main():
    print("===================")
    print("Basic output checks")
    print("===================\n")

    safe_run("NPuzzle basics check", check_npuzzle_basics)
    safe_run("Route-finding basics check", check_route_finding_basics)
    safe_run("expand(...) output check", check_expand_output)
    safe_run("Search function interface checks", check_search_function_interfaces)


if __name__ == "__main__":
    main()