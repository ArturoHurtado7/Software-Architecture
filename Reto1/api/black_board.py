
class BlackBoard(object):

    def __init__(self):
        self.common_state = {
            'warning': self.get_warning_emails(),
            'danger': self.get_danger_emails(),
        } | self.get_range()

    def get_warning_emails(self):
        """
        Returns the warning emails
        """
        warning_emails = [
            'cco@ccs.com',
            'admin@ccs.com'
        ]
        return warning_emails
    
    def get_danger_emails(self):
        """
        Returns the danger emails
        """
        danger_emails = [
            'cco@ccs.com',
            'admin@ccs.com',
            'policia@colombia.gov.co',
            'emergencias@colombia.gov.co'
        ]
        return danger_emails
    
    def get_range(self):
        """
        Returns the ranges
        """
        return {
            'temperature': {'normal': 0, 'warning': 30, 'emergency': 40},
            'speed': {'normal': 0, 'warning': 60, 'emergency': 100},
            'planned_stops': {'normal': 0, 'warning': 60, 'emergency': 100},
            'non_planned_stops': {'normal': 0, 'warning': 20, 'emergency': 40}
        }

board = BlackBoard()