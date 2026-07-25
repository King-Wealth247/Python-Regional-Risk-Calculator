#!/usr/bin/env python
# coding: utf-8

# # Regional Risk Predictor.
# 
# A Python based program designed to calculate the risk and safety of a regions upon user input.
# Presently, the calculations are done based on regional crime indexes hardcore coded into the system.

from datetime import datetime

__name___ = "main"

# Color codes
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"   # Default terminal color

li_input_regions = []
li_unfound_regions = []

regions = dict(        # Making use of a dictonary (Key=>value pairs). Could also use {}. data = {"Key" : "Value", "Key" : "Value"}
        far_north=67, 
        north=46, 
        adamawa=60, 
        west=12, 
        north_west=83, 
        south_west=71, 
        littoral=75, 
        center=77, 
        south=33, 
        east=27
    )

def main(): 
    get_regions()  # Get the regions from the locations.txt file
    get_safety_status(li_input_regions, regions)  # Calculate the risk and safety of the regions in the locations.txt file
    log_safety_status()  # Log the risk and safety of the regions in the locations.txt file to a log file

def get_regions():
    try:
        input_regions = open("locations.txt", "r")
        for line in input_regions:
            line = line.lower().replace(" ", "_").strip()
            if line in regions:
                li_input_regions.append(line)
            else:
                li_unfound_regions.append(line)
        input_regions.close()

    except FileNotFoundError:
        print(f"{RED} ERROR: The file locations.txt was not found!{RESET}")
    

def get_safety_status(li_location: list[str], regions: dict[str, int]) -> list[str]:    
    # Risk Calculation Logic
    #tp_result = ()    # Tuple where we'll store our results 
    li_result = []     # List where we'll store our results

    for location in li_location:  
        if regions[location] >= 70:
            risk = "unsafe"
            COLOR = RED
        elif regions[location] >= 50:
            risk = "moderate"
            COLOR = YELLOW
        elif regions[location] >= 30:
            risk = "fair"
            COLOR = BLUE
        else:
            risk = "safe"
            COLOR = GREEN

        #tp_result += ({"location" : location, "risk" : risk, "color" : COLOR}, ) # Concatenate dictionary containig results as a tuple to the result tuple
        li_result.append([location, risk, COLOR])


    # Calculated Output. 
    for i in range(len(li_result)):
        print(f"\nLocation: {li_result[i][0].replace("_", " ").title()} \nSafety Status: {li_result[i][2]}{li_result[i][1]}{RESET}\n")
    # print(f"\nYour Destination: {location.replace("_", " ").title()} \nRisk Level: {COLOR}{risk.title()}{RESET}")

    return(li_result)

def log_safety_status():
    try:
        with open("safety_log.txt", "a") as log_file:
            for i in range(len(li_input_regions)):
                log_file.write(f"Region: {li_input_regions[i].replace('_', ' ').title()} | Risk Index: {regions[li_input_regions[i]]} | Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    except FileNotFoundError:
        with open("safety_log.txt", "w+") as log_file:
            log_file.write(f"{"safety log".center(50, "-").title()}\n")

if __name__ == "__main__":
    main()

