__author__ = 'bkurniawan'
from rl.agent.eligibility_traces7 import EligibilityTracesAgent7
from rl import rl_utils
# 2D agent using Q-learning
    def __init__(self, params_filename=None):
    actions = ['no_command', 'change_speed_by_percentage(-10)', 'change_speed_by_percentage(10)', 
    def calculate_t(self, reward):
    def is_terminal(self, state):
    def is_in_goal(self, state):
    def get_state(self, entity_state, threat_state):
    def get_reward(self, state):

    def log(self, t, reward, prev_state_action, q, e):