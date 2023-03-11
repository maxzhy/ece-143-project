'''
Route planner
@author: Zhaoyang

presuppose:
1. only use DC fast charges
2. assume user have access to all DCFC
3. charge at most once every 200 miles
'''

from api_call import CallAPI
from dbscan import gen_cluster
from station_recommendation import recommend
from plot import plot_map

if __name__ == '__main__':
    # start point and end point
    start_city = input('Enter start city name: ')
    end_city = input('Enter start city name: ')

    # call APIs
    api = CallAPI(start_city, end_city)
    [json_distance, json_time, coos] = api.maprequest_api()
    stations = api.nrel_api()

    # DBSCAN
    [new_stations, lst] = gen_cluster(stations)

    # recommend
    closest_coordinates_strs = recommend(json_distance, json_time, coos, lst)
    print('Total distance: ', json_distance)

    # plot
    plot_map(coos, new_stations, closest_coordinates_strs, start_city, end_city)
