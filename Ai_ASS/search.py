from collections import deque
import heapq


class Node:
    """
    Search tree/graph node.

    A node stores:
        state:
            The problem state represented by this node.

        parent:
            The parent node in the search tree/graph.
            The root node has parent = None.

        action:
            The action that was applied to the parent state to reach this node.
            The root node has action = None.

        depth:
            The depth of the node in the search tree/graph.
            The root node has depth = 0.

        path_cost:
            The total path cost from the initial state to this node.
    """
    def __init__(self, state, parent=None, action=None, path_cost=0, depth=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.path_cost = path_cost


class SearchResult:
    """
    Search result returned by a search algorithm.

    actions:
        The sequence of actions from the initial state to the goal state.

    states:
        The sequence of states from the initial state to the goal state.

    depth:
        The depth of the goal node, i.e. the number of actions in the solution.

    cost:
        The total path cost of the solution.

    expanded_order:
        The states in the order in which they were expanded
        (i.e. removed from the fringe and processed).
    """
    def __init__(self, actions, states, depth, cost, expanded_order):
        self.actions = actions
        self.states = states
        self.depth = depth
        self.cost = cost
        self.expanded_order = expanded_order

    def __str__(self):
        """
        For printing a search result in an easy-to-read form.
        """
        lines = []
        lines.append(f"Actions: {self.actions}")
        lines.append(f"Depth: {self.depth}")
        lines.append(f"Cost: {self.cost}")
        lines.append("States:")
        for state in self.states:
            lines.append(str(state))
        lines.append("Expanded order:")
        for state in self.expanded_order:
            lines.append(str(state))
        return "\n".join(lines)
    
    
def extract_solution(node):
    """
    Extract the solution represented by a goal node.

    Returns:
        actions:
            The list of actions from the root to the given node.

        states:
            The list of states from the root to the given node.
    """
    actions = []
    states = []

    while node is not None:
        states.append(node.state)
        if node.action is not None:
            actions.append(node.action)
        node = node.parent

    actions.reverse()
    states.reverse()

    return actions, states


def expand(problem, node):
    """
    Expand a node using the problem successor function.
    """
    children = []
    for action, next_state in problem.get_successors(node.state):
        cost = problem.step_cost(node.state, action, next_state)
        child = Node(
            state=next_state,
            parent=node,
            action=action,
            path_cost=node.path_cost + cost,
            depth=node.depth + 1
        )
        children.append(child)
    return children


class DFSFringe:
    """
    Depth-first-search fringe.

    This is a LIFO fringe:
        the most recently inserted node is removed first.
        
    The constructor creates a list containing the initial node.
    
    Note:
        The representation is reversed: the end of the list is 
        treated as the front of the fringe.
    """
    def __init__(self, initial_node):
        self.nodes = [initial_node]

    def empty(self):
        """
        Return True if and only if the fringe is empty.
        """
        return len(self.nodes) == 0

    def remove_first(self):
        """
        Remove and return the first node in the fringe 
        (last node in the list).
        """
        return self.nodes.pop()

    def insert(self, node):
        """
        Insert a node into the fringe (added to the end of the list).
        """
        self.nodes.append(node)
        
        
class BFSFringe:
    """
    Breadth-first-search fringe.

    This is a FIFO fringe:
        the earliest inserted node is removed first.

    The constructor creates a double-ended queue (deque)
    containing the initial node.
    """
    def __init__(self, initial_node):
        self.queue = deque([initial_node])

    def empty(self):
        return len(self.queue) == 0

    def remove_first(self):
        return self.queue.popleft()

    def insert(self, node):
        self.queue.append(node)


class UCSFringe:
    """
    Uniform-cost-search fringe.

    Nodes are ordered by path cost.
    Nodes with equal path cost should follow insertion order (FIFO).

    The constructor creates an empty heap, initializes the insertion counter,
    and inserts the initial node.
    """
    def __init__(self, initial_node):
        self.heap = []
        self.counter = 0
        self.insert(initial_node)

    def empty(self):
        return len(self.heap) == 0

    def remove_first(self):
        _, _, node = heapq.heappop(self.heap)
        return node

    def insert(self, node):
        heapq.heappush(self.heap, (node.path_cost, self.counter, node))
        self.counter += 1


class AstarFringe:
    """
    A* fringe.

    Nodes are ordered by:
        1. f = g + h
        2. h
        3. insertion order

    where:
        g is the path cost of the node
        h is the heuristic value of the node state

    The constructor stores the heuristic function, initializes the heap and
    insertion counter, and inserts the initial node.
    """
    def __init__(self, initial_node, heuristic):
        self.heap = []
        self.counter = 0
        self.heuristic = heuristic
        self.insert(initial_node)

    def empty(self):
        return len(self.heap) == 0

    def remove_first(self):
        _, _, _, node = heapq.heappop(self.heap)
        return node

    def insert(self, node):
        h = self.heuristic(node.state)
        f = node.path_cost + h
        heapq.heappush(self.heap, (f, h, self.counter, node))
        self.counter += 1


def graph_search(problem, fringe):
    """
    General graph search.
    """
    closed_list = set()
    expanded_order = []

    while not fringe.empty():
        node = fringe.remove_first()

        if node.state in closed_list:
            continue

        if problem.is_goal(node.state):
            actions, states = extract_solution(node)
            return SearchResult(actions, states, node.depth, node.path_cost, expanded_order)

        closed_list.add(node.state)
        expanded_order.append(node.state)

        for child in expand(problem, node):
            if child.state not in closed_list:
                fringe.insert(child)

    return SearchResult([], [], 0, float("inf"), expanded_order)


def dfs(problem):
    """
    Run depth-first graph search on the given problem.
    """
    initial_node = Node(problem.initial_state)
    fringe = DFSFringe(initial_node)
    return graph_search(problem, fringe)

def bfs(problem):
    """
    Run breadth-first graph search on the given problem.
    """
    initial_node = Node(problem.initial_state)
    fringe = BFSFringe(initial_node)
    return graph_search(problem, fringe)


def ucs(problem):
    """
    Run uniform-cost graph search on the given problem.
    """
    initial_node = Node(problem.initial_state)
    fringe = UCSFringe(initial_node)
    return graph_search(problem, fringe)


def astar(problem):
    """
    Run A* graph search on the given problem.
    """
    initial_node = Node(problem.initial_state)
    fringe = AstarFringe(
        initial_node,
        problem.heuristic
    )
    return graph_search(problem, fringe)