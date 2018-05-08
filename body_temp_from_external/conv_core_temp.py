#!/usr/bin/env python

# Author: Makenzie Brian
# Date: April 23, 2018
# Class: ME 599
# File: conv_core_temp.py
# Description: converts csv to estimated core temperature


def conv_file(file):
    """converts csv to array for use in later functions
    args: filename as .csv"""
    with open(file, 'r') as f1:
        file_contents = []
        for line in f1:
            file_contents.append(line.strip().split(","))  # strip \n and split into values to put in array

        return file_contents


def conv_core_temperature(temp_array):
    """converts array of temperature values to an average value
    args: array of temperatures as floats or ints"""
    average_temp = float(sum(temp_array)) / float(max(temp_array))
    est_core_temp = average_temp * 1.052    # bad est b/c need external tmp etc.
    # core_temp = skin_temp + (heat_flux * (d/lambda) but can't get d and lamba sooooo
    # upon further inspection may need to have it learn this based on known datasets....
    if est_core_temp < 0:
        return "INVALID VALUE"
    else:
        return est_core_temp

 
