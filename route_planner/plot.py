'''
Plot route with recommended stations using folium
'''

import folium
import webbrowser

def plot_map(coos, new_stations, closest_coordinates_strs, start_city, end_city):
    # initialize the map
    #m = folium.Map(location=[38, -120], zoom_start=6) # regular map tile
    m = folium.Map(location=[38, -120], tiles="Stamen Terrain", zoom_start=6) # terrain map tile

    # plot route with polylines
    folium.PolyLine(coos, tooltip="Route").add_to(m)

    # mark the new stations
    for i in range(len(new_stations)):
        test_list = []
        test_list.append(new_stations[i][1])
        test_list.append(new_stations[i][2])

        if test_list in closest_coordinates_strs:
            # recommended station with red
            folium.Marker(
                [new_stations[i][1],new_stations[i][2]],
                icon=folium.Icon(color="red",icon="plus-sign"),
                popup = new_stations[i][3] +' '+ new_stations[i][4]
            ).add_to(m)
        else:
            # other stations
            folium.Marker(
                [new_stations[i][1],new_stations[i][2]],
                popup = new_stations[i][3] +' '+ new_stations[i][4]
            ).add_to(m)

    # output plot
    file_path = "./output maps/{}-{}.html".format(start_city, end_city)
    m.save(file_path)  # save as html file
    webbrowser.open_new(file_path)  # open with default browser




