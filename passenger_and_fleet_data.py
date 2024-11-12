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

pdata = passenger_data("passenger_data_v1.txt")
fdata = fleet_data("fleet_data.txt")
