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

# edited by @ Sanay Devi. asurite: svdevi PROJECT:1 ARTIFICIAL INTELLIGENCE CSE 572


import traceback
import util

class SearchProblem:

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
    return [w, w, w, w, w, w, w, w]


""" 
Q1. Depth First Search: Looks at the deepest Node first, has much lower memory requirements and uses Stacks. 
"""

def depthFirstSearch(problem):

    try:
        root = problem.getStartState()
        visited = set()
        # Stack because The DataStructure which DFS uses is LIFO Queue
        branch = util.Stack()
        branch.push((root, [], 0)) #Branch is the current fringe we are looking at.
        while not branch.isEmpty():
            location, path, cost = branch.pop()
            if problem.isGoalState(location):
                return path
            if location not in visited:
                visited.add(location)
                # For a given state, this should return a list of triples, (successor, action, stepCost)
                for succ, action, sCost in problem.getSuccessors(location):
                    if succ not in visited:
                        branch.push((succ, path + [action], sCost))
        return []
    except Exception :
        traceback.print_exc()
        return []

""" 
Q2. Breadth First Search: Will always look at the shallowest node, so it is quicker and uses FIFO queue.
"""

def breadthFirstSearch(problem):

    try:
        visited = list()
        root = problem.getStartState()
        #Queue because the DataStructure which BFS uses is FIFO queue
        branch = util.Queue()
        branch.push((root, [], 0))
        while not branch.isEmpty():
            location, path, cost = branch.pop()
            if problem.isGoalState(location):
                return path
            if location not in visited:
                visited.append(location)
                # For a given state, this should return a list of triples, (successor, action, stepCost)
                for succ, action, sCost in problem.getSuccessors(location):
                    if succ not in visited:
                        branch.push((succ, path + [action], sCost))
        return []
    except Exception :
        traceback.print_exc()
        return []

"""
 Q3. Uniform Cost Search: Will always find a path with minimum cost, uses Priority Queue. 
"""

def uniformCostSearch(problem):

    root = problem.getStartState()
    try:
        visited = list()
        branch = util.PriorityQueue()  #Branch is the current fringe we are looking at.
        branch.push((root, [], 0), 0)
        while not branch.isEmpty():
            location, path, cost = branch.pop()
            if problem.isGoalState(location):
                return path
            if location not in visited:
                visited.append(location)
                # For a given state, this should return a list of triples, (successor, action, stepCost)
                for succ, action, sCost in problem.getSuccessors(location):
                    if succ not in visited:
                        branch.push((succ, path + [action], sCost+cost), sCost+cost)
        return []
    except Exception :
        traceback.print_exc()
        return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

""" 
Q4. A* Search uses Forward and Backward Cost to estimate the best path 
"""

def aStarSearch(problem, heuristic=nullHeuristic):


    try:
        root = problem.getStartState()
        visited = list()
        branch = util.PriorityQueue()
        branch.push((root, [], 0), 0)
        while not branch.isEmpty():
            location, path, cost = branch.pop()
            if problem.isGoalState(location):
                return path
            if location not in visited:
                visited.append(location)
                # For a given state, this should return a list of triples, (successor, action, stepCost)
                for succ,action,sCost in problem.getSuccessors(location):
                    if succ not in visited:
                        backwardCost = sCost + cost
                        forwardCost = heuristic(succ, problem)
                        estimatedCost = backwardCost+forwardCost
                        branch.push((succ, path + [action], backwardCost), estimatedCost)
        return []
    except Exception :
        traceback.print_exc()
        return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
