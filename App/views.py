from matplotlib import cm
from matplotlib.tri import Triangulation, TriAnalyzer, UniformTriRefiner
import plotly.graph_objs as go
from datetime import datetime
import json
from django.db import connections
import pandas as pd
import sqlite3
import base64
from django.db.models import Count
from io import BytesIO
import numpy as np
from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import Axes3D
from django.shortcuts import render
import plotly.express as px
from .models import Addresses, Fertilizers, Irrigations, Users, Castors, WaterExpences
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import requests
from mpl_toolkits import mplot3d
import itertools
from plotly.graph_objs.layout import Template
import plotly.graph_objs as go
from plotly.graph_objs.layout import Template
from plotly.graph_objs import scatter
from plotly.graph_objs import layout
import chart_studio.plotly as py
import chart_studio.tools as tls



class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


def chart(request):
    cat = Addresses.objects.all()
    data = list(cat.values())
    co2 = json.dumps(data, cls=CustomEncoder)

    fig = px.pie(
        data,
        values='user_id',
        names='district',
        title="Total Number of Users in Each District",
        hole=0.3,
        height=500,
        width=900
    )

    fig.update_traces(textposition='inside')

    total_users = cat.count()
    fig.update_layout(annotations=[
        dict(text=f'Total Users: {total_users}',
             x=0.5, y=0.5, font_size=10, showarrow=False)
    ])

    chart = fig.to_html()

    years = [2018, 2019, 2020, 2021, 2022]
    saved_water = [25, 35, 50, 60, 75]
    used_water = [50, 60, 70, 80, 85]

    fig1 = px.bar(x=years, y=[saved_water, used_water], barmode='group', labels={
                  'x': 'Year', 'y': 'Water (in units)'})

# update layout
    fig1.update_layout(title={'text': 'Saved and Used Water by Year', 'font': {
                       'size':20}}, xaxis_title='Year', yaxis_title='Water (in units)')

    saved_water_bar = fig1.data[0]
    used_water_bar = fig1.data[1]

    saved_water_bar.name = 'Saved Water'
    saved_water_bar.marker.color = 'black'
    used_water_bar.name = 'Used Water'
    used_water_bar.marker.color = 'yellow'

    chart1 = fig1.to_html()
    data = [{'year': 2019, 'farmer_type': 'External', 'value': 20},
            {'year': 2019, 'farmer_type': 'Internal', 'value': 10},
            {'year': 2020, 'farmer_type': 'External', 'value': 25},
            {'year': 2020, 'farmer_type': 'Internal', 'value': 15},
            {'year': 2021, 'farmer_type': 'External', 'value': 30},
            {'year': 2021, 'farmer_type': 'Internal', 'value': 20},
            {'year': 2022, 'farmer_type': 'External', 'value': 35},
            {'year': 2022, 'farmer_type': 'Internal', 'value': 25}]

    fig3 = go.Figure(data=[go.Scatter3d(
        x=[d['year'] for d in data],
        y=[d['farmer_type'] for d in data],
        z=[d['value'] for d in data],
        mode='markers',
        marker=dict(
            color=[
                'rgb(66, 196, 244)' if d['farmer_type'] == 'External' else 'rgb(255, 165, 0)'
                for d in data
            ],
            size=5,
            symbol='circle',
            line=dict(
                color='black',
                width=2
            )
        )
    )])
    # updating the layout of the chart
    fig3.update_layout(scene=dict(
        xaxis_title='Year',
    ),
        title=dict(
        text="Farmer's Type",
        font=dict(
            size=20,
            color='rgb(66, 196, 244)'
        )
    ),
        width=900,  # increased the width of the chart
        height=500,  # increased the height of the chart
        paper_bgcolor='rgba(0,0,0,0)',  # set background color to transparent
        plot_bgcolor='rgba(0,0,0,0)'  # set plot color to transparent
    )

    chart3 = fig3.to_html()

    irrigations = Irrigations.objects.all()

# Convert the queryset to a list of dictionaries
    data = list(irrigations.values())

# Define the labels and colors for each type of irrigation
    bar_labels = ['Furrow', 'RainFed', 'Alternate Furrow', 'Sprinkler']
    bar_colors = ['red', 'blue', 'green', 'orange']

# Create a mapping between the type of irrigation and the corresponding index in the bar_labels and bar_colors lists
    type_mapping = {'Furrow': 0, 'RainFed': 1,
                    'Alternate Furrow': 2, 'Sprinkler': 3, }

# Replace the type of irrigation in the data with the corresponding index in the type_mapping dictionary
    for d in data:
        d['type'] = next((i for i, v in type_mapping.items()
                          if d['type'].lower() in i.lower()), -1)

# Filter out the data with an unknown type of irrigation
    filtered_data = [d for d in data if d['type'] != -1]

# Create a new list of labels for each data point based on the index in the type_mapping dictionary
    filtered_labels = [bar_labels[type_mapping[d['type']]]
                       for d in filtered_data]

# Create a new list of colors for each data point based on the index in the type_mapping dictionary
    filtered_colors = [bar_colors[type_mapping[d['type']]]
                       for d in filtered_data]

# Group the filtered data by the type of irrigation and count the number of occurrences of each type
    grouped_data = {}
    for d in filtered_data:
        if d['type'] not in grouped_data:
            grouped_data[d['type']] = 1
        else:
            grouped_data[d['type']] += 1

# Convert the grouped data into a list of dictionaries for plotting
    grouped_data_list = [{'type': k, 'count': v}
                         for k, v in grouped_data.items()]

# Create the bar chart
    fig2 = px.bar(
        grouped_data_list,
        x='type',
        y='count',
        color='type',
        color_discrete_sequence=bar_colors,
        title='Irrigation Analysis',
        height=500,
        width=900
    )

# Update the names and colors of each bar in the chart
    Ferrow_bar = fig2.data[0]
    RainFed_bar = fig2.data[1]
    Alternate_Furrow_bar = fig2.data[2]
    Sprinkler_bar = fig2.data[3]

    Ferrow_bar.name = 'Furrow'
    RainFed_bar.name = 'RainFed'
    Alternate_Furrow_bar.name = 'Alternate Furrow'
    Sprinkler_bar.name = 'Sprinkler'

    Ferrow_bar.marker.color = 'red'

    RainFed_bar.marker.color = 'blue'
    Alternate_Furrow_bar.marker.color = 'green'
    Sprinkler_bar.marker.color = 'orange'

# Convert the chart to an HTML string
    chart2 = fig2.to_html()
# Get data from database
    fertilizers = Fertilizers.objects.values('name')
# Define color dictionary
    color_dict = {
    'gypsum': '#ff0000',
    'urea': '#00ff00',
    'Chloro cyper': '#0000ff',
    'Imida': '#FFFF00',
    'DAP': '#FFC0CB',
    'SSP': '#008000',
    'Zinc Sulphate': '#800000',
    'ASP': '#ADD8E6',
    '20-20+0': '#0000FF',
    'NPK': '#FF00FF',
    'Nano UREA': '#FFA500',
    'Bentonite Sulphur': '#A52A2A',
    'Ammonium Sulphate': '#808080',
    'WDG Sulphur 90%': '#FFFFFF',
    'potash': '#800000',
    'Blucopper': '#00FFFF',
    'Nem Doc': '#800080',
    'Castor Cake': '#808000',
    'organic': '#00FF00'
    }

    colors = [color_dict.get(t, '#000000') for t in fertilizers.values_list('name', flat=True)]

    x_values = list(fertilizers.values_list('name', flat=True))
    y_values = list(range(len(fertilizers)))


    fig4 = go.Figure(data=[go.Bar(
    x=y_values,
    y=x_values,
    orientation='h',
    marker=dict(color=colors)
    )])

    fig4.update_layout(
        height=1000,
        width=1500,
        title='Fertilizers',
        template='plotly_white'
    )



    chart4 = fig4.to_html()

    context = {'chart': chart, 'chart1': chart1,
               'chart3': chart3, 'chart2': chart2, 'chart4': chart4}
    return render(request, 'core/graph.html', context)
def distance(x1,y1,x2,y2):
    d=np.sqrt((x1-x2)**2+(y1-y2)**2)
    return d


def distance(x1,y1,x2,y2):
    d=np.sqrt((x1-x2)**2+(y1-y2)**2)
    return d

def graph(request, id=None):
    # Construct the API URL with the ID parameter
    url = f'http://soil-test.solidaridadasia.net/api/get-land-coordinates-by-farmer/{id}'

    # Make the API call and extract the data
    r = requests.get(url, headers={'Authorization': 'Bearer %s' % 'access_token'})
    data = r.json()['data']

    # Extract the x, y, and z values from the data
    x = []
    y = []
    z = []
    moisture = []
    temperature = []
    conductivity = []
    ph = []
    nitrogen = []
    phosphorous = []
    potassium = []
    for point in data:
        z.append(float(point['altitude']))
        x.append(float(point['latitude']))
        y.append(float(point['longitude']))
        moisture.append(float(point['moisture']))
        temperature.append(float(point['temperature']))
        conductivity.append(float(point['electrical_conductivity']))
        ph.append(float(point['pH']))
        nitrogen.append(float(point['nitrogen']))
        phosphorous.append(float(point['phosphorous']))
        potassium.append(float(point['potassium']))

    def idw_npoint(xz,yz,n_point,p):
        r=3 #block radius iteration distance
        nf=0
        while nf<=n_point: #will stop when np reaching at least n_point
            x_block=[]
            y_block=[]
            z_block=[]
            r +=3 # add 10 unit each iteration
            xr_min=xz-r
            xr_max=xz+r
            yr_min=yz-r
            yr_max=yz+r
            for i in range(len(x)):
            # condition to test if a point is within the block
                if ((x[i]>=xr_min and x[i]<=xr_max) and (y[i]>=yr_min and y[i]<=yr_max)):
                    x_block.append(x[i])
                    y_block.append(y[i])
                    z_block.append(z[i])
            nf=len(x_block) #calculate number of point in the block
    
    #calculate weight based on distance and p value
        w_list=[]
        for j in range(len(x_block)):
            d=distance(xz,yz,x_block[j],y_block[j])
            if d>0:
                w=1/(d**p)
                w_list.append(w)
                z0=0
            else:
                w_list.append(0) #if meet this condition, it means d<=0, weight is set to 0
    
        #check if there is 0 in weight list
        w_check=0 in w_list
        if w_check==True:
            idx=w_list.index(0) # find index for weight=0
            z_idw=z_block[idx] # set the value to the current sample value
        else:
            wt=np.transpose(w_list)
            z_idw=np.dot(z_block,wt)/sum(w_list) # idw calculation using dot product
        return z_idw
    n=100 #number of interpolation point for x and y axis
    x_min=min(x)
    x_max=max(x)
    y_min=min(y)
    y_max=max(y)
    w=x_max-x_min #width
    h=y_max-y_min #length
    wn=w/n #x interval
    hn=h/n #y interval

#list to store interpolation point and elevation
    y_init=y_min
    x_init=x_min
    x_idw_list=[]
    y_idw_list=[]
    z_head=[]
    for i in range(n):
        xz=x_init+wn*i
        yz=y_init+hn*i
        y_idw_list.append(yz)
        x_idw_list.append(xz)
        z_idw_list=[]
        for j in range(n):
            xz=x_init+wn*j
            z_idw=idw_npoint(xz,yz,3,1.5) #min. point=5, p=1.5
            z_idw_list.append(z_idw)
        z_head.append(z_idw_list)

    # CREATING 3D TERRAIN
    surface = go.Surface(z=z_head,x=x_idw_list,y=y_idw_list, showscale=False,)
    traces = []
    moisture_text = ['Moisture: {:.2f}'.format(val) for val in moisture]
    temperature_text = ['Temperature: {:.2f}'.format(val) for val in temperature]
    conductivity_text = ['Conductivity: {:.2f}'.format(val) for val in conductivity]
    ph_text = ['pH: {:.2f}'.format(val) for val in ph]
    nitrogen_text = ['Nitrogen: {:.2f}'.format(val) for val in nitrogen]
    phosphorous_text = ['Phosphorous: {:.2f}'.format(val) for val in phosphorous]
    potassium_text = ['Potassium: {:.2f}'.format(val) for val in potassium]

    text = [m + '<br>' + t + '<br>' + c + '<br>' + p + '<br>' + n + '<br>' + po + '<br>' + k         for m,t,c,p,n,po,k in zip(moisture_text, temperature_text, conductivity_text, ph_text, nitrogen_text, phosphorous_text, potassium_text)]

    traces.append(go.Scatter3d(x=x, y=y, z=z, mode='markers',
                            text=text,
                            name='',
                            hoverinfo='text'))
    plot_layout = go.Layout(
        title='Soil Data',
        scene=dict(
            aspectratio=dict(x=2, y=2, z=0.5),
            xaxis=dict(title='Latitude'),
            yaxis=dict(title='Longitude'),
            zaxis=dict(title='Altitude')
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        autosize=True,
    )
    # Create the plot figure
    plot_figure = go.Figure(data=[surface] + traces, layout=plot_layout)
    mesh = go.Mesh3d(x=x, y=y, z=z, color='gray', opacity=0.5, name='', showlegend=False)

# Create trace for highlighted points
    highlighted_points = go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(color='red', size=5), name='', showlegend=False)

# Create trace for lines
    lines = go.Scatter3d(x=x, y=y, z=z, mode='lines', line=dict(color='darkblue', width=2), name='', showlegend=False)

# Create figure and add traces
    fig = go.Figure(data=[mesh,lines]+traces, layout=plot_layout)
# Convert the plot to HTML
    chart = fig.to_html(full_html=False)
    # Generate the plot HTML
    chart1 = plot_figure.to_html(full_html=False)
    xlin = np.linspace(min(x_idw_list), max(x_idw_list), 100)
    ylin = np.linspace(min(y_idw_list), max(y_idw_list), 100)
    X, Y = np.meshgrid(xlin, ylin)

# Interpolate the z-values at each point in the meshgrid
    Z = griddata((x,y), z, (X, Y), method='cubic') # use the interpolation method of your choice
    #wave_amplitude = 5 # adjust the amplitude of the wave
    #wave_frequency = 5 # adjust the frequency of the wave
    #Z_wave = Z + wave_amplitude*np.sin(wave_frequency*X)
    #X_wave = X
    #Y_wave = Y

    wireframe_data = go.Scatter3d(x=X.flatten(), y=Y.flatten(), z=Z.flatten(), mode='lines', line=dict(color='black', width=6),name='')

# Create a 3D surface plot using plotly
    fig2 = go.Figure(data=[wireframe_data]+traces,layout=plot_layout)
    chart2 = fig2.to_html(full_html=False);
    
    context = {'chart': chart,'chart1':chart1,'chart2':chart2}
    return render(request, 'core/chart.html', context)

    


















    



