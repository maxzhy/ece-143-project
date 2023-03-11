'''
Recommend stations
'''

from geopy.distance import geodesic
from geopy.distance import distance
import datetime

def recommend(json_distance, json_time, coos, lst):

    dist_btw = [] # distance between two turning points
    for i in range(len(coos)-1):
        d = 0
        pointA = coos[i]
        pointB = coos[i+1]
        d = geodesic(pointA, pointB).miles
        dist_btw.append(d)

    # find stop around which coordinate to find stations
    stop_count = 0 # num of charging
    while ((stop_count) * 200) < json_distance: # json_distance = the real distance
        stop_count += 1
    stop_seg = sum(dist_btw) / stop_count # charge after miles

    dist_count = 0 # how many miles at present
    stop_count2 = 0 # num of stops
    coord_findstation = [] # find stations around these coordinates

    for i in range(len(dist_btw)):
        dist_count += dist_btw[i]
        if dist_count > (stop_count2+1) * stop_seg:
            # find around this coordinate
            coord_findstation.append(coos[i])
            stop_count2 += 1

    # calculate the closest station
    closest_coordinates = []
    for target in coord_findstation:
        coordinates = lst
        closest_distance = float("inf")
        closest_coordinate = None

        for coor in coordinates:
            dist = distance(target, coor).miles  # calculate distance in miles
            if dist < closest_distance:
                closest_distance = dist
                closest_coordinate = coor
        closest_coordinates.append(closest_coordinate)

    # turn closest_coordinates into list & str
    closest_coordinates_strs = [] # closest_coordinates_strs = ['lat', 'lon']
    for i in range(len(closest_coordinates)):
        closest_coordinates_str = []
        closest_coordinates_str.append(str(closest_coordinates[i][0]))
        closest_coordinates_str.append(str(closest_coordinates[i][1]))
        closest_coordinates_strs.append(closest_coordinates_str)

    drive_time = json_time
    charge_time = 3600 * (stop_count-1)
    all_time = drive_time + charge_time
    convert_time = str(datetime.timedelta(seconds = all_time))

    #print('Total distance: ', json_distance)
    print('Time estimation: ', convert_time)

    return closest_coordinates_strs, convert_time


