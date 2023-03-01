'''
Generate EV charger heatmap in CA
'''
import folium
import webbrowser
from folium.plugins import HeatMap
import csv
from itertools import islice

map_obj = folium.Map(location = [38, -119], zoom_start = 6) # open at CA

#csv_data_file = './dataset/data_cleaned.csv'
csv_data_file = './dataset/new_data_cleaned.csv'
#csv_data_file = './dataset/test.csv'

with open(csv_data_file) as csvfile:
    csv_reader = csv.reader(csvfile)
    lats_longs = []
    #for row in csv_reader:
    for row in islice(csv_reader, 1, None):
        line = []
        line.append(row[9]) # Lat
        line.append(row[10]) # Long
        #line.append(0.1) # weight
        lats_longs.append(line)

HeatMap(lats_longs).add_to(map_obj)

if __name__ == '__main__':
    file_path = r"new_heatmap_ca.html"
    map_obj.save(file_path)  # save as html file
    webbrowser.open(file_path)  # open with default browser