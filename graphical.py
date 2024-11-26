import tkinter as tk
from passenger_and_fleet_data import passenger_data, fleet_data
from daily_data import daily_data
from overweight import overweight
from oversold import oversold
from layover import layover


def graphical_teamID(oversold_data, overweight_data, layover_data):
    """
    Creates a graphical interface summarizing:
    1. Oversold Business and Economy seats
    2. Passengers with Overweight Bags
    3. Passengers Arriving Late and Having to Layover
    """
    # Unpack the provided data into separate components
    oversold_business, oversold_economy = oversold_data
    fleet_overweight = overweight_data[1]
    plane_layover = layover_data[0]

    # Convert data into dictionaries for quick lookups
    oversold_business_dict = {item[0]: item[1] for item in oversold_business}
    oversold_economy_dict = {item[0]: item[1] for item in oversold_economy}
    overweight_dict = {item[0]: item[1] for item in fleet_overweight}
    layover_dict = {item[0]: item[1] for item in plane_layover}

    # Collect all unique plane models across the data
    # Set gets all unique values, then convert back to a list
    # We get all unique plane models by combining all keys from the dictionaries
    plane_models = list(set(oversold_business_dict.keys()) |
                        set(oversold_economy_dict.keys()) |
                        set(overweight_dict.keys()) |
                        set(layover_dict.keys()))

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

### USAGE ##

# Load data from external files
pdata = passenger_data("passenger_data_v2.txt")
fdata = fleet_data("fleet_data.txt")

# Process data to extract oversold, overweight, and layover information
oversold_business, oversold_economy = oversold(pdata, fdata, daily_data(pdata))
passenger_overweight, fleet_overweight = overweight(pdata, fdata)
plane_layover, passenger_gate = layover(pdata, fdata)

# Organize data into tuples for use in the GUI function
oversold_data = (oversold_business, oversold_economy)
overweight_data = (passenger_overweight, fleet_overweight)
layover_data = (plane_layover, passenger_gate)

# Launch the graphical interface
graphical_teamID(oversold_data, overweight_data, layover_data)
