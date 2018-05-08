#!/usr/bin/env python

# Author: Makenzie Brian
# Date: May 7, 2018
# Class: ME 599
# File: integrate_factor.py
# Description: integrates external factors (ambient temp, maybe sweatinig, pulse) into temp calculations

# NOTe TO SELF (and anyone else who is reading this): all degrees in c


# will need to take in external temperature; do not currently have hardware setup for this but should just be a thermistor
# not fully fleshed out because need to do ahrdware setup to test effects

#def read_in_ambient_temp():
#   """reads in ambient environment temperature to be accounted for in calculation of core temp
#    hardware: probably a thermistor? Deson't need to be highly precise"""


#def combine_data(ambient_temp, est_core_temp):
#    """combines ambient_temp and est_core_temp to get a more accurate core_temperature
#    add: citations from papers about how skin temp is affected by ambient temp"""
#    if ambient_temp > est_core_temp:
#        #ie. its hot out
#    else if ambient_temp < est_core_temp:
#        #ie. its not super hot out
#    else if ambient_temp < 5.0:
#        #ie. its pretty cold out (this system is probably meant to be used indoors though)


def check_if_fever(est_core_temp):
    """checks if temperature is above fever threshold or not
    args: estimated core temperature"""
    # maybe need statistical data to test this on so for now just returns if above or below a certain temp
    
    temp_threshold = 37.0
    if est_core_temp > temp_threshold:
        return True
    else:
        return False



