# Write a program to display information about 1) time 2) perf_counter 3) monotonic 4) process_time

import time

print("time() :\t\t ", time.get_clock_info('time'))
print("perf_counter() : ", time.get_clock_info('perf_counter'))
print("monotonic() :\t ", time.get_clock_info('monotonic'))
print("process_time() : ", time.get_clock_info('process_time'))