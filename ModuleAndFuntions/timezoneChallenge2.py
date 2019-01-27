# allow the user to see upto 9 timezones
# allow the used to input the timezones the user actually want to see

# the program should display the timezone in local as well as UTC timezone
# Display the timezones in a format so that user can understand

import pytz
import datetime

available_timezones = {'1': "Africa/Tunis",
                       '2': "Asia/Kolkata",
                       '3': "Australia/Adelaide",
                       '4': "Europe/Brussels",
                       '5': "Europe/London",
                       '6': "Japan",
                       '7': "Pacific/Tahiti",
                       '8': "US/Hawaii",
                       '9': "Zulu"}

print("Please enter your choice or enter zero to quit: ")
for item in sorted(available_timezones):
    print("Enter {} for {}".format(item, available_timezones[item]))

while True:
    value = input("Please enter now : ")
    if value == '0':
        break
    elif value in available_timezones.keys():
        tzDisplay = pytz.timezone(available_timezones[value])
       # print(tzDisplay)
        worldTime = datetime.datetime.now(tz=tzDisplay)
        print("Time zone selected is {} and time here is {}".format(available_timezones[value], worldTime))
    else:
        print("Please choose a valid option from the dictionary")
