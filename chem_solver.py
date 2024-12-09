from asyncio.windows_events import NULL
import math
import os

while True:
    GIVEN_VALUES = []

    print("")
    GIVEN_INPUT = str(input("Values given are: "))
    GIVEN_VALUES = GIVEN_INPUT.lower().split(", ")

    for i in range (len(GIVEN_VALUES)-1):
        temp = GIVEN_VALUES[i]
        sm = i + 1
        for j in range (i, len(GIVEN_VALUES)):
            if (GIVEN_VALUES[sm] > GIVEN_VALUES[j]):
                sm = j

        GIVEN_VALUES[i] = GIVEN_VALUES[j]
        GIVEN_VALUES[sm] = temp
        # print(GIVEN_VALUES)

    if "volume" in GIVEN_VALUES and "moles in ":
        del(GIVEN_INPUT)
        del(GIVEN_VALUES)
        
    PROCEED = input("Stop Calculating? (y/n): ")
    if PROCEED.upper() == "Y":
        break