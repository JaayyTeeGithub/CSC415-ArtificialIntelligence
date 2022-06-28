# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    # initialize the fringe stack and visited list
    fringe = util.Stack()
    visited = []
    # initialize the starting point and node
    # node format: (state, direction)
    point = problem.getStartState()

    # push the starting node and moves list onto the fringe stack
    # point, moves (to goal)
    fringe.push((point, []))

    # start depth first search with the start node
    while not fringe.isEmpty():
        node = fringe.pop()
        point = node[0]
        moves = node[1]

        if point not in visited:
            visited.append(point)

            if problem.isGoalState(point):
                return moves

            for state in problem.getSuccessors(point):
                add_point = state[0]
                move = state[1]
                add_moves = moves + [move]
                fringe.push((add_point, add_moves))

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # initialize fringe queue and visited list
    fringe = util.Queue()
    visited = []

    # initialize the starting point and node
    # node format: (state, direction)
    point = problem.getStartState()

    # push the starting node and moves list onto the fringe stack
    # point, moves (to goal)
    fringe.push((point, []))

    # start breadth first search with the start node
    while not fringe.isEmpty():
        node = fringe.pop()
        point = node[0]
        moves = node[1]

        if point not in visited:
            visited.append(point)

            if problem.isGoalState(point):
                return moves

            for state in problem.getSuccessors(point):
                add_point = state[0]
                move = state[1]
                add_moves = moves + [move]
                fringe.push((add_point, add_moves))

    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # initialize priority queue for fringe and visited list
    fringe = util.PriorityQueue()
    visited = []

    # initialize the starting point and node
    point = problem.getStartState()

    # push the starting node, moves list, and cost onto the fringe priority queue
    # (point, moves (to goal), cost), priority
    fringe.push((point, [], 0), 0)

    # start uniform cost search with start node
    while not fringe.isEmpty():
        node = fringe.pop()
        point = node[0]
        moves = node[1]
        costs = node[2]

        if point not in visited:
            visited.append(point)

            if problem.isGoalState(point):
                return moves

            for state in problem.getSuccessors(point):
                add_point = state[0]
                move = state[1]
                cost = state[2]
                add_moves = moves + [move]
                priority = costs + cost
                fringe.push((add_point, add_moves, priority), priority)

    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # initialize priority queue for fringe and visited list
    fringe = util.PriorityQueue()
    visited = []

    # initialize the starting point and node
    point = problem.getStartState()

    # push the starting node, moves list, and cost onto the fringe priority queue
    # (point, moves (to goal), cost), priority
    fringe.push((point, [], 0), 0)

    # start A* search with start node
    while not fringe.isEmpty():
        node = fringe.pop()
        point = node[0]
        moves = node[1]
        costs = node[2]

        if point not in visited:
            visited.append(point)

            if problem.isGoalState(point):
                return moves

            for state in problem.getSuccessors(point):
                add_point = state[0]
                move = state[1]
                cost = state[2]
                add_moves = moves + [move]
                add_costs = costs + cost
                add_heuristic = add_costs + heuristic(add_point, problem)
                fringe.push((add_point, add_moves, add_costs), add_heuristic)

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
