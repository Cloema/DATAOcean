#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# main.py
#author : CRI students
#date : september 2019
#version : V1.0


#import for the log
import logging
from datetime import datetime
from calsal import Calcul_salin

# initialization of log setting
logging.basicConfig(filename='./app.log',level=logging.INFO)
logging.info("Beginning of the program\n")
logging.basicConfig(format= '%(asctime)s %(message)s', datefmt='%I:%M:%S %p  %d/%m/%Y')


#and the main starts (principal program)
if __name__ == "__main__":
    try:
        j=1
        test_des_calculs = Calcul_salin()
        for i in range (10):
            j += 0.2
            print ("COUCOU ", i)
            print(test_des_calculs.salinity_calculator(i,j))

    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        logging.info(message)
        #continue