def layover(passengerList, fleetList):
    planeLayover = []
    passengerGate = []
    for plane in fleetList:
        plane_model = plane[0]
        gate = plane[4]
        layover_count = 0  
        
        for passenger in passengerList:
            if passenger[2] == gate and passenger[7] == "Layover":
                layover_count += 1  
                
        planeLayover.append([plane_model, layover_count])  
    
    for passenger in passengerList:
        if passenger[7] == "Layover":
            passengerGate.append([passenger[0], passenger[1], passenger[2]])
    print(planeLayover)
    print(passengerGate)


layover(data1, data2)
