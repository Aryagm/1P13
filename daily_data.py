def daily_data(passenger_list):
    '''Expected output: 2D list that has the gate, the number of business
    passengers and the number of economy passengers'''
    daily_data_list = [] #list to store data for each gate w counts for business & economy passengers
    gates = [] #check if gate has already been added

    #initialize business & economy counts for each
    for passenger in passenger_list:
        gate = passenger[2]
        if gate not in gates:
            gates.append(gate)
            daily_data_list.append([gate, 0, 0]) #format[gate, business_count, economy_count]

    #count business & economy passengers per gate
    for passenger in passenger_list: 
        gate = passenger[2]
        seating_class = passenger[3]

        #find the entry for the gate in daily_data_list
        for data in daily_data_list:
            if data[0] == gate: #check if this entry matches the gate
                if seating_class == 'B':  #add 1 based on seating class
                    data[1] += 1
                elif seating_class == 'E':
                    data[2] += 1
                break

    return daily_data_list



