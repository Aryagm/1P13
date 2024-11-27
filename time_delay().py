def time_delay(passengerList, fleetList):
    planelatelayover=[]
    
    for plane in fleetList:
        plane_model = plane[0]
        gate = plane[4]
        late_layover_count = 0
        
        for passenger in passengerList:
            if passenger[2] == gate and passenger [7] == "Layover" and passenger[8] == "Late":
                late_layover_count += 1
                
     
        planelatelayover.append([plane_model, late_layover_count])
        
    return planelatelayover
