# valueIterationAgents.py
# -----------------------
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
# @ author Sanay Devi svdevi Arizona State University


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Value iteration code here
        state = self.mdp.getStates()[2]
        nextState = mdp.getTransitionStatesAndProbs(state, mdp.getPossibleActions(state)[0])
        states = self.mdp.getStates()
        for i in range(iterations):
            values_copy = self.values.copy()
            for state in states:
                final_reward = None
                for action in self.mdp.getPossibleActions(state):
                    currentValue = self.computeQValueFromValues(state, action)
                    if final_reward == None or final_reward < currentValue:
                        final_reward = currentValue
                if final_reward == None:
                    final_reward = 0
                values_copy[state] = final_reward
            self.values = values_copy

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    # returns the Q-value of the (state, action) pair given by the value function given by self.values.

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        value = 0
        tStateAction = self.mdp.getTransitionStatesAndProbs(state, action)
        for nextState, probability in tStateAction:
            value += probability * (self.mdp.getReward(state, action, nextState)
                                    + (self.discount * self.values[nextState]))
        return value

    # Computes Best Action according to value function given in self.values

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        possibleActions = self.mdp.getPossibleActions(state)

        if len(possibleActions) == 0:
            return None
        value = None
        result = None
        for action in possibleActions:
            temp_val = self.computeQValueFromValues(state, action)
            if value is None or temp_val > value:
                value = temp_val
                result = action
        return result

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
