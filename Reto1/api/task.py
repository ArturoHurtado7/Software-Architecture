from api.schemas import CentralSchema
from api.black_board import BlackBoard

def process(board: BlackBoard, request: CentralSchema) -> dict:
    """
    Processes the task
    """
    # local variables
    emergencies = []
    warnings = []
    attributes = {
        'speed': request.truck.speed,
        'planned_stops': request.truck.stops.planned,
        'non_planned_stops': request.truck.stops.non_planned,
        'temperature': request.shipment.temperature
    }

    # passthrough emergencies
    if request.panic:
        emergencies.append('panic')
    if request.shipment.state:
        emergencies.append('status')

    # process attributes and ranges
    for attribute, value in attributes.items():
        # attribute black board variables
        attribute_ranges = board.common_state.get(attribute)
        emergency_value = attribute_ranges.get('emergency')
        Warning_value = attribute_ranges.get('warning')

        # attribute processing
        if value > emergency_value:
            emergencies.append(attribute)
            continue
        elif value > Warning_value:
            warnings.append(attribute)

    return {'warnings': warnings, 'emergencies': emergencies}
