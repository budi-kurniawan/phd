__author__ = 'bkurniawan'
class EligibilityTracesAgent9(EligibilityTracesAgent7):
    Extends EligibilityTracesAgent7 that uses a less 'generous' reward function and 
    use 5 actions instead of 2
    """
    def __init__(self, params_filename=None):
        super(EligibilityTracesAgent9, self).__init__()
               'change_speed_by_percentage(10)', 'change_speed_by_percentage(20)']