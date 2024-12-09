# Created: OCTOBER 2022 | Updated: AUGUST 2024 

# **Update**: I added comments to explain what's going on. It's been a few years so I'm not if it's all correct, program still works though! Good job college freshman me!
# All functions will generally be the same structure, just slightly different calcuation to achieve the intended value. 
# I riddled one function with comments and then the other functions just get little titles and equations to identify which function is which. 
# Did this for any who stumble upon this whom are unfamiliar with programming and/or want to easily figure out what's going on I guess.
# Only change I did was adding a constant for decimals rounded, incase it wants to be editted for more precision.

# Ideal Gas Law: PV=nRT

RATE = 0.0821 # Gas Law Constant in L atm mol^-1 K^-1
DECIMAL_PLACES = 2 # How many decimal places the calculated value will be.

# SOLVER FOR pressure.
def solvepressure(): 
    # Ideal Gas Law; Solving for pressure
    # P=(nRT)/V
    print("SOLVING FOR pressure") # Just reminding the user what's being solved.
     
    moles = input("Provide the molar mass (mol): ") # Asking for user input for the molar mass, temperature, and volume. 
    temperature = input("Provide the temperature (K): ")
    volume = input("Provide the volume (L): ")
    
    if moles.isnumeric() is False or temperature.isnumeric() is False or volume.isnumeric() is False: # Very simple value checking for the input for just numbers.
        print("ERROR: One or more inputs is not a number. Please only input numbers.\n", end="\n") 
        solvepressure() # Instead of yeeting the program for invalid input, just having the user redo the value input process. I mean, unless it was intentional to get out of the program HAHA.
    else:
        moles = float(moles) # Turning values to floats if they aren't already, and this is being done for all inputted values. We want all values to be the same and be able to output numbers with decimals anyway.
        temperature = float(temperature)
        volume = float(volume)
        print(f"\n[Result] The pressure is: ~{round((moles*RATE*temperature)/volume, DECIMAL_PLACES)} atm", end="\n\n")  # lumped calcuation in with printing result. Only would be better to seperate it for easy of readability I suppose.

# SOLVER FOR volume
def solvevolume(): 
    # Ideal Gas Law; Solving for volume
    # V=(nRT)/P
    print("SOLVING FOR volume")
    moles = input("Provide the mass (mol): ")
    temperature = input("Provide the temperature (K): ")
    pressure = input("Provide the pressure (atm): ")
    
    if moles.isnumeric() is False or pressure.isnumeric() is False or temperature.isnumeric() is False:
        print("ERROR: One or more inputs is not a number. Please only input numbers.\n", end="\n")
        solvevolume()
    else:
        moles = float(moles)
        temperature = float(temperature)
        pressure = float(pressure)
        print(f"\n[Result] The volume is: ~{round((moles*RATE*temperature)/pressure, DECIMAL_PLACES)} L", end="\n\n") 

# SOLVER FOR MASS
def solveMass():
    # Ideal Gas Law; Solving for moles
    # n = (PV)/(RT)
    print("SOLVING FOR MASS")
    pressure = input("Provide the pressure (atm): ")
    volume = input("Provide the volume (L): ")
    temperature = input("Provide the temperature (K): ")

    if temperature.isnumeric() is False or pressure.isnumeric() is False or volume.isnumeric() is False:
        print("ERROR: One or more inputs is not a number. Please only input numbers.\n", end="\n")
        solveMass()
    else:
        pressure = float(pressure)
        volume = float(volume)
        temperature = float(temperature)
        print(f"[Result] The mass is: ~{round((pressure*volume)/(RATE*temperature), DECIMAL_PLACES)} mol", end="\n\n")

# Solver for temperature
def solvetemperature():
    # Ideal Gas Law; Solving for moles
    # T = (PV)/(nR)
    print("SOLVING FOR temperature")
    pressure = input("Provide the pressure (atm): ")
    volume = input("Provide the volume (L): ")
    moles = input("Provide the mass (mol): ")

    if moles.isnumeric() is False or pressure.isnumeric() is False or volume.isnumeric() is False:
        print("ERROR: One or more inputs is not a number. Please only input numbers.\n", end="\n")
        solvetemperature()
    else:
        pressure = float(pressure)
        volume = float(volume)
        moles = float(moles)
        print(f"[Result] The mass is: ~{round((pressure*volume)/(moles*RATE), DECIMAL_PLACES)} K", end="\n\n")

while True: # Just to keep it going. Terrible idea to do it this way but hey, it works I suppose.
    SOLVE_FOR = input("\nWhat value are you needing? (pressure, volume, mass, temperature): ").lower() 
    match SOLVE_FOR: # My brillancy back when i made this program was to use cases, which is more efficient than if-else chains. Although could be used here, too, since there's not many cases.
        case "pressure":
            solvepressure()
        case "volume":
            solvevolume()
        case "mass":
            solveMass()
        case "temperature":
            solvetemperature()

    PROCEED = input("Stop Calculating? (y/n): ") # Just asking whether or not to continue calculating  
    if PROCEED.lower() == "y":
        break