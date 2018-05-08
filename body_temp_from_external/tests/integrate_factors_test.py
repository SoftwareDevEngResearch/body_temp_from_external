#!/usr/bin/env python

# Author: Makenzie Brian
# Date: April 25, 2018
# Class: ME 599
# File: conv_core_temp_test.py
# Description: tests for conv_core_temp.py

import pytest

from ..integrate_factors import check_if_fever 



def test_1_check_if_fever():
    """confirms values higher than set temp return true; uses int"""
    # this ended up becoming a very simple check because I don't have a fully developed statistical model to judge this on yet
    assert check_if_fever(38) == True
                 
                     
def test_2_check_if_fever():
    """confirms vlaues lower than set temp return false; uses float"""
    assert check_if_fever(36.0) == False



