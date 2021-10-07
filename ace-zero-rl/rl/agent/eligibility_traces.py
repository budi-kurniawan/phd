__author__ = 'bkurniawan'
from rl.agent.base_agent import BaseAgent

class EligibilityTracesAgent(BaseAgent):
    https://stackoverflow.com/questions/40862578/how-to-understand-watkinss-q%CE%BB-learning-algorithm-in-suttonbartos-rl-book
    
    Do not use http://www-anw.cs.umass.edu/~barto/courses/cs687/Chapter%207.pdf (wrong)
    We want to get between 500 and 3000 feet. (500feet is about 152m
    max_q = 0
    def __init__(self, params_filename=None):
    def get_q(self):
        return rl_utils.context.q
    def get_e(self):
        return rl_utils.context.e

    def get_reward(self, state):
            greedy = action == greedy_action
            delta = reward + EligibilityTracesAgent.GAMMA * q1 - q0
    
    def get_q_value(self, state_action):
        q = self.get_q()
        return q[state_action] if state_action in q else 0
    
    def update_q_value(self, state_action, value):
        q = self.get_q()
        q[state_action] = value
        
    def get_action_with_max_value(self, state):
        q = self.get_q()
        return super().get_action_with_max_q_value(q, state)
    
    def get_explore_or_exploit_action(self, epsilon, state):
        q = self.get_q()
        return self.get_explore_exploit_action(epsilon, q, state)
    