#!/usr/bin/env python
# coding: utf-8

# # Regional Risk Predictor.
# 
# A Python based program designed to calculate the risk and safety of a regions upon user input.
# Presently, the calculations are done based on regional crime indexes hardcore coded into the system.




def main():
    regions = dict(        # Making use of a dictonary (Key=>value pairs). Could also use {}. data = {"Key" : "Value", "Key" : "Value"}
        far_north=67, 
        north=46, 
        adamawa=60, 
        west=69, 
        north_west=83, 
        south_west=71, 
        littoral=75, 
        center=77, 
        south=33, 
        east=47
    )
    
    # Color codes
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"   # Default terminal color


    # user input.
    li_location = []
    
    print("Enter 5 regions in Cameroon: \n")
    
    for i in range(1, 6):
    
        while True:
            location = input(f"Enter the region number {BLUE} {i} {RESET} (It must be one of the 10 regions in Cameroon): ")
            location=location.lower().replace(" ","_")      #clean texxt
            if location in regions:
                #print(location)
                li_location.append(location)
                break;
            print(f"\n{RED}It seems the region you entered isn't one of the 10 in Cameroon!{RESET} Please, reENTER\n")
    
    get_safety_status(li_location, regions)


def get_safety_status(li_location: list[str], regions: list[str]) -> list[str]:
    
    # Color codes
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    BLUE = "\033[34m"
    RESET = "\033[0m"   # Default terminal color
    
    # Risk Calculation Logic
    #tp_result = ()    # Tuple where we'll store our results 
    li_result = []     # List where we'll store our results

    for location in li_location:  
        if regions[location] >= 70:
            risk = "high"
            COLOR = RED
        elif regions[location] >= 40:
            risk = "moderate"
            COLOR = YELLOW
        else:
            risk = "low"
            COLOR = GREEN

        #tp_result += ({"location" : location, "risk" : risk, "color" : COLOR}, ) # Concatenate dictionary containig results as a tuple to the result tuple
        li_result.append([location, risk, COLOR])


    # Calculated Output
    for i in range(len(li_result)):
        print(f"\nLocation: {li_result[i][0].replace("_", " ").title()} \nSecurity Risk: {li_result[i][2]}{li_result[i][1]}{RESET}\n")
    # print(f"\nYour Destination: {location.replace("_", " ").title()} \nRisk Level: {COLOR}{risk.title()}{RESET}")

    return(li_result)

if __name__ == "main":
    main()



