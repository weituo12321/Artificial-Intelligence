# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util,sys

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        #print successorGameState
        #print newPos
        #print newFood
        #print newGhostStates
        #print newScaredTimes

        "*** YOUR CODE HERE ***"        
        # get positions of each ghost
        newGhostPositions = [ghostState.getPosition() for ghostState in newGhostStates]
        # get the min distance between the ghosts and pacman
        ghost_pacman = min([util.manhattanDistance(ghost_position, newPos) for ghost_position in newGhostPositions])
        newFood_list = newFood.asList()
        # find the distance between the pacman and the closest food
   
        min_food_pacman =float("inf")
        for food in newFood_list:
          temp_dis = util.manhattanDistance(newPos, food)
          min_food_pacman=min(min_food_pacman,temp_dis)
        
        # the evaluation function: 
        # score = 1.0/distance between the pacman and the closest food - amount of food left - 4.0/distance between the pacman and the closest ghost
        score = 1.0/min_food_pacman-len(newFood_list)
        # if the ghosts are in the scared time, the pacman will ignore all the ghosts
        if newScaredTimes[0] == 0:
          if ghost_pacman == 0:
            return -float("inf")
          if ghost_pacman < 3:
            score -= 4.0/ghost_pacman
        return score
    

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displaye        return self.MinimaxSearch(gameState, self.depth, 0 )

    def MinimaxSearch(self, gameState, currentDepth, agentIndex):
      "terminal check"
      if gameState.isWin() or gameState.isLose() or currentDepth == 0:
        return self.evaluationFunction(gameState)
      
      "minimax algorithm"
      legalMoves = [action for action in gameState.getLegalActions(agentIndex) if action!='Stop']
      
      # update next depth and next index
      nextIndex = agentIndex + 1
      nextDepth = currentDepth
      if nextIndex >= gameState.getNumAgents():
        nextIndex = 0
        nextDepth -= 1
      
      # Choose one of the best actions or keep query the minimax result
      results = [self.MinimaxSearch(gameState.generateSuccessor(agentIndex, action), nextDepth, nextIndex) for action in legalMoves]
      
      if agentIndex == 0 and currentDepth == self.depth:
        return max([self.MinimaxSearch(gameState.generateSuccessor(0, action), self.depth, 1) for action in legalMoves])
      if agentIndex == 0:  
        return max(results)
      else:
        return min(results)d in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        '''
        # Return action leads to the outcome with best utility
        bestValue = -(float("inf"))
        bestAction = Directions.STOP
        legalMoves = gameState.getLegalActions(0)
        
        # Remove stop action to increase the search depth achievable by our agent
        if Directions.STOP in legalMoves:
          legalMoves.remove(Directions.STOP)
        for action in legalMoves:
          tempValue=self.minValue(self.depth,1,gameState.generateSuccessor(0,action))
          if tempValue>bestValue:
            bestValue=tempValue
            bestAction=action
        return bestAction
    def minValue(self,depth,agentIndex,gameState):
      if gameState.isWin() or gameState.isLose() or depth==0:
        return self.evaluationFunction(gameState)
      else:
        actions=gameState.getLegalActions(agentIndex)
        bestValue=float("inf")
        for action in actions:
          if agentIndex==gameState.getNumAgents()-1:
            tempValue=self.maxValue(depth-1,0,gameState.generateSuccessor(agentIndex,action))
            tempValue=min(tempValue,bestValue)
          else:
            tempValue=self.minValue(depth,agentIndex+1,gameState.generateSuccessor(agentIndex,action))
            tempValue=min(tempValue,bestValue)
        return bestValue


    def maxValue(self,depth,agentIndex,gameState):
      if gameState.isWin() or gameState.isLose() or depth==0:
        return self.evaluationFunction(gameState)
      else:
        actions=gameState.getLegalActions(agentIndex)
        if Directions.STOP in actions:
          actions.remove(Directions.STOP)
        bestValue=-(float("inf"))
        for action in actions:
          tempValue=self.minValue(depth-1,agentIndex+1,gameState.generateSccucessor(agentIndex,action))
          tempValue=max(tempValue,bestValue)
        return bestValue
        '''
        return self.MinimaxSearch(gameState, self.depth, 0)

    def MinimaxSearch(self, gameState, currentDepth, agentIndex):
      "terminal check"
      if gameState.isWin() or gameState.isLose() or currentDepth == 0:
        return self.evaluationFunction(gameState)
      
      "minimax algorithm"
      legalMoves = [action for action in gameState.getLegalActions(agentIndex) if action!=Directions.STOP]
      
      # update next depth and next index
      nextIndex = agentIndex + 1
      nextDepth = currentDepth
      if nextIndex >= gameState.getNumAgents():
        nextIndex = 0
        nextDepth -= 1
      
      # Choose one of the best actions or keep query the minimax result
      results = [self.MinimaxSearch(gameState.generateSuccessor(agentIndex, action), nextDepth, nextIndex) for action in legalMoves]
      
      if agentIndex == 0 and currentDepth == self.depth:  
        bestMove = max(results)
        for index in range(len(results)):
          if results[index] == bestMove:
            return legalMoves[index]
        #chosenIndex = random.choice(bestIndices) # Pick randomly among the best
        #print 'pacman %d' % bestMove
        #return legalMoves[bestIndices[0]]
    
        
      if agentIndex == 0:  
        return max(results)
      else:
        return min(results)
      


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
    """
      Your agent for the mini-contest
    """

    def getAction(self, gameState):
        """
          Returns an action.  You can use any method you want and search to any depth you want.
          Just remember that the mini-contest is timed, so you have to trade off speed and computation.

          Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
          just make a beeline straight towards Pacman (or away from him if they're scared!)
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

