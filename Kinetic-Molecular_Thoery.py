import math

while True:
    GAS_CONSTANT = 8.314 #Ideal gas constant (J/K*mol)
    TEMPERATURE = float(input("Provide the Temperature (Kelvin): ")) 
    MOLAR_MASS = float(input("Provide the molar mass (g/mol): "))/1000 #Input: g/mol => Converted: kg/mol

    rms_speed = math.sqrt((3*GAS_CONSTANT*TEMPERATURE)/MOLAR_MASS) #u_rms
    u_squared = pow(rms_speed, 2) #u_rms^2

    print(f"\n[Result] The root mean square speed is: {round(rms_speed, 3)} m/s")
    print(f"[Result] The average kinetic energy for the gas molecule is: {round((MOLAR_MASS*u_squared)/2, 3)} J") #Calculation & Output for the Average Kinetic Energy of a gas.

    PROCEED = input("Stop Calculating? (y/n): ")
    if PROCEED.upper() == "Y":
        break