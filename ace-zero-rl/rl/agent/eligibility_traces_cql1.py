__author__ = 'bkurniawan'
class EligibilityTracesCQL1Agent(EligibilityTracesAgent):
    actions = [ 'no_command()', 'change_speed_by_percentage(-10)', 'change_speed_by_percentage(-20)', 'change_speed_by_percentage(-50)',
    def learn(self, t, dt):