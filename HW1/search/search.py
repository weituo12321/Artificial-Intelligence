# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     return graph_search(problem, Stack())    required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]


def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  # for display purpose
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:",problem.getSuccessors(problem.getStartState())

  # use Stack for DFS
  frontier=util.Stack()
  frontier.push((problem.getStartState(),[],0))
  explored=[]
  while frontier:
    present_node=frontier.pop()
    if problem.isGoalState(present_node[0]):
      return present_node[1]
    if present_node[0] not in explored:
      explored.append(present_node[0])
      child_nodes=problem.getSuccessors(present_node[0])
      for child_node in child_nodes:
        path=present_node[1]+[child_node[1]]
        cost=child_node[2]
        frontier.push((child_node[0],path,cost))
  return []
  util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  # for display purpose
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:",problem.getSuccessors(problem.getStartState())

  # use Queue for BFS
  frontier=util.Queue()
  frontier.push((problem.getStartState(),[],0))
  explored=[]
  while frontier:
    present_node=frontier.pop()
    if problem.isGoalState(present_node[0]):
      return present_node[1]
    if present_node[0] not in explored:
      explored.append(present_node[0])
      child_nodes=problem.getSuccessors(present_node[0])
      for child_node in child_nodes:
        path=present_node[1]+[child_node[1]]
        cost=child_node[2]
        frontier.push((child_node[0],path,cost))
  return [] 
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  # for display purpose
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  
  # use PriorityQueue for UCS
  frontier=util.PriorityQueue()
  frontier.push((problem.getStartState(),[],0),0)
  explored=[]
  cost_dict={}
  while frontier:
    present_node=frontier.pop()
    if problem.isGoalState(present_node[0]):
      return present_node[1]
    else:
      explored.append(present_node[0])  
      child_nodes=problem.getSuccessors(present_node[0])
      for child_node in child_nodes:
        if child_node[0] not in explored:
          solution=present_node[1]+[child_node[1]]
          path_cost=present_node[2]+child_node[2]
          if not cost_dict.has_key(child_node[0]):
            frontier.push((child_node[0],solution,path_cost),path_cost)
            cost_dict[child_node[0]]=path_cost
          elif cost_dict[child_node[0]]>path_cost:
            frontier.push((child_node[0],solution,path_cost),path_cost)
            cost_dict[child_node[0]]=path_cost
  return []
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  # for display purpose
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  

  # add a heuristic function based on the UCS
  frontier=util.PriorityQueue()
  frontier.push((problem.getStartState(),[],0),0)
  explored=[]
  cost_dict={}
  while frontier:
    present_node=frontier.pop()
    if problem.isGoalState(present_node[0]):
      return present_node[1]
    else:
      explored.append(present_node[0])  
      child_nodes=problem.getSuccessors(present_node[0])
      for child_node in child_nodes:
        if child_node[0] not in explored:
          solution=present_node[1]+[child_node[1]]
          step_cost=child_node[2]
          path_cost=present_node[2]+child_node[2]
          if not cost_dict.has_key(child_node[0]):
            frontier.push((child_node[0],solution,path_cost),path_cost+heuristic(child_node[0],problem))
            cost_dict[child_node[0]]=path_cost
          elif cost_dict[child_node[0]]>path_cost:
            frontier.push((child_node[0],solution,path_cost),path_cost+heuristic(child_node[0],problem))
            cost_dict[child_node[0]]=path_cost
  return []  
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
