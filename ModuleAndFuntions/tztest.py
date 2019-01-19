import pytz
import datetime

country = "IN"

time_to_display = pytz.country_timezones[country]
local_time = datetime.datetime.now()


print("The time in {} is {}".format(pytz.country_names[country], local_time))
print("The UTC Time is {}".format(datetime.datetime.utcnow()))

# print(dir(pytz))


# for x in sorted(pytz.country_names):
#     print("{} - {}".format(x, pytz.country_names[x]))
    # if pytz.country_timezones.get(x):
    #     print("{}".format(pytz.country_timezones[x]))