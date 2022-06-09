# AUTHOR JACOB WARREN STACK
import phonenumbers
from phonenumbers import timezone,geocoder,carrier

# user instructions and input
print("\nPHONE-TRACKER")
print('----------------------------------------------')
print("Enter a 10-digit number and country code.")
print("Example, '+10101010101'")
numInput = input("Enter number: ")
print("----------------------------------------------\n")

# parse input into a phone number
phoneNumber = phonenumbers.parse(numInput)

# gather information (timezone, service provider, location)
timezone = timezone.time_zones_for_number(phoneNumber)
carrier = carrier.name_for_number(phoneNumber, 'en')  # in english
location = geocoder.description_for_number(phoneNumber, 'en')

# display info (number, timezone, carrier, location of registration)
print("DETAILS")
print("----------------------------------------------")
print(phoneNumber)
print("Timezone: ", timezone)
print("Carrier: ", carrier)
print("Location: ", location)
print("----------------------------------------------\n")

# output
# DETAILS---------------------------------------
# Country Code: 1 National Number: 2129914000
# Timezone:  ('America/New_York',)
# Service provider:
# Country:  New York, NY
# ----------------------------------------------

print(f"Save to '{phoneNumber.national_number}.txt' ?")
save = input("'Y' or 'N': ")

if save == 'Y':
    # if selected Y, save the details to a file named after the number
    f = open(f"{phoneNumber.national_number}.txt", "w")  # w creates new file if doesnt exist
    f.write(f"{phoneNumber}")
    f.write(f"\nTZ: {timezone}")
    f.write(f"\nC: {carrier}")
    f.write(f"\nL: {location}")

    # open and read the file
    f = open(f"{phoneNumber.national_number}.txt", "r")  # r opens the file for reading
    print(f.read())

