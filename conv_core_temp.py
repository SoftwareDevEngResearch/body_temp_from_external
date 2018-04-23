#!/usr/bin/env python

# Author: Makenzie Brian
# Date: April 23, 2018
# Class: ME 599
# File: conv_core_temp.py
# Description:


def conv_file(file):
    with open(file, 'r') as f1:
        file_contents = []
        for line in f1:
            file_contents.append(line.strip().split(","))  # strip \n and split into values to put in array

        return file_contents


def conv_file_test():
    real_contents = [['24', '25', '23', '23', '24', '25'], ['23', '24', '25', '24', '24', '25'], ['28', '30', '30', '30', '28', '25'], ['26', '29', '28', '28', '29', '25'], ['23', '24', '24', '24', '25', '25']]
    est_contents = conv_file("data.csv")
    #print conv_file("data.csv")

    # literally just need one simple test because what else can I even check here???
    if est_contents == real_contents:
        print "PASS"


def conv_core_temp(temp_array):
    average_temp = float(sum(temp_array) / max(temp_array))
    est_core_temp = average_temp * 1.052    # bad est b/c need external tmp etc.
    # core_temp = skin_temp + (heat_flux * (d/lambda) but can't get d and lamba sooooo
    # upon further inspection may need to have it learn this based on known datasets....
    if est_core_temp < 0:
        return "INVALID VALUE"
    else:
        return est_core_temp


def conv_core_temp_test():
    # currently linear so there are no edge cases
    test_array = [24,25,23,23,24,25,23,24,25,24,24,25,28,30,30,30,28,25,26,29,28,28,29,25,23,24,24,24,25,25]
    if conv_core_temp(test_array) == 26.3:
        print "PASS"
    else:
        print "FAIL"

    test_array_2 = [-3,-2,-5,-3,-3,3,0]
    if conv_core_temp(test_array_2) == "INVALID VALUE":
        print "PASS"
    else:
        print "FAIL"


def check_if_fever(est_core_temp):
    # need statistical data to test this on so for now just returns if above or below a certain temp
    temp_threshold = 37.0
    if est_core_temp > temp_threshold:
        return True
    else:
        return False

def check_if_fever_test():
    # this ended up becoming a very simple check because I don't have a fully developed statistical model to judge this on yet
    if check_if_fever(38) == True:
        print "PASS"
    else:
        print "FAIL"

    if check_if_fever(36.0) == False:
        print "PASS"
    else:
        print "FAIL"


# MAIN
if __name__ == '__main__':
    # there aren't a lot of tests because there aren't a lot of things to check yet sorry
    conv_file_test()
    conv_core_temp_test()
    check_if_fever_test()
