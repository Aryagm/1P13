def passenger_data(filename):
    file = open(filename, mode="r")
    passenger_list = []
    lines = file.readlines()
    file.close()
    for line in lines:
        passenger_list.append(line.strip().split(","))
    return passenger_list

def fleet_data(filename):
    file = open(filename, mode="r")
    fleet_list = []
    lines = file.readlines()
    file.close()
    for line in lines:
        fleet_list.append(line.strip().split(","))
    return fleet_list



data1= passenger_data("passenger_data_v1.txt")
data2 = fleet_data("fleet_data.txt")

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
