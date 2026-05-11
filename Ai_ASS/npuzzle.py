class NPuzzleProblem:
    """
    n-puzzle problem definition.

    State representation:
        A state is a tuple of tuples, for example:
            ((1, 2, 3),
             (4, 0, 6),
             (7, 5, 8))

        The blank tile is represented by 0.

    Data provided to the constructor:
        initial_state:
            The start state of the puzzle. It may be given as a list of lists
            or as a tuple of tuples. It is converted internally to a tuple of tuples.

        goal_state:
            The goal state of the puzzle. If no goal_state is provided, the
            default goal is used, for example for the 8-puzzle:
                ((1, 2, 3),
                 (4, 5, 6),
                 (7, 8, 0))
    """
    
    def __init__(self, initial_state, goal_state=None):
        self.initial_state = tuple(tuple(row) for row in initial_state)

        self.size = len(self.initial_state)

        if goal_state is None:
            numbers = list(range(1, self.size * self.size)) + [0]
            rows = []
            for i in range(self.size):
                row = tuple(numbers[i * self.size:(i + 1) * self.size])
                rows.append(row)
            self.goal_state = tuple(rows)
        else:
            self.goal_state = tuple(tuple(row) for row in goal_state)

    def is_goal(self, state):
        """
        Return True if and only if the given state is the goal state.
        """
        return state == self.goal_state

    def get_successors(self, state):
        """
        Return the successors of the given state as a list of pairs:
            (action, next_state)

        Actions are one of:
            "Up", "Down", "Left", "Right"

        Successors are returned in this fixed order:
            Up, Down, Left, Right
        """
        blank_row = -1
        blank_col = -1

        # Find the blank tile
        for r in range(self.size):
            for c in range(self.size):
                if state[r][c] == 0:
                    blank_row = r
                    blank_col = c
                    break
            if blank_row != -1:
                break

        successors = []

        moves = [
            ("Up", -1, 0),
            ("Down", 1, 0),
            ("Left", 0, -1),
            ("Right", 0, 1),
        ]

        for action, dr, dc in moves:
            new_row = blank_row + dr
            new_col = blank_col + dc

            if 0 <= new_row < self.size and 0 <= new_col < self.size:
                # Make a new state by swapping the blank with the target tile
                new_state = [list(row) for row in state]
                new_state[blank_row][blank_col], new_state[new_row][new_col] = \
                    new_state[new_row][new_col], new_state[blank_row][blank_col]

                new_state = tuple(tuple(row) for row in new_state)
                successors.append((action, new_state))

        return successors

    def step_cost(self, state, action, next_state):
        """
        Return the cost of taking the given action from state to next_state.

        In this problem, all moves have cost 1.
        """
        return 1

    def heuristic(self, state):
        """
        Return the Manhattan distance from the current state to the goal state.

        The Manhattan distance is computed by adding, for each numbered tile,
        the number of horizontal and vertical moves needed to move that tile
        from its current position to its goal position.

        The blank tile (0) should not be included.

        Example:
            In the 8-puzzle, if tile 8 is currently at position (1, 2)
            and its goal position is (2, 1), then its contribution to the
            Manhattan distance is:
                abs(1 - 2) + abs(2 - 1) = 2
        """
        goal_positions = {}
        for r in range(self.size):
            for c in range(self.size):
                tile = self.goal_state[r][c]
                goal_positions[tile] = (r, c)

        total = 0
        for r in range(self.size):
            for c in range(self.size):
                tile = state[r][c]
                if tile != 0:
                    goal_r, goal_c = goal_positions[tile]
                    total += abs(r - goal_r) + abs(c - goal_c)
        return total


def print_state(state):
    """
    Print a state in an easy-to-read form.
    """
    for row in state:
        print(" ".join(str(x) if x != 0 else "_" for x in row))