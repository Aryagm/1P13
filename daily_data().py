# from passenger_data, passenger_data(): this function is used to read from the passenger_data.txt 
# [[Passenger 1 name, First letter of last name, Gate,
# Seating class, Destination, Arrival status, Baggage weight,
# Layover status], [Passenger 2 name,...etc.],...etc.]

def daily_data(passenger_data):
    '''Expected output: 2D list that has the gate, the number of business
    passengers and the number of economy passengers'''

    for passenger in passenger_data:
        business_seats = 0
        economy_seats = 0 

    # depends on the ordinal number of passenger data list but for ex. gate = 3, and seating class = 4
        gate = passenger[3] # says that gate is the 3rd index in passenger list
        seating_class = passenger[4]

        if seating_class == "business":
            business_seats += 1
        elif seating_class == "economy":
            economy_seats += 1

    daily_data_list = [["Gate, ", gate, "Number of business pasengers, ", business_seats, "Number of economy passengers, ", economy_seats]]

    return daily_data_list



