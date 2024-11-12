def layover(passengerList, fleetList):
    PlaneLayover = []
    PassengerGate = []
    for plane in fleetList:
        plane_model = plane[0]
        gate = plane[4]
        layover_count = 0  
        
        for passenger in passengerList:
            if passenger[2] == gate and passenger[7] == "Layover":
                layover_count += 1  
                
        PlaneLayover.append([plane_model, layover_count])  
    
    for passenger in passengerList:
        if passenger[7] == "Layover":
            PassengerGate.append([passenger[0], passenger[1], passenger[2]])
    print(PlaneLayover)
    print(PassengerGate)


layover(data1, data2)
