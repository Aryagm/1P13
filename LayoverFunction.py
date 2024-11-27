def layover(passengerList, fleetList):
    """Calculates the number of passengers with layover status, counts them and assigns that number to a plane. 
    Next it creates a list of passengers with the layover status and their associated gate info.
    Function accepts 2 lists, and returns 2 lists"""
    planeLayover = [] #creating lists to return
    passengerGate = []
    for plane in fleetList:  #for every plane in the fleetList list 
        plane_model = plane[0] #get the model of the plane and gate
        gate = plane[4]
        layover_count = 0  
        
        for passenger in passengerList: #for every passenger in the passengerList check if their gate matches up with the plane and if they have the layover status
            if passenger[2] == gate and passenger[7] == "Layover":  #if yes add 1 to the counter
                layover_count += 1  
                
        planeLayover.append([plane_model, layover_count])  
    
    for passenger in passengerList: #check every passenger for the layover status and if they have it add their first, last name and gate 
        if passenger[7] == "Layover":
            passengerGate.append([passenger[0], passenger[1], passenger[2]])
    return planeLayover, passengerGate #returning the 2 lists


print(layover(data1, data2))
