__author__ = 'bkurniawan'
from rlagents.rl_agent.base_agent import BaseAgent
class RewardShapingAgent(BaseAgent):
    actions = [ 'change_speed_by_percentage(-10)', 'change_speed_by_percentage(10)']
    def __init__(self, params_filename=None):
    def get_q(self):
    def tick(self, t, dt):
    def get_reward(self, prev_state, prev_action, state):
    def learn(self, t, dt):
    def log(self, my_state, threat_state, t, dx, reward, prev_state_action, old_value, new_value, q, max_q, max_q_sa):
    def test(self, t, dt):