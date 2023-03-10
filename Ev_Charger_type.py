#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 00:01:32 2023

@author: evangelinejing
"""
import csv
import numpy as np 
import matplotlib.pyplot as plt
want_to_opne = '/Users/evangelinejing/Downloads/143_data/ev_charger_type/data_cleaned.csv'
want_to_out = '/Users/evangelinejing/Downloads/143_data/ev_charger_type/Ev_Charger_type.csv'
type_file = '/Users/evangelinejing/Downloads/143_data/ev_charger_type/Ev_Charger_type.csv'
out_cities = '/Users/evangelinejing/Downloads/143_data/ev_charger_type/Ev_cities.csv'
type_file = '/Users/evangelinejing/Downloads/143_data/ev_charger_type/Ev_Connectors.csv'
type_cities = '/Users/evangelinejing/Downloads/143_data/ev_charger_type/Ev_cities.csv'
Latitude =  '/Users/evangelinejing/Downloads/143_data/ev_charger_type/Ev_Latitude.csv'
Longitude = '/Users/evangelinejing/Downloads/143_data/ev_charger_type/Ev_Longitude.csv'
level2 = '/Users/evangelinejing/Downloads/143_data/ev_charger_type/Ev_level2.csv'
DCFC = '/Users/evangelinejing/Downloads/143_data/ev_charger_type/DCFC.csv'
TESLA ='/Users/evangelinejing/Downloads/143_data/ev_charger_type/TESLA.csv'
level1 = '/Users/evangelinejing/Downloads/143_data/ev_charger_type/level1.csv'
with open(want_to_opne) as WTO:
    file_read = csv.reader(WTO)

    all_data = []
    for row in file_read:
        #print(row[12])
        all_data.append(row)
        #print(len(all_data))
        
        '''
        types = []
        n = str(row[12])
        
        types.append(n)
        #types = tuple(types)
        
        for i in types:
            i_types = tuple(i)
        #print(i_types)
        count = 0
        for i in i_types:
            if i == 'B':
                count = count+1
        location = np.where(count == 1)

        check = np.array(location)
        
        #print(check)
        

        #print(test[0])
        '''
  

        
with open(want_to_out, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Charger_Connector_Type'])
    for i in range(len(all_data)):
    
        try_writing = [all_data[i][12]]
        writer.writerow(try_writing)

with open(type_file) as connectors:
    file_read = csv.reader(connectors)
    Con_types = []
    for row in file_read:
        #print(row[12])
        Con_types.append(row)
     
        
    ''' 
    a = 0
    b = a+1
    c = np.array([])
    for i in range(len(Con_types)):
        
        
        while b<= i:
            stack_a = np.array([Con_types[a][0]])
            stack_b = np.array([Con_types[b][0]])
            c = np.hstack([stack_a,stack_b])
            
            b = b+1
            a = a+1
        print(c)
            
     '''  
        
   
        
    
    #print ((Con_types[2][0]))

    
    
    

    count_J1772 = 0 
    count_CHADEMO = 0
    count_ccs = 0 
    count_ALL_DC = 0
    count_CHADEMO_J1772_J1772COMBOl = 0
    count_CHADEMO_J1772 = 0
    count_J1772_J1772COMBO = 0
    count_Tesla = 0 
    count_Tesla_J1772 = 0
      
    Total_CCS = 1292
    Total_CHADEMO = 1356
    Total_J1772 = 14220
    Total_connectors = len(Con_types)
    Total_Tesla = 1132
    Total_NEMA = 48
    Total_AC = Total_NEMA+Total_J1772
    Total_DC = Total_Tesla+Total_CHADEMO+Total_CCS
    
    for i in range(len(Con_types)) :
        if Con_types[i][0] == 'J1772':
            count_J1772 = count_J1772+1
    t = '# of locations that have only J1772 Level 2 Connectors: '
    t = t.title()
    #print(t,count_J1772)
                   
    for i in range(len(Con_types)) :
        if Con_types[i][0] == 'CHADEMO':
            count_CHADEMO = count_CHADEMO+1
    tt = '# of locations that have only CHADEMO Connectors: '
    tt = tt.title()
    #print(tt,count_CHADEMO)
       
    for i in range(len(Con_types)) :
        if Con_types[i][0] == 'J1772COMBO':
            count_ccs = count_ccs+1  
    ttt = '# of locations that have only CCS Connectors: '
    ttt = ttt.title()
    #print(ttt,count_ccs)
    
    for i in range(len(Con_types)):
        if Con_types[i][0] == 'CHADEMO J1772COMBO':
            
            count_ALL_DC += 1
    text = '# of locations that both (CHADEMO CCS) DC Fast Connectors: '
    text = text.title()
    #print(text, count_ALL_DC)

    for i in range(len(Con_types)):
        if Con_types[i][0] == 'CHADEMO J1772 J1772COMBO':
            
            count_CHADEMO_J1772_J1772COMBOl += 1
    text = '# of locations that have all connector types (CHADEMO CCS and J1772): '
    text = text.title()
    #print(text, count_CHADEMO_J1772_J1772COMBOl)
    
    for i in range(len(Con_types)):
        if Con_types[i][0] == 'CHADEMO J1772':
            count_CHADEMO_J1772 += 1
        elif Con_types[i][0] == 'J1772 CHADEMO':
            count_CHADEMO_J1772 += 1
    text = '# of locations that support DC CHADEMO, AC J1772 connectors: '
    text = text.title()
    #print(text, count_CHADEMO_J1772)
    
    for i in range(len(Con_types)):
        if Con_types[i][0] == 'J1772 J1772COMBO':
            count_J1772_J1772COMBO += 1
        elif Con_types[i][0] == 'J1772 J1772COMBO':
            count_J1772_J1772COMBO += 1
            
            
    text = '# of locations that support DC CCS J1772COMBO, AC J1772 connectors: '
    text = text.title()
    #print(text, count_J1772_J1772COMBO)

    
    for i in range(len(Con_types)) :
        if Con_types[i][0] == 'TESLA':
            count_Tesla = count_Tesla+1
    t = '# of locations that have only Tesla Connectors: '
    t = t.title()
    #print(t,count_Tesla)
    

    for i in range(len(Con_types)) :
        if Con_types[i][0] == 'J1772 TESLA':
            count_Tesla_J1772 = count_Tesla_J1772+1
    t = '# of locations that have  Tesla DCFC and J1772 AC connectors: '
    t = t.title()
    #print(t,count_Tesla_J1772)
    


    
    All_Types = ('count_J1772', 'count_CHADEMO', 'count_ccs' ,'count_ALL_DC' ,
             'count_CHADEMO_J1772_J1772COMBOl' ,'count_CHADEMO_J177',
             'count_Tesla','count_Tesla_J1772')
    All_Numbers = (count_J1772, count_CHADEMO, count_ccs ,count_ALL_DC,
             count_CHADEMO_J1772_J1772COMBOl, count_CHADEMO_J1772,
             count_Tesla,count_Tesla_J1772)
    
    All_zip = zip(All_Types,All_Numbers)
    Types_dict = dict(tuple(All_zip))
    
    Total_connectors = len(Con_types)
    not_all = Total_connectors - count_CHADEMO_J1772_J1772COMBOl
    
    '''
    y = np.array([not_all, count_CHADEMO_J1772_J1772COMBOl])
    mylabels = [ 'Locations that support partial EVs', 'Locations that support ALL EVs']
    myexplode = [0.1, 0.1]
    
    plt.pie(y, labels = mylabels, explode = myexplode,)
    plt.legend(title = "% of locations that offer all EVSE: ")
    plt.show() 
    '''
    
    
    '''
    y = np.array([count_ccs,count_J1772,count_CHADEMO, count_Tesla])
    mylabels = [ 'CCS Only', 'AC Only','CHADEMO Only', 'Tesla Only']
    myexplode = [0.1, 0.2, 0.1,0.1]
    
    plt.pie(y, labels = mylabels, explode = myexplode,)
    plt.legend(title = "Only One Type Of Connectors: ")
    plt.show() 
    '''
    
    
    '''
    Exists_Universal_DC = count_CHADEMO + count_ccs +count_ALL_DC+ count_CHADEMO_J1772_J1772COMBOl
    Exists_Tesla_DC = count_Tesla+count_Tesla_J1772
    y = np.array([ count_J1772,Exists_Universal_DC,Exists_Tesla_DC])
    mylabels = [ 'AC Only','Universal DCFC',  'Tesla DCFC']
    myexplode = [0.1, 0.1, 0.1]
    
    plt.pie(y, labels = mylabels, explode = myexplode,)
    plt.legend(title = "DCFC vs AC Level2: ")
    plt.show() 
    '''


    '''
    y = np.array([ Total_Tesla,Total_CCS, Total_CHADEMO])
    mylabels = [ 'Tesla','US/Euro EV','Japanese EV']
    myexplode = [0, 0, 0]
    
    plt.pie(y, labels = mylabels, explode = myexplode,)
    plt.legend(title = "ALL DCFC's: ")
    plt.show() 
    '''

    
    '''
    y = np.array([ Total_AC, Total_DC])
    mylabels = [ '# of AC Connectors in CA', '# of DC connectors in CA']
    myexplode = [0.1, 0]
    
    plt.pie(y, labels = mylabels, explode = myexplode,)
    plt.legend(title = "# of AC and DC connectors in CA:  ")
    plt.show() 
    '''
    
   
with open(out_cities, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    #writer.writerow(['Cities'])
    for i in range(len(all_data)):
    
        try_writing = [all_data[i][1]]
        writer.writerow(try_writing)
    
with open(type_file) as connectors:
    file_read = csv.reader(connectors)
    
    Con_types = []
    for row in file_read:
        #print(row[12])
        Con_types.append(row)
        
    population = list(range(len(all_data)))
    dic_con = {}
    trail = []
    for i in population :
        dic_con[i] = Con_types[i][0]
    #print(range(len(dic_con.keys())))

with open(type_cities) as cities :
    file_cities = csv.reader(cities)
    
    cities = []
    for i in file_cities:
        cities.append(i)
    population = list(range(len(all_data)))
    dic_cities = {}
    for i in population :
        dic_cities[i] = cities[i][0]
    #print(dic_cities)
    #print(list(dic_cities.values()))
    
all_cities = list(dic_cities.values())
#print(all_cities)
all_cons = list(dic_con.values())
#print(all_cons)

my_zip = zip(all_cities,all_cons)
zip_tuple = (tuple(list(my_zip)))

number=[]
for i,words in enumerate (zip_tuple,1):
    if 'San Diego' in words:
        number.append(i)
#print(number)
   
    
def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
 
List = all_cities
LA = most_frequent(List)
print(most_frequent(List))


def remove_items(test_list, item):
 
    # using list comprehension to perform the task
    res = [i for i in test_list if i != item]
 
    return res

test_list = all_cities
item = most_frequent(List)

def Second_frequent(NO_LA):
    counter = 0
    num = NO_LA[0]
     
    for i in NO_LA:
        curr_frequency = NO_LA.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num

NO_LA = remove_items(test_list, item)
SD = Second_frequent(NO_LA)
print(Second_frequent(NO_LA))
    


def Third_frequent(NO_LASD):
    counter = 0
    num = NO_LASD[0]
     
    for i in NO_LASD:
        curr_frequency = NO_LASD.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
NO_LASD = remove_items(NO_LA, SD)
print(Third_frequent(NO_LASD))




'''
my_cons = []

for i in all_cons:
    
    n = i.split()

    con_list = [''.join(ele) for ele in n]
    #print(con_list)
    my_cons.append(con_list)
again = [''.join(ele) for ele in my_cons]
'''



with open(want_to_opne) as WTO:
    file_read = csv.reader(WTO)

    all_data = []
    for row in file_read:
        #print(row[12])
        all_data.append(row)
        #print(len(all_data))
with open(Latitude, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    #writer.writerow(['Charger_Connector_Type'])
    for i in range(len(all_data)):
    
        try_writing = [all_data[i][9]]
        writer.writerow(try_writing)
        
with open(Longitude, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    #writer.writerow(['Cities'])
    for i in range(len(all_data)):
    
        try_writing = [all_data[i][10]]
        writer.writerow(try_writing)
with open(level2, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    #writer.writerow(['Cities'])
    for i in range(len(all_data)):
    
        try_writing = [all_data[i][6]]
        writer.writerow(try_writing)
        
with open(DCFC, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    #writer.writerow(['Cities'])
    for i in range(len(all_data)):
    
        try_writing = [all_data[i][7]]
        writer.writerow(try_writing)
        
        
with open(level1, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    #writer.writerow(['Cities'])
    for i in range(len(all_data)):
    
        try_writing = [all_data[i][5]]
        writer.writerow(try_writing)
      

with open(Latitude) as length:
    file_read = csv.reader(length)
    
    Con_Latitude = []
    for row in file_read:
        #print(row[12])
        Con_Latitude.append(row)
        
    population = list(range(1,len(all_data)))
    dic_Latitude = {}
    trail = []
    for i in population :
        dic_Latitude[i] = Con_Latitude[i][0]
    #print(range(len(dic_con.keys())))

with open(Longitude) as Longitudes :
    file_cities = csv.reader(Longitudes)
    
    Longitudes = []
    for i in file_cities:
        Longitudes.append(i)
    population = list(range(1,len(all_data)))
    dic_Longitude = {}
    for i in population :
        dic_Longitude[i] = Longitudes[i][0]
    #print(dic_cities)
    #print(list(dic_cities.values()))
    
with open(level2) as twos :
    file_two = csv.reader(twos)
    
    levelT = []
    for i in file_two:
        levelT.append(i)
    population = list(range(1,len(all_data)))
    dic_level2 = {}
    for i in population :
        dic_level2[i] = levelT[i][0]
        
with open(level1) as ones :
    file_one = csv.reader(ones)
    
    levelO = []
    for i in file_one:
        levelO.append(i)
    population = list(range(1,len(all_data)))
    dic_level1 = {}
    for i in population :
        dic_level1[i] = levelO[i][0]   

with open(DCFC) as d :
    file_d = csv.reader(d)
    
    level3 = []
    for i in file_d:
        level3.append(i)
    population = list(range(1,len(all_data)))
    dic_level3 = {}
    for i in population :
        dic_level3[i] = level3[i][0] 
        
    
all_Latitudes = list(dic_Latitude.values())

all_Longitudes = list(dic_Longitude.values())

level2_list = list(dic_level2.values())
level1_list = list(dic_level1.values())
level3_list = list(dic_level3.values())

#print(len(all_Latitudes))
#print(len(all_Longitudes))
la_max = max(all_Latitudes)
la_min = min(all_Latitudes)
longmax = max(all_Longitudes)
longmin = min(all_Longitudes)
print(la_max,la_min)
#print(longmax,longmin)
x = []
y = []

        
leveltwo = []
levelone = []
levelthree = []
US =['USA']*len(all_Latitudes)
for i in range(len(all_Latitudes)):
    xx = float(all_Latitudes[i])
    yy = float(all_Longitudes[i])    
    tt = level2_list[i]
    oo = level1_list [i]
    ttt = level3_list[i]
    leveltwo.append(tt)
    levelone.append(oo)
    levelthree.append(ttt)
    x.append(xx)
    y.append(yy)


for i in range(len(all_Latitudes)):
    #print(tuple(leveltwo[i]))
    if tuple(leveltwo[i]) == ():
        leveltwo[i] = '0'

for i in range(len(all_Latitudes)):
    #print(tuple(levelone[i]))
    if tuple(levelone[i]) == ():
        levelone[i] = '0'

for i in range(len(all_Latitudes)):
    #print(tuple(levelthree[i]))
    if tuple(levelthree[i]) == ():
        levelthree[i] = '0'
        
l2 = []
for i in range(len(all_Latitudes)):
    ttt = int(leveltwo[i])
    l2.append(ttt)
    
dcfc = []

for i in range(len(all_Latitudes)):
    ttt = int(levelthree[i])
    dcfc.append(ttt)

l1 = []
for i in range(len(all_Latitudes)):
    ttt = int(levelone[i])
    l1.append(ttt)
    
    
        



data_l2=pd.DataFrame({'latitude':x, 'longitude':y, 'count':l2, 'US':US})
data_l1=pd.DataFrame({'latitude':x, 'longitude':y, 'count':l1, 'US':US})
data_dcfc=pd.DataFrame({'latitude':x, 'longitude':y, 'count':dcfc, 'US':US})


#sns.scatterplot(x=y, y=y)
my_datalist = ['data_l2', 'data_l1', 'data_dcfc']


#fig = px.density_mapbox(i, lat='latitude', lon='longitude', z='count',
                        #mapbox_style="stamen-terrain")
    

#iplot(fig) 
#print(data['count'])
#figg = px.scatter_geo(data, lat='latitude', lon='longitude', color="continent", size=50)
#iplot(figg) 
    
import plotly.graph_objects as go  
fig_l2= go.Figure(go.Scattergeo(
    lat=data_l2['latitude'],
    lon=data_l2['longitude'],

    marker = dict(
            size = 12,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'circle',
            line = dict(
                width=1,
                color='rgba(102, 102,102)'
            ),
            colorscale = px.colors.diverging.BrBG,
            cmin = 0,
            color = data_l2['count'],
            cmax = data_l2['count'].max(),
            colorbar=dict(
                title='Level2 Charger Density',
                tickvals=[0,25,50,75,100,150,200,250,300,data_l2['count'].max()],
            )
            
)))
fig_l2.update_layout(
        geo_scope='usa',
    )

#fig_l2.show()

fig_l1= go.Figure(go.Scattergeo(
    lat=data_l1['latitude'],
    lon=data_l1['longitude'],

    marker = dict(
            size = 12,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'circle',
            line = dict(
                width=1,
                color='rgba(102, 102,102)'
            ),
            colorscale = px.colors.diverging.BrBG,
            cmin = 0,
            color = data_l1['count'],
            cmax = data_l1['count'].max(),
            colorbar=dict(
                title='Level1 Charger Density',
                tickvals=[0,5,10,20,30,40,50,60,data_l1['count'].max()],
            )
            
)))
fig_l1.update_layout(
        geo_scope='usa',
    )

#fig_l1.show()


fig_dcfc= go.Figure(go.Scattergeo(
    lat=data_dcfc['latitude'],
    lon=data_dcfc['longitude'],

    marker = dict(
            size = 12,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'circle',
            line = dict(
                width=1,
                color='rgba(102, 102,102)'
            ),
            colorscale = px.colors.diverging.BrBG,
            cmin = 0,
            color = data_dcfc['count'],
            cmax = data_dcfc['count'].max(),
            colorbar=dict(
                title='DCFC Charger Density',
                tickvals=[0,5,10,20,30,40,50,60,data_dcfc['count'].max()],
            )
            
)))
fig_dcfc.update_layout(
        geo_scope='usa',
    )

#fig_dcfc.show()

with open(TESLA, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    #writer.writerow(['Charger_Connector_Type'])
    for i in range(len(all_data)):
    
        try_writing = [all_data[i][12]]
        writer.writerow(try_writing)

with open(TESLA) as T :
    file_T = csv.reader(T)
    
    tesla = []
    for i in file_T:
        tesla.append(i)
    population = list(range(1,len(all_data)))
    dic_tesla = {}
    for i in population :
        dic_tesla[i] = tesla[i][0] 

level3_tesla = list(dic_tesla.values())      

teslaonly=[]  


for i in range(len(level3_tesla)):
    #print(tuple(level3_tesla))
    if tuple(level3_tesla) == (TESLA):
        teslaonly[i] = '1' 
    else:
        teslaonly[i] = '0' 
    print(teslaonly)
        
        

        
        
        
        
        
        
        
        
        















        
    