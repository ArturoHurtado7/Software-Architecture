from api.schemas import CentralSchema
from api.params import Params
from time import time

class Task(object):
    def __init__(self, params: Params, request: CentralSchema, start_time: float):
        self.params = params.common_state
        self.request = request
        self.start_time = start_time
        self.danger = []
        self.warnings = []
        self.attributes = {
            'speed': self.request.truck.speed,
            'planned_stops': self.request.truck.stops.planned,
            'non_planned_stops': self.request.truck.stops.non_planned,
            'temperature': self.request.shipment.temperature
        }


    def priority(self):
        """
        Priority of the task
        """
        if self.request.panic:
            self.danger.append('panic')
            self.notify()
        else:
            self.classify()


    def classify(self):
        """
        Classify the task in danger or warning
        """
        # validate danger & warnings
        if self.request.shipment.state:
            self.danger.append('status')

        # process attributes and ranges
        for attribute, value in self.attributes.items():
            # attribute black params variables
            ranges = self.params.get(attribute)
            danger = ranges.get('danger')
            warning = ranges.get('warning')

            # attribute processing
            if value > danger:
                self.danger.append(attribute)
            elif value > warning:
                self.warnings.append(attribute)

        # notify
        if len(self.danger) > 0:
            self.notify()
        elif len(self.warnings) > 0:
            self.notify()
        else:
            self.save()


    def notify(self):
        """
        Notify the user
        """
        if len(self.danger) > 0:
            print('send email to: ', self.params.get('danger'), str(self.danger))
        elif len(self.warnings) > 0:
            print('send email to: ', self.params.get('warning'), str(self.warnings))
        self.save()


    def save(self):
        """
        Save the data
        """
        total_time = time() - self.start_time
        print('time', total_time)

