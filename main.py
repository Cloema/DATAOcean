#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import plotly
import plotly.graph_objects as go
import pandas as pd
import os

# and the main starts (principal program)
if __name__ == "__main__":

    dir = os.getcwd()
    namefile = dir + '/datalog.csv'

    df = pd.read_csv(namefile)

    fig = go.Figure(data=go.Scattergeo(
        lon=df['Longitude'],
        lat=df['Latitude'],
        text=df['Temperature'],
        mode='markers',
        marker_color='DarkSlateGrey',
    ))

    fig.update_layout(
        title='DATA Oceans<br>ASTROLABE EXPEDITIONS',
        geo_scope='europe',
    )

    plotly.offline.plot(fig, filename='file.html')