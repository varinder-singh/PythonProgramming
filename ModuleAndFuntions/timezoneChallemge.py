# aware time and naive time

import datetime
import pytz

local_datetime = datetime.datetime.now()
utc_datetime = datetime.datetime.utcnow()

print("Local time from datetime is {} and timezone is {}".format(local_datetime, local_datetime.tzname()))
print("UTC time from datetime is {} and timezone is {}".format(utc_datetime, utc_datetime.tzname()))

local_pytz = pytz.utc.localize(local_datetime)

utc_pytz = pytz.utc.localize(utc_datetime)

print("Aware local datetime is {} and time zone is".format(local_pytz))

print("Awrae utc datetime is {} and time zone is".format(utc_pytz))