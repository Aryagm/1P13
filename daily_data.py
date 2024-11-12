def daily_data(passenger_data):
    '''Expected output: 2D list that has the gate, the number of business
    passengers and the number of economy passengers'''
    daily_data_list = []
    gates = [] # ensures no repeats

    for passenger in passenger_data:
        business_seats = 0
        economy_seats = 0 
    
    for passenger in passenger_list:
        gate = passenger[2]
        if gate not in gates:
            gates.append(gates)
            daily_data_list.append([gate, 0 ,0])
    
    # depends on the ordinal number of passenger data list but for ex. gate = 3, and seating class = 4
    for passenger in passenger_list:
        gate = passenger[2] # says that gate is the 3rd index in passenger list
        seating_class = passenger[3]

        for data in daily_data_list:
            if seating_class == "B":
                business_seats += 1
            elif seating_class == "E":
                economy_seats += 1
            break

    return daily_data_list



