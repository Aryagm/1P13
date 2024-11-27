import tkinter as tk
from passenger_and_fleet_data import passenger_data, fleet_data
from daily_data import daily_data
from overweight import overweight
from oversold import oversold
from layover import layover


def graphical_46(oversold_data, overweight_data, layover_data):
    """
    Creates a graphical interface summarizing:
    1. Oversold Business and Economy seats
    2. Passengers with Overweight Bags
    3. Passengers Arriving Late and Having to Layover
    """
    # Unpack the provided data into separate components
    oversold_business, oversold_economy = oversold_data
    
    # we dont caer about passenger output so only get index 1 which is the fleet output
    fleet_overweight = overweight_data[1]
    
    # we dont care about passenger output so only get index 0 which is the plane output
    plane_layover = layover_data[0]

    
    # Convert data into dictionaries for quick lookups
    # Each dictionary will have plane model as key and the corresponding value
    oversold_business_dict = {item[0]: item[1] for item in oversold_business}
    oversold_economy_dict = {item[0]: item[1] for item in oversold_economy}
    overweight_dict = {item[0]: item[1] for item in fleet_overweight}
    layover_dict = {item[0]: item[1] for item in plane_layover}

    # Collect all unique plane models across the data
    # Set gets all unique values, then convert back to a list
    # We get all unique plane models by combining all keys from the dictionaries
    plane_models = list(layover_dict.keys())

    # Initialize the main window for the GUI
    root = tk.Tk()
    root.title("Flight Summary")  # Set the window title
    root.geometry("800x600")  # Define window size
    root.configure(bg="#f0f8ff")  # Set background color

    # Add a title label to the window
    tk.Label(root, text="Flight Summary Dashboard", font=("Helvetica", 16, "bold"), bg="#f0f8ff").pack(pady=10)

    # Create a frame to hold individual plane summaries
    frame = tk.Frame(root, bg="#f0f8ff")
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Variables to manage the layout of plane summaries in a grid
    column_count = 3  # Number of columns
    row, col = 0, 0  # Track the current row and column

    # Create a GUI frame for each plane model
    for plane in plane_models:
        # Retrieve data for the current plane, defaulting to 0 if not available
        oversold_b = oversold_business_dict.get(plane, 0)
        oversold_e = oversold_economy_dict.get(plane, 0)
        overweight = overweight_dict.get(plane, 0)
        layover = layover_dict.get(plane, 0)

        # Frame for displaying details about the current plane
        plane_frame = tk.Frame(frame, bg="#e0ffff", bd=2, relief="groove", padx=10, pady=5)
        plane_frame.grid(row=row, column=col, padx=10, pady=10, sticky="n")

        # Add details for the plane inside the frame
        # We need .pack because we are adding widgets to a frame
        # If we did not pack 
        tk.Label(plane_frame, text=plane, font=("Helvetica", 14, "bold"), bg="#e0ffff").pack(anchor="w")
        tk.Label(plane_frame, text=f"Oversold Business Seats: {oversold_b}", bg="#e0ffff").pack(anchor="w", pady=2)
        tk.Label(plane_frame, text=f"Oversold Economy Seats: {oversold_e}", bg="#e0ffff").pack(anchor="w", pady=2)
        tk.Label(plane_frame, text=f"Overweight Bags: {overweight}", bg="#e0ffff").pack(anchor="w", pady=2)
        tk.Label(plane_frame, text=f"Passengers in Layover: {layover}", bg="#e0ffff").pack(anchor="w", pady=2)

        # Update the layout for the next plane
        col += 1
        if col == column_count:  # Move to a new row after the last column
            col = 0
            row += 1

    # Start the main GUI loop
    root.mainloop()


# Load data from external files
pdata = passenger_data("passenger_data_v1.txt")
fdata = fleet_data("fleet_data.txt")

# Process data using the functions and data
oversold_data = oversold(pdata, fdata, daily_data(pdata))
overweight_data = overweight(pdata, fdata)
layover_data = layover(pdata, fdata)
print(oversold_data)

# Launch the graphical interface by passing the processed data
graphical_46(oversold_data, overweight_data, layover_data)
