def oversold(passenger_list, fleet_list, daily_data_list):
    """
Calculate the number of oversold business & economy seats for each flight based on fleet and daily data. 
Returns two 2D lists of oversold business seats & oversold economy seats containing the 
plane model & oversold seat count.
    """
    #initialize lists to store info for oversold seats in each class
    oversold_business = []
    oversold_economy = []

    for data in daily_data_list:
        #get gate, business & economy info from daily data
        gate = data[0]
        business_count = data[1]
        economy_count = data[2]
        
        for plane in fleet_list:
            if plane[4] == gate: #check if plane matches the gate in fleet_list & daily_data_list
                #get business & economy capacity for the plane
                business_capacity = int(plane[1])
                economy_capacity = int(plane[2])

                #calculate oversold seats for bussiness and economy
                business_oversold = business_count - business_capacity
                economy_oversold = economy_count - economy_capacity

                #append plane model and count to the respective list
                if business_oversold > 0:
                    oversold_business.append([plane[0], business_oversold])
                if economy_oversold > 0:
                    oversold_economy.append([plane[0], economy_oversold])
                
                break 
            
    return oversold_business, oversold_economy
