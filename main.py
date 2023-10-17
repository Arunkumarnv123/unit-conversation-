
import tkinter as tk
from tkinter import ttk


def update_conversion_methods(*args):
    selected_type = type_var.get()

    if selected_type == "Length":
        conversion_combobox['values'] = (
        "Centimeter to Meter", "Meter to Centimeter", "Centimeter to INCH", "INCH to Centimeter",
        "Centimeter to KiloMetre", "KiloMetre to Centimeter", "Centimeter to FOOT", "FOOT to Centimeter",
        "Kilometre to Mile", "Mile to Kilometre", "Centimeter to Feets", "Feet to inches")
    elif selected_type == "Area":
        conversion_combobox['values'] = ("Sqft to Sqmtrs", "Sqft to Hectre / Acres")
    elif    selected_type == "Mass":
        conversion_combobox['values'] = (
        "Gram to Kilogram", "Kilogram to Gram", "Kilogram to Tonne", "Kilogram to Tonne", "Tonne to Kilogram",
        "Milligram to Kilogram", "Kilogram to Milligram", "Milligram to Gram", "Gram to Milligram",
        "kilogram to pound (lb)", "pound (lb) to Kilogram", "Micrograms to gram", "Micrograms to Kilogram")
    elif selected_type == "Temperature":
        conversion_combobox['values'] = (
        "Celsius to Fahrenheit", "Celsius to Kelvin", "Fahrenheit to Celsius", "Fahrenheit to Kelvin",
        "Kelvin to Celsius", "Kelvin to Fahrenheit")


    elif selected_type == "Pressure":
        conversion_combobox['values'] = (
        "Bar to Pascal", "Bar to Standard atmosphere", "Pascal to Bar", "Pascal to Standard atmosphere",
        "Standard atmosphere to Pascal", "Standard atmosphere to Bar")
    elif selected_type == "Area":
        conversion_combobox['values'] = ("Sqft to Sqmtrs", "Sqft to Hectre / Acres")
    else:
        conversion_combobox['values'] = ()


# Function to perform the conversion
def convert():
    # Get the selected type of conversion
    selected_type = type_var.get()

    # Get the user input and convert to float
    input_value = entry.get()

    # Get the selected conversion method
    selected_conversion = conversion_var.get()

    # Default result message
    result = "Select a conversion and enter a value."

    if selected_type and selected_conversion and input_value:
        input_value = float(input_value)
        if selected_type == "Length":
            if selected_conversion == "Centimeter to Meter":
                result = input_value / 100
            elif selected_conversion == "Meter to Centimeter":
                result = input_value * 100
            elif selected_conversion == "Centimeter to INCH":
                result = input_value / 2.54
            elif selected_conversion == "INCH to Centimeter":
                result = input_value * 2.54
            elif selected_conversion == "Centimeter to KiloMetre":
                result = input_value / 100000
            elif selected_conversion == "KiloMetre to Centimeter":
                result = input_value * 100000
            elif selected_conversion == "Centimeter to FOOT":
                result = input_value / 30.48
            elif selected_conversion == "FOOT to Centimeter":
                result = input_value * 30.48
            elif selected_conversion == "Kilometre to Mile":
                result = input_value / 1.609
            elif selected_conversion == "Mile to Kilometre":
                result = input_value * 1.609
            elif selected_conversion == "Centimeter to Feets":
                result = input_value * 0.0328084
            elif selected_conversion == "Feet to inches":
                result = input_value * 12



        elif selected_type == "Mass":
            if selected_conversion == "Gram to Kilogram":
                result = input_value / 1000
            elif selected_conversion == "Kilogram to Gram":
                result = input_value * 1000
            elif selected_conversion == "Kilogram to Tonne":
                result = input_value / 1000
            elif selected_conversion == "Tonne to Kilogram":
                result = input_value * 1000
            elif selected_conversion == "Milligram to Kilogram":
                result = input_value / 1000000
            elif selected_conversion == "Kilogram to Milligram":
                result = input_value * 1000000
            elif selected_conversion == "Milligram to Gram":
                result = input_value / 1000
            elif selected_conversion == "Gram to Milligram":
                result = input_value * 1000
            elif selected_conversion == "kilogram to pound (lb)":
                result = input_value * 2.20462
            elif selected_conversion == "pound (lb) to Kilogram":
                result = input_value / 2.20462
            elif selected_conversion == "Micrograms to gram":
                result = input_value / 1e+6
            elif selected_conversion == "Micrograms to Kilogram":
                result = input_value / 1e+9



        elif selected_type == "Temperature":
            if selected_conversion == "Celsius to Fahrenheit":
                result = (input_value * 9.5) + 32
            elif selected_conversion == "Celsius to Kelvin":
                result = input_value + 273.15
            elif selected_conversion == "Fahrenheit to Celsius":
                result = (input_value - 32) * 5.9
            elif selected_conversion == "Fahrenheit to Kelvin":
                result = (input_value - 32) * 5.9 + 273.15
            elif selected_conversion == "Kelvin to Celsius":
                result = input_value - 273.15
            elif selected_conversion == "Kelvin to Fahrenheit":
                result = (input_value - 273.15) * 9.5 + 32

        elif selected_type == "Pressure":
            if selected_conversion == "Bar to Pascal":
                result = input_value * 100000
            elif selected_conversion == "Bar to Standard atmosphere":
                result = input_value / 1.013
            elif selected_conversion == "Pascal to Bar":
                result = input_value / 100000
            elif selected_conversion == "Pascal to Standard atmosphere":
                result = input_value / 101300
            elif selected_conversion == "Standard atmosphere to Pascal":
                result = input_value * 101300
            elif selected_conversion == "Standard atmosphere to Bar":
                result = input_value * 1.013



        elif selected_type == "Area":
            if selected_conversion == "Sqft to Sqmtrs":
                result = input_value * 0.09290304
            elif selected_conversion == "Sqft to Hectre / Acres":
                result = input_value * 0.0000092903

    # Update the result label
    result_label.config(text=f"RESULT: {result}")

# Create the main window

root = tk.Tk()
root.title("Calcy")
# Create a label for the title
title_label = tk.Label(root, text="UNIT CONVERTER", font=("Arial", 26))
title_label.pack(pady=20)

# Create a label for type selection
type_label = tk.Label(root, text="Choose the type of conversion:")
type_label.pack()

# Create a combobox for selecting the type
type_var = tk.StringVar()
type_combobox = ttk.Combobox(root, textvariable=type_var,
                             values=("Length", "Area", "Mass", "Temperature",  "Pressure"))
type_combobox.pack()

# Link the update_conversion_methods function to the type_var
type_var.trace("w", update_conversion_methods)

# Create a label for value input

# Create a label for conversion method selection
conversion_label = tk.Label(root, text="Choose the conversion method:")
conversion_label.pack()

# Create a combobox for selecting the conversion method
conversion_var = tk.StringVar()
conversion_combobox = ttk.Combobox(root, textvariable=conversion_var, values=())  # Start with an empty list
conversion_combobox.pack()

value_label = tk.Label(root, text="Enter a value to convert:")
value_label.pack()

# Create an entry for user input
entry = tk.Entry(root)
entry.pack()


# Create a button to perform the conversion
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=10)

# Create a label for displaying the result
result_label = tk.Label(root, text="Result: Select a conversion and enter a value.")
result_label.pack()

# Start the GUI main loop
root.mainloop()
print("----------********--------")
print("     without tkinter ")
"""def area():
    print("--- You chose type Area ---- ")
    print("")
    Temp_dict = \
        {

            1: "Sqft to Acres",
            2: "Sqft to Sqmtrs"

        }

    # ==== for getting number of conversion ====
    print(" ----  ----  ----  ---- ")
    for keys, values in Temp_dict.items():
        print("{:2}. {}".format(keys, values))
    Area_op = int(input("\nWhich conversion you want to do from 1 to 2:"))

    Area = float(input("- Enter a number to convert: "))

    # ==== converting ====
    if Area_op == 1:
        print("{} Sqrt is equal to {} Acres".format(Area, (Area / 43560)))

    elif Area_op == 2:
        print("{} Sqrt is equal to {} Sqmtrs".format(Area, (Area / 10.764)))

    else:
        print("Sorry, Please type correct number from 1 to 6.")

def pressure():
    print(" ----  You chose type Pressure ----\n ")

    Pressure_dict = \
        {
            1: "Bar to Pascal",
            2: "Bar to Standard atmosphere",
            3: "Pascal to Bar",
            4: "Pascal to Standard atmosphere",
            5: "Standard atmosphere to Pascal",
            6: "Standard atmosphere to Bar"
        }
    # ==== for getting number of conversion ====
    print(" ----  ----  ----  ---- ")
    for keys, values in Pressure_dict.items():
        print("{:2}. {}".format(keys, values))
    Pressure_convert = int(input("\nWhich conversion you want to do from 1 to 6: "))
    Pressure_value = float(input("- Enter a number to convert: "))


    # ==== converting ====
    if Pressure_convert == 1:
        print("{} Bar is equal to {} P".format(Pressure_value, Pressure_value * 100000))
    elif Pressure_convert == 2:
        print("{} Bar is equal to {} atm".format(Pressure_value, Pressure_value / 1.013))
    elif Pressure_convert == 3:
        print("{} P is equal to {} Bar".format(Pressure_value, Pressure_value / 100000))
    elif Pressure_convert == 4:
        print("{} P is equal to {} atm".format(Pressure_value, Pressure_value / 101300))
    elif Pressure_convert == 5:
        print("{} atm is equal to {} P".format(Pressure_value, Pressure_value * 101300))
    elif Pressure_convert == 6:
        print("{} atm is equal to {} Bar".format(Pressure_value, Pressure_value * 1.013))
    else:
        print("Sorry, Please type correct number from 1 to 6.")

def lenth():
    print(" ----  You chose type Length ---- ")
    print("")
    length_dict = \
        {
            1: "Centimeter to FOOT",
            2: "Feet to Inches",
            3: "Centimeter to INCH",
            4: "INCH to Centimeter",
            5: "Centimeter to KiloMetre",
            6: "KiloMetre to Centimeter",
            7: "Centimeter to Meter",
            8: "FOOT to Centimeter",
            9: "Kilometre to Mile",
            10: "Mile to Kilometre",
            11: "Centimeter to Feets",
            12: "Meter to Centimeter"

        }

    # ==== for getting number of conversion ====
    print(" ----  ----  ----  ----  ---- ")
    for keys, values in length_dict.items():
        print("{:2}. {}".format(keys, values))
    length_convert = int(input("\nWhich conversion you want to do from 1 to 12: "))
    length_value = float(input("- Enter a number to convert: "))


    # ==== converting ====
    if length_convert == 1:
        print("{} cm is equal to {} feet.".format(length_value, length_value / 30.48))
    elif length_convert == 2:
        print("{} Feet is equal to {} inches".format(length_value, length_value * 12))

    elif length_convert == 3:
        print("{} cm is equal to {} inch.".format(length_value, length_value / 2.54))
    elif length_convert == 4:
        print("{} inch is equal to {} cm.".format(length_value, length_value * 2.54))
    elif length_convert == 5:
        print("{} cm is equal to {} km.".format(length_value, length_value / 100000))
    elif length_convert == 6:
        print("{} km is equal to {} cm.".format(length_value, length_value * 100000))
    elif length_convert == 7:
        print("{} cm is equal to {} m.".format(length_value, length_value / 100))

    elif length_convert == 8:
        print("{} feet is equal to {} cm.".format(length_value, length_value * 30.48))
    elif length_convert == 9:
        print("{} KM is equal to {} mile".format(length_value, length_value / 1.609))
    elif length_convert == 10:
        print("{} mile is equal to {} KM".format(length_value, length_value * 1.609))
    elif length_convert == 11:
        print("{} Centimeter is equal to {} Feet".format(length_value, length_value / 30.48))
    elif length_convert == 12:
        print("{} m is equal to {} cm.".format(length_value, length_value * 100))

    else:
        print("Sorry, Please type correct number from 1 to 10.")

def mass():
    print(" ----  You chose type Mass ---- ")
    print("")
    mass_dict = \
        {
            1: "Gram to Kilogram",
            2: "Kilogram to Gram",
            3: "Kilogram to Tonne",
            4: "Tonne to Kilogram",
            5: "Milligram to Kilogram",
            6: "Kilogram to Milligram",
            7: "Milligram to Gram",
            8: "Gram to Milligram",
            9: "kilogram to pound (lb)",
            10: "pound (lb) to Kilogram",
            11: "Micrograms to gram",
            12: "Micrograms to Kilogram"
        }

    # ==== for getting number of conversion ====
    print(" ----  ----  ----  ---- ")
    for keys, values in mass_dict.items():
        print("{:2}. {}".format(keys, values))
    mass_convert = int(input("\nWhich conversion you want to do from 1 to 10: "))
    mass_value = float(input("- Enter a number to convert: "))

    # ==== converting ====
    if mass_convert == 1:
        print("{} g is equal to {} Kg".format(mass_value, mass_value / 1000))
    elif mass_convert == 2:
        print("{} Kg is equal to {} g".format(mass_value, mass_value * 1000))
    elif mass_convert == 3:
        print("{} kg is equal to {} T".format(mass_value, mass_value / 1000))
    elif mass_convert == 4:
        print("{} T is equal to {} kg".format(mass_value, mass_value * 1000))
    elif mass_convert == 5:
        print("{} mg is equal to {} kg".format(mass_value, mass_value / 1000000))
    elif mass_convert == 6:
        print("{} Kg is equal to {} mg".format(mass_value, mass_value * 1000000))
    elif mass_convert == 7:
        print("{} mg is equal to {} g".format(mass_value, mass_value / 1000))
    elif mass_convert == 8:
        print("{} g is equal to {} mg".format(mass_value, mass_value * 1000))
    elif mass_convert == 9:
        print("{} Kg is equal to {} lb".format(mass_value, mass_value * 2.20462))
    elif mass_convert == 10:
        print("{} lb is equal to {} kg".format(mass_value, mass_value / 2.20462))
    elif mass_convert == 11:
        print("{} μg is equal to {} g".format(mass_value, mass_value / 1e+6))
    elif mass_convert == 12:
        print("{} μg is equal to {} Kg".format(mass_value, mass_value / 1e+9))
    else:
        print("Sorry, Please type correct number from 1 to 12.")

def temp():
    print(" ----  You chose type Temperature ---- ")
    print("")
    Temp_dict = \
        {
            1: "Celsius to Fahrenheit",
            2: "Celsius to Kelvin",
            3: "Fahrenheit to Celsius",
            4: "Fahrenheit to Kelvin",
            5: "Kelvin to Celsius",
            6: "Kelvin to Fahrenheit"
        }

    # ==== for getting number of conversion ====
    print(" ----  ----  ----  ----  ---- ")
    for keys, values in Temp_dict.items():
        print("{:2}. {}".format(keys, values))
    Temp_convert = int(input("\nWhich conversion you want to do from 1 to 6: "))
    Temp_value = float(input("- Enter a number to convert: "))

    # ==== converting ====
    if Temp_convert == 1:
        print("{} C is equal to {} F".format(Temp_value, (Temp_value * 9.5) + 32))
    elif Temp_convert == 2:
        print("{} C is equal to {} K".format(Temp_value, Temp_value + 273.15))
    elif Temp_convert == 3:
        print("{} F is equal to {} C".format(Temp_value, (Temp_value - 32) * 5.9))
    elif Temp_convert == 4:
        print("{} C is equal to {} K".format(Temp_value, (Temp_value - 32) * 5.9 + 273.15))
    elif Temp_convert == 5:
        print("{} K is equal to {} C".format(Temp_value, Temp_value - 273.15))
    elif Temp_convert == 6:
        print("{} K is equal to {} F".format(Temp_value, (Temp_value - 273.15) * 9.5 + 32))
    else:
        print("Sorry, Please type correct number from 1 to 6.")


def unit_convert():
    unit_change = \
        {
            1: "Length",
            2: "Area",
            3: "Mass",
            4: "Temperature",
            5: "Pressure"

        }



    # ==== for getting number of type ====
    for keys, values in unit_change.items():
        print("{:2}. {}".format(keys, values))

    ip =(input("\nWhich type of conversion you want to do from 1 to 5: "))
    ip=int(ip)
    if  ip == 1:
        lenth()
    elif  ip == 2:
        area()
    elif ip  == 3:
        mass()
    elif ip  == 4:
        temp()
    elif  ip == 5:
        pressure()
    else:
        print(" Please Enter correct number from 1 to 5.")

def contactme():
    print("\n\n--- contact me through email ---")
    print("arunkumarnv9164@gmail.com\n\n")

if __name__ == "__main__":
    contactme()
    i="Y"
    while i == "Y" or i == "y":
        unit_convert()
        i=input("do you want to continue (Y/N)")
    contactme()
"""
