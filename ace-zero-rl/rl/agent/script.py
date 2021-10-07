__author__ = 'bkurniawan'from rl.agent.base_agent import BaseAgent
from .. import rl_utilsclass ScriptAgent(BaseAgent):    """    This class represents an opposing agent that can be controlled through a json file.    """    def __init__(self, params_filename=None):        super(ScriptAgent, self).__init__()        if params_filename:            self.steps = params_filename['steps'] if 'steps' in params_filename else None    def tick(self, t, dt):        super().tick(t, dt) # must call super to log and empty commands        if self.steps:            for step in self.steps:                if t == step['t']:                    exec('self.' + step['action'])