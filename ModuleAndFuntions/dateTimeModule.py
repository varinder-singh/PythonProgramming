import time

print("The epoch time on this machine starts at : ", time.strftime("%c", time.gmtime(0)))

print("The current timezone is {0} and offset is {1}".format(time.tzname[0], -(time.timezone/3600)))

if time.daylight != 0:
    print("DayTime Saving is in effect")
    print("The DST TimeZone is {}".format(time.tzname[1]))
else:
    print("{} does not have DST rules".format(time.tzname[0]))

print("Local Time is {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
print("UTC is  {}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())))
