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
import random, util

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
        '''
        # we consider the left food amount+food distances+ghost distances as the factors of the evaluation function
        newfoodList = newFood.asList()
        closestFood = float("inf")
        for foodPos in newfoodList:
          closestFood = min(util.manhattanDistance(newPos, foodPos), closestFood)
        foodScore = 1.0/closestFood

        ghostPositions = [ghostState.getPosition() for ghostState in newGhostStates]
        closestGhost = min([util.manhattanDistance(ghostPos, newPos) for ghostPos in ghostPositions])

        # the evaluation function:
        score = foodScore - len(newfoodList)
        # if the ghosts are in the scared time, the pacman will ignore all the ghosts
        if newScaredTimes[0] == 0:
          if closestGhost == 0:
            return -float("inf")
          if closestGhost <=3:
            score -= 4.0/closestGhost
        '''
        print 'wonderful music'
        #return score

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

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
        return self.MinimaxSearch(gameState, self.depth, 0)

    def MinimaxSearch(self, gameState, curDepth, agentIndex):
      # terminal test:if it is clear who wins/loses or reach the leaf node
      if gameState.isWin() or gameState.isLose() or curDepth == 0:
        return self.evaluationFunction(gameState)
      
      # store each legal action except for STOP from the list of legal moves
      actions = [action for action in gameState.getLegalActions(agentIndex) if action!='Stop']
      
      # update agentindex and nextdepth
      nextIndex = agentIndex + 1
      nextDepth = curDepth
      if nextIndex >= gameState.getNumAgents():   # if all the opponents responded, then move to the next depth 
        nextIndex = 0
        nextDepth -= 1
      
      # pacman moves first
      if agentIndex == 0 and curDepth == self.depth:
        bestAction = Directions.STOP
        maxVal = -float("inf")
        
        # get the maximum value supplied by #1 opponet at the current depth
        for action in actions:
          val = self.MinimaxSearch(gameState.generateSuccessor(0, action), self.depth, 1)
          if val > maxVal:
            maxVal = val
            bestAction = action   # choose the action corresponding to the largest min values
        return bestAction    

      else:
      #store all the values that the next agent supplies by each action
        results = [self.MinimaxSearch(gameState.generateSuccessor(agentIndex, action), nextDepth, nextIndex) for action in actions]
        if agentIndex == 0:
          return max(results)    # pacman gets the largest number of the values
        else:
          return min(results)    # opponents get the smallest number of the values
    
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        return self.AlphaBeta(gameState, self.depth, 0, -float("inf"), float("inf"))

    def AlphaBeta(self, gameState, curDepth, agentIndex, alpha, beta):
      # terminal test:if it is clear who wins/loses or reach the leaf node
      if gameState.isWin() or gameState.isLose() or curDepth == 0:
        return self.evaluationFunction(gameState)
      
      # store each legal action except for STOP from the list of legal moves
      actions = [action for action in gameState.getLegalActions(agentIndex) if action!='Stop']
      
      # update agentindex and nextdepth
      nextIndex = agentIndex + 1
      nextDepth = curDepth
      if nextIndex >= gameState.getNumAgents(): # if all the opponents responded, then move to the next depth
        nextIndex = 0
        nextDepth -= 1
      
      # pacman moves first
      if agentIndex == 0 and curDepth == self.depth:
        bestAction = Directions.STOP
        maxVal = -float("inf")


        # get the maximum value supplied by #1 opponet at the current depth
        for action in actions:
          val = self.AlphaBeta(gameState.generateSuccessor(0, action), self.depth, 1, alpha, beta)
          if val > maxVal:
            maxVal = val
            bestAction = action
        return bestAction

      else:
        if agentIndex == 0:
          maxVal = -float("inf")
          for action in actions:
            val = self.AlphaBeta(gameState.generateSuccessor(agentIndex, action), nextDepth, nextIndex, alpha, beta)
            if val > maxVal:
              maxVal = val      # get the maximum value of all the results
            if maxVal >= beta:  # only consider the value larger than beta value
              return maxVal
            alpha = max(alpha, maxVal)
          return maxVal
        else:
          minVal = float("inf")
          for action in actions:
            val = self.AlphaBeta(gameState.generateSuccessor(agentIndex, action), nextDepth, nextIndex, alpha, beta)
            if val < minVal:
              minVal = val  # get the minimum value of all the results
            if minVal <= alpha: # only consider the value smaller than alpha value
              return minVal
            beta = min(beta, minVal)
          return minVal    
          
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

