"""
Create an empty class called Car, then create two instances.
Add the following attributes for each of the instances: Make, Model, Year.
Create print statements to display the attributes of each one of the instances.
"""
class Car:
    pass

Sedan = Car()
Sedan.Make = "Chevy"
Sedan.Model = "Prizm"
Sedan.Year = 2001

SportsCar = Car()
SportsCar.Make = "Aston Martin"
SportsCar.Model = "DB9"
SportsCar.Year = 2003

print(f"Sedan Make: {Sedan.Make}, Model: {Sedan.Model}, Year: {Sedan.Year}")
print(f"SportsCar Make: {SportsCar.Make}, Model: {SportsCar.Model}, Year: {SportsCar.Year}")
