"""
Aarohan Singh
"""

def time_delay(passengerList, fleetList):
    #Initializes the list which stores the final result
    planelatelayover = []

    #Loop through each plane in fleetList - gives the model of the plane, the gate that the plane is in, and a counter for the number of passengers that are late and have a layover
    for plane in fleetList:
        plane_model = plane[0]
        gate = plane[4]
        late_layover_count = 0

        #Loop through each passenger in passengerList. 
        for passenger in passengerList:
            #Checks if the passenger is at the same gate as the plane, and whether they have a layover or late status. It then adds one to the counter if they have a layover or if they are late
            if passenger[2] == gate and passenger [7] == "Layover" and passenger[8] == "Late":
                late_layover_count += 1

        #Appends the plane model and the count of the passengers who are late and have a layover to the planelatelayover list
        planelatelayover.append([plane_model, late_layover_count])

    #returns the final list with plane models and passengers
    return planelatelayover
