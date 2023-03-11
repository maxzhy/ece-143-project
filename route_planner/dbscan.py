'''
use DBSCAN to cluster the redundant stations
'''

from sklearn.cluster import DBSCAN
from geopy.distance import great_circle
from shapely.geometry import MultiPoint
import pandas as pd
import numpy as np

def get_centermost_point(cluster):
    centroid = (MultiPoint(cluster).centroid.x, MultiPoint(cluster).centroid.y)
    centermost_point = min(cluster, key=lambda point: great_circle(point, centroid).m)
    return tuple(centermost_point)

def gen_cluster(stations):

    # turn coordinates into Numpy type
    coord = np.array([[row[1], row[2]] for row in stations])
    coords = coord.astype(float)

    kms_per_radian = 6371.0088
    epsi = 10 / kms_per_radian
    db = DBSCAN(eps=epsi, min_samples=1, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
    cluster_labels = db.labels_
    num_clusters = len(set(cluster_labels))
    clusters = pd.Series([coords[cluster_labels == n] for n in range(num_clusters)])

    #print('Original stations: ', len(coord))
    #print('Number of clusters: ', num_clusters)

    centermost_points = clusters.map(get_centermost_point)
    lst = centermost_points.tolist() # lst = [lat, lon]

    # use lst to filter stations
    string_lst = []
    for line in lst:
        line_list = []
        for l in line:
            line_list.append(str(l))
        string_lst.append(line_list)

    new_stations = [] # same as stations: new_stations = ['ids', 'lat', 'lon', 'street', 'city']
    for s in stations:
        s_list = []
        s_list.append(s[1])
        s_list.append(s[2])
        if s_list in string_lst:
            new_stations.append(s)

    return new_stations, lst