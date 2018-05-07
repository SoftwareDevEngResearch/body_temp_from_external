#!/usr/bin/env python

# Author: Makenzie Brian
# Date: April 25, 2018
# Class: ME 599
# File: conv_core_temp_test.py
# Description: tests for conv_core_temp.py

import pytest

from ..conv_core_temp import conv_file, conv_core_temperature, check_if_fever 


def test_conv_file():
    """compares file to expected output of known file"""
    real_contents = [['24', '25', '23', '23', '24', '25'], ['23', '24', '25', '24', '24', '25'], ['28', '30', '30', '30', '28', '25'], ['26', '29', '28', '28', '29', '25'], ['23', '24', '24', '24', '25', '25']]
    est_contents = conv_file("data.csv")
    #print conv_file("data.csv")

    # literally just need one simple test because what else can I even check here???
    assert est_contents == real_contents
    
def test_1_conv_core_temp():
    """compares known output average to calculated output average"""
    # currently linear so there are no edge cases
    test_array = [24,25,23,23,24,25,23,24,25,24,24,25,28,30,30,30,28,25,26,29,28,28,29,25,23,24,24,24,25,25]
    assert conv_core_temperature(test_array) == 26.3

        
def test_2_conv_core_temp():
    """compares to known value; known values should be INVALID"""
    test_array_2 = [-3,-2,-5,-3,-3,3,0]
    assert conv_core_temperature(test_array_2) == "INVALID VALUE"
    
def test_1_check_if_fever():
    """confirms values higher than set temp return true; uses int"""
    # this ended up becoming a very simple check because I don't have a fully developed statistical model to judge this on yet
    assert check_if_fever(38) == True
     
    
def test_2_check_if_fever():
    """confirms vlaues lower than set temp return false; uses float"""
    assert check_if_fever(36.0) == False
    
# MAIN
if __name__ == '__main__':
    # there aren't a lot of tests because there aren't a lot of things to check yet sorry
    conv_file_test()
    conv_core_temp_test_1()
    check_if_fever_test_1()
