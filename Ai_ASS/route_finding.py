class RouteFindingProblem:
    """
    Route-finding problem definition.

    State representation:
        A state is a city name, represented as a string, for example:
            "Arbor"
            "Haven"

    Data provided to the constructor:
        roads:
            A dictionary representing the road network.

            roads[city] is a list of pairs:
                (neighbor_city, distance)

            Example:
                roads["Arbor"] = [("Brook", 3), ("Cedar", 3)]

        locations:
            A dictionary giving 2D coordinates for each city
            (used for the straight-line-distance heuristic).

            locations[city] = (x, y)

            Example:
                locations["Arbor"] = (0, 4)

        initial_state:
            The start city.

        goal_state:
            The destination city.
            
    Route data:
        You are provided with two roads and locations dictionaries in 
        route_data_small.py and route_data_large.py, which you can import 
        and provide to the constructor. You can also create your own 
        route_data file for testing your implementation.            
    """

    def __init__(self, roads, locations, initial_state, goal_state):
        self.roads = roads
        self.locations = locations
        self.initial_state = initial_state
        self.goal_state = goal_state

    def is_goal(self, state):
        """
        Return True if and only if the given state is the goal state.
        """
        return state == self.goal_state

    def get_successors(self, state):
        """
        Return the successors of the given state as a list of pairs:
            (action, next_state)
        """
        successors = []
        for neighbor, distance in self.roads[state]:
            action = f"go({neighbor})"
            successors.append((action, neighbor))
        return successors

    def step_cost(self, state, action, next_state):
        """
        Return the cost of taking the given action from state to next_state.
        """
        for neighbor, distance in self.roads[state]:
            if neighbor == next_state:
                return distance
        raise ValueError(f"No road from {state} to {next_state}")

    def heuristic(self, state):
        """
        Return the straight-line (Euclidean) distance from the current city 
        to the goal city.
        """
        x1, y1 = self.locations[state]
        x2, y2 = self.locations[self.goal_state]
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def print_state(state):
    """
    Print a state in an easy-to-read form.
    """
    print(state)