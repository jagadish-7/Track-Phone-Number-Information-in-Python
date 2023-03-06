import phonenumbers
from phonenumbers import geocoder, timezone, carrier

#Taking the phone number as input from the user
number = input("Enter the number with country code\n")
print("----------------------------------")

parsed_number = phonenumbers.parse(number)

country_info = geocoder.description_for_number(parsed_number, "en")
time_info = timezone.time_zones_for_number(parsed_number)
service_info = carrier.name_for_number(parsed_number, "en")

print("Country Name:- ", country_info)
print("Timezone:- ", time_info)
print("ISP:- ", service_info)