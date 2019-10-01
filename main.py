#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#librairies for the cartography
import plotly
import plotly.graph_objects as go
import pandas as pd

#library for the command on terminal
import os

#import for the log
import logging
from datetime import datetime


#from calsal import Calcul_salin

# initialization of log setting
logging.basicConfig(filename='./app.log',level=logging.INFO)
logging.info("Beginning of the program\n")
logging.basicConfig(format= '%(asctime)s %(message)s', datefmt='%I:%M:%S %p  %d/%m/%Y')

# and the main starts (principal program)
if __name__ == "__main__":
    try:

        #find the current repertory to create a full path
        dir = os.getcwd()
        namefile = dir + '/datalog.csv'

        #read the csv file
        df = pd.read_csv(namefile)


        #creation of the object Figure used for the map
        fig = go.Figure(data=go.Scattergeo(
            lon=df['Longitude'],
            lat=df['Latitude'],
            text=df['Temperature'],
            mode='markers',
            marker_color='DarkSlateGrey',
        ))

        #add infos for the display of the map
        fig.update_layout(
            title='DATA Oceans<br>ASTROLABE EXPEDITIONS',
            geo_scope='europe',
        )

        # display of the map
        plotly.offline.plot(fig, filename='file.html')

    #creation of a log file if there are problems in the code
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        logging.info(message)