'''
Call APIs
'''
import requests
import json
import csv
import numpy as np
import sys
import os

class CallAPI:
    def __init__(self, start_city, end_city):
        # full cities name
        start = start_city + ', CA'
        end = end_city + ', CA'

        self.start = start
        self.end = end
        self.coos = []

    def maprequest_api(self):

        start = self.start
        end = self.end
        
        # call MapRequest API to get general info
        url1 = f'http://www.mapquestapi.com/directions/v2/route?key=24Kb50gRGAB4ndDacHzA6CHHJIHsiDkT&from={start}&to={end}'
        response1 = requests.get(url1).json()
        sid = response1['route']['sessionId']
        json_distance = response1['route']['distance'] # distance between start to end in miles
        json_time = response1['route']['time'] # general time of the trip, usually < realtime

        # with the sessionId obtained from above API, get the detailed route in polyline format
        url2 = f'http://www.mapquestapi.com/directions/v2/routeshape?key=24Kb50gRGAB4ndDacHzA6CHHJIHsiDkT&sessionId={sid}&generalize=1000'
        response2 = requests.get(url2).json()
        lat_lng = response2['route']['shape']['shapePoints']

        arr = np.array(lat_lng)
        arr_2d = arr.reshape(-1, 2)
        coos = arr_2d.tolist() # all the turning points
        
        # coordinates of the polylines turning points: coos = [lat, lng]
        arr = np.array(lat_lng)
        arr_2d = arr.reshape(-1, 2)
        coos = arr_2d.tolist()

        self.coos = coos

        return json_distance, json_time, coos

    def nrel_api(self):
        coos = self.coos

        # add turning coordinates as [lng+lat]
        coos_add = []
        for c in coos:
            c1 = ('{}' +'+'+ '{}').format(c[1], +c[0])
            coos_add.append(c1)
        # if less than 2 points: throw error
        if len(coos_add) < 2:
            print('error')
            sys.exit(0)
        # add turning coordinates together for API usage
        left = coos_add[0]
        for i in range(len(coos_add)-1):
            right = coos_add[i+1]
            left = ('{}' +','+ '{}').format(left, right)
        
        url3 = f'https://developer.nrel.gov/api/alt-fuel-stations/v1/nearby-route.json?api_key=MIjVh1EiBsSCU31yFaRJWDSXc6qYeepqfOgShgWZ&return_type=ids&fuel_type=ELEC&distance=1&route=LINESTRING({left})'
        response3 = requests.get(url3).json()

        ids = response3['fuel_station_ids'] # station ids
        ids_str = [str(x) for x in ids] # int -> str

        # compare the obtained ids with cleaned dataset and remove those not in dataset
        stations = [] # stations = ['ids', 'lat', 'lng', 'street address', 'city']
        with open('./dataset/new_data_cleaned2.csv', 'r') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                if row[11] in ids_str:
                    station = []
                    station.append(row[11]) # ids
                    station.append(row[9]) # lat
                    station.append(row[10]) # lng
                    station.append(row[0]) # street address
                    station.append(row[1]) # city
                    stations.append(station)
        f.close()
        '''
        # json 3
        with open('out3.json', 'r') as j3file:
            station3 = json.load(j3file)
        j3file.close()
        ids = station3['fuel_station_ids'] # station ids

        # id: int to str
        ids_str = [str(x) for x in ids]

        # compare the obtained ids with cleaned dataset and remove those not in dataset
        stations = [] # stations = [ids, lat, lng, street address]
        with open('./dataset/new_data_cleaned2.csv', 'r') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                if row[11] in ids_str:
                    station = []
                    station.append(row[11])
                    station.append(row[9])
                    station.append(row[10])
                    station.append(row[0]) # street address
                    station.append(row[1]) # city
                    stations.append(station)
        f.close()
        '''
        return stations


