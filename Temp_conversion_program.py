# Program for temperature conversion between celsius,fahrenheit and kelvin


#Asking user to select conversion type
print("Please select Conversion type: \n"
        "1. Celsius to Fahrenheit\n"
        "2. Celsius to Kelvin\n"
        "3. Fahrenheit to Celsius \n"
        "4. Fahrenheit to Kelvin\n"
        "5. Kelvin to Celsius\n"
        "6. Kelvin to Fahrenheit\n")

select_1=int(input("Enter option(1-6) : "))

#Asking user to input temperature
degree=float(input("Enter temperature: "))


# Applying condition for conversion type=1 (celsius to fahrenheit)
if select_1==1:
   fahrenheit = (9/5) * degree + 32
   print(degree,"Celsius = ",fahrenheit,"Fahrenheit")

# Applying condition for conversion type=2 (celsius to kelvin)
elif select_1==2:
  kelvin = degree + 273.25
  print(degree,"Celsius = ",kelvin,"Kelvin")

#Applying condition for conversion type=3 (fahrenheit to celsius)
elif select_1==3:
  celsius = (degree-32) * 5/9
  print(degree,"Fahrenheit = ",celsius,"Celsius")

# Applying condition for conversion type=4 (fahrenheit to kelvin)
elif select_1==4:
  kelvin = (degree-32) * 5/9 + 273.15
  print(degree,"Fahrenheit = ",kelvin,"Kelvin")

# Applying condition for conversion type=5 (kelvin to celsius )
elif select_1==5:
 celsius=degree-273.15
 print(degree,"Kelvin = ",celsius,"Celsius")

# Applying condition for conversion type=6 (kelvin to fahrenheit)
elif select_1==6:
 fahrenheit=(degree-273.15) * 9/5 + 32
 print(degree,"Kelvin = ",fahrenheit,"Fahrenheit")   
   

 
   
        
