def overweight(passenger_data, fleet_data):
    """
    Calculate overweight baggage for passengers and track overweight counts per aircraft.
    Takes passenger data and fleet data as input and returns two lists:
    - A list of passenger data with overweight baggage amounts
    - A list of aircraft models and overweight counts
    """
    passenger_output = []
    fleet_output = []
    
    # Initialize fleet output with unique plane models and zero overweight counts
    for plane in fleet_data:
        plane_model = plane[0]
        if [plane_model] not in fleet_output:
            fleet_output.append([plane_model, 0])

    # Process each passenger
    for passenger in passenger_data:
        gate = passenger[2]
        plane_model = None
        max_weight = None
        overweight = None
        
        # Find matching plane and max baggage weight for passenger's gate
        for plane in fleet_data:
            if plane[4] == gate:
                plane_model = plane[0]
                max_weight = plane[7]

        # Calculate overweight amount and update fleet counters
        if passenger[6] > max_weight:
            overweight = round(float(passenger[6]) - float(max_weight), 1)
            for plane in fleet_output:
                if plane_model == plane[0]:
                    plane[1] += 1
        else:
            overweight = 0
        
        # Add passenger result to output
        passenger_output.append([passenger[0], passenger[1], passenger[2], overweight])
    
    return passenger_output, fleet_output
