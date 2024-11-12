def oversold(passenger_list, fleet_list, daily_data_list):
    """
Returns 2D list of the model of the plane and the # of economy and bussiness passengers 
with oversold seats for each for in each flight.
    """
    oversold_business = []
    oversold_economy = []

    for data in daily_data_list:
        #get gate, business & economy info from daily data
        gate = data[0]
        business_count = data[1]
        economy_count = data[2]
        
        for plane in fleet_list:
            if plane[4] == gate: #check if plane matches the gate
                #get business & economy capacity from plane data
                business_capacity = int(plane[1])
                economy_capacity = int(plane[2])
                
                business_oversold = max(0, business_count - business_capacity)
                economy_oversold = max(0, economy_count - economy_capacity)
                
                if business_oversold > 0:
                    oversold_business.append([plane[0], business_oversold])
                if economy_oversold > 0:
                    oversold_economy.append([plane[0], economy_oversold])
                
                break 
            
    return oversold_business, oversold_economy
