# This is calculation Night DeTime
import math


def set_variables():
    fill_vol_per_exchange = int(input("Enter the value of Nigh Fill Vol Per cycle"))
    four_hour_vol_inf = int(input("Enter 4 Hour Volume Infused from PET"))
    four_hour_inf_time = int(input("Enter 4 Hour fill Time from PET"))
    four_hour_vol_drained = int(input("Enter 4 hour Vol drained from PET"))
    four_hour_drain_time = int(input("Enter 4 hour drain time from PET"))
    res_dial_vol = int(input("Enter tghe value of Nigh Fill Vol Per cycle"))
    therapy_time = int(input("Enter the total Therapy time"))
    num_of_exchange = int(input("Enter the number of cycles"))
    calc_night_dwell_time(fill_vol_per_exchange, four_hour_vol_inf, four_hour_inf_time, four_hour_vol_drained, four_hour_drain_time, res_dial_vol, therapy_time, num_of_exchange)

def calc_night_dwell_time(fill_vol_per_exchange, four_hour_vol_inf, four_hour_inf_time, four_hour_vol_drained, four_hour_drain_time, res_dial_vol, therapy_time, num_of_exchange):
    in_fill_time = fill_vol_per_exchange / (four_hour_vol_inf / four_hour_inf_time)
    drain_time = -(math.log(res_dial_vol / (fill_vol_per_exchange + res_dial_vol))) / (-(math.log(res_dial_vol / (four_hour_vol_drained + res_dial_vol))) / four_hour_drain_time)
   # Below is the main calculation
    night_dwell_time = (therapy_time - (num_of_exchange * (in_fill_time + drain_time))) / num_of_exchange
    return night_dwell_time



if __name__=="__main__":
    set_variables()