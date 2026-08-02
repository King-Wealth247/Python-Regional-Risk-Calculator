# # Regional Risk Predictor.
from datetime import datetime

class Location:
    def __init__(self, name: str, risk_index: int, status: str):
        self.name = name
        self.risk_index = risk_index
        self.status = status

# Color codes
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"   # Default terminal color

li_input_regions = []
li_unfound_regions = []
li_result = []     # List where we'll store our results

far_north = Location("far north", 67, "moderate")
north = Location("north", 46, "fair")
adamawa = Location("adamawa", 60, "moderate")
west = Location("west", 12, "safe")
north_west = Location("north west", 83, "unsafe")
south_west = Location("south west", 71, "unsafe")
littoral = Location("littoral", 75, "unsafe")
center = Location("center", 77, "unsafe")
south = Location("south", 33, "fair")
east = Location("east", 27, "safe")

def main(): 
    get_regions()
    get_safety_status(li_input_regions)
    log_safety_status()

def get_regions():  # Get the regions from the locations.txt file
    try:
        input_regions = open("locations.txt", "r")
        for line in input_regions:
            line = line.lower().replace(" ", "_").strip()
            if line == "far_north" or line == "north" or line == "adamawa" or line == "west" or line == "north_west" or line == "south_west" or line == "littoral" or line == "center" or line == "south" or line == "east":
                li_input_regions.append(line)
            else:
                li_unfound_regions.append(line)
        input_regions.close()

    except FileNotFoundError:
        print(f"{RED} ERROR: The file locations.txt was not found!{RESET}")
    

def get_safety_status(li_location: list[str]) -> list[str]:      # Calculate the risk and safety of the regions in the locations.txt file
    for location in li_location:  
        if location == "far_north":
            risk_index = far_north.risk_index
            status = far_north.status
        elif location == "north":
            risk_index = north.risk_index
            status = north.status   
        elif location == "adamawa":
            risk_index = adamawa.risk_index
            status = adamawa.status
        elif location == "west":
            risk_index = west.risk_index
            status = west.status
        elif location == "north_west":
            risk_index = north_west.risk_index
            status = north_west.status
        elif location == "south_west":
            risk_index = south_west.risk_index
            status = south_west.status
        elif location == "littoral":
            risk_index = littoral.risk_index
            status = littoral.status
        elif location == "center":
            risk_index = center.risk_index
            status = center.status
        elif location == "south":
            risk_index = south.risk_index
            status = south.status
        elif location == "east":
            risk_index = east.risk_index
            status = east.status

        if risk_index >= 70:
            COLOR = RED
        elif risk_index >= 50:
            COLOR = YELLOW
        elif risk_index >= 30:
            COLOR = BLUE
        else:
            COLOR = GREEN

        li_result.append([location, risk_index, status, COLOR])


    # Calculated Output. 
    for i in range(len(li_result)):
        print(f"\nLocation: {li_result[i][0].replace("_", " ").title()} \nRisk Index: {li_result[i][1]} \nSafety Status: {li_result[i][3]}{li_result[i][2]}{RESET}\n")

    return(li_result)

def log_safety_status():     # Log the risk and safety of the regions in the locations.txt file to a log file
    try:
        with open("safety_log.txt", "a") as log_file:
            for i in range(len(li_input_regions)):
                log_file.write(f"Region: {li_input_regions[i].replace('_', ' ').title()} | Risk Index: {li_result[i][1]} | Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    except FileNotFoundError:
        with open("safety_log.txt", "w+") as log_file:
            log_file.write(f"{"safety log".center(50, "-").title()}\n")

if __name__ == "__main__":
    main()

