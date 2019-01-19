# how time, datetime and calendar can be used

import time
# time method certainly gives the elapsed time, however, we will test perf_counter, monotonic
# and process_time(CPU clock used)
# from time import time as timer     # result            1.556854486465454
# from time import perf_counter as timer     # result    2.492020669997146
# from time import monotonic as timer    # result        1.0669808430029661
from time import process_time as timer  # result        0.00015149400000000202

import random

# prints GMT since the begining - in computer world Jan 01 1970 00:00 hours is considered to be start time
# print(time.gmtime(0))
#
# print(time.localtime())
#
# # Number of seconds since the time of epoch - 1970
# print(time.time())

# Return the time as a named tuple "time.struct_time"

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = timer()
input("press enter to end")
end_time = timer()

print("started at "+time.strftime("%a, %d %b %Y %H:%M", time.localtime(start_time)))
print("Ended at "+time.strftime("%a, %d %b %Y %H:%M", time.localtime(end_time)))

print("Difference between the time {}".format(end_time - start_time))