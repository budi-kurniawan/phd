__author__ = 'bkurniawan'
class BaseAgent(Agent):
    # how many consecutive times the agent has been in a goal zone 
    # support for eligibility traces
    def get_my_callsign(self):
        other_y = self.beliefs.threat_state.y
    def get_table_value(self, table, state_action):
    def execute_action(self, action):