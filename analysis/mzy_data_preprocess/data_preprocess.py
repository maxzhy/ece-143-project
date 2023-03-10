'''
Data filtering:
1. Fuel Type Code = ELEC
2. State = CA
3. Expected Data = None
4. Groups With Access Code = access_allow
5. Removed some outliers

Kept following columns:
1. Street Name
2. City
3. ZIP
4. Groups With Access Code: station time
5. Access Days Time: how to access
6. EV Level1/Level2 EVSE Num, DC Fast Count, Other Info: charger type
7. Latitude & Longitude: coordinate
8. ID: unique identification
9. EV Connector Types: connector type
10. Facility Type: surrounding facilities

@author: Zhaoyang
'''

import csv

test_csv_file = './web_dataset/new_fuel_stations.csv'
out_csv_file = './output_dataset/new_data_cleaned.csv'

access_allow = ['Public', 
                'Public - Card key at all times', 
                'Public - Credit card at all times', 
                'Public - Call ahead', 
                'Private', 
                'Private - Credit card at all times']
all_data = []

with open(test_csv_file) as csvfile:
    csv_reader = csv.reader(csvfile)

    #fil = [] # filter a specific column

    for row in csv_reader:

        # filter EV, Cal, not Expected, accessible, filter out some points in other states
        if row[0]=='ELEC' and row[5]=='CA' and row[10]=='' and row[11] in access_allow and float(row[25]) < -112:

            #print(row[0]) # fuel type: ELEC
            #print(row[2]) # street name
            #print(row[4]) # city (should get lowercase!)
            #print(row[5]) # state
            #print(row[6]) # zip code
            #print(row[11]) # accessibilty: private/public/...
            #print(row[12]) # access daytime: (fleet)
            #print(row[17],'|',row[18],'|',row[19],'|',row[20]) # EV charger type and count
            #print(row[24],'|',row[25]) # latitude and longitude
            #print(row[27]) # unique ID
            #print(row[37]) # charger connector type
            #print(row[47]) # facility type: standalone, convenience store

            #fil.append(row[4])
            all_data.append(row)

    '''
    # filter specific data for observation
    fil_set = set(fil)
    for i in fil_set:
        print(i)
    '''

with open(out_csv_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)

    # write header
    writer.writerow(['Street Address',
                     'City',
                     'ZIP',
                     'Groups With Access Code',
                     'Access Days Time',
                     'EV Level1 EVSE Num',
                     'EV Level2 EVSE Num',
                     'EV DC Fast Count',
                     'EV Other Info',
                     'Latitude',
                     'Longitude',
                     'ID',
                     'EV Connector Types',
                     'Facility Type'])

    for i in range(len(all_data)):
        
        outrow = [all_data[i][2],all_data[i][4],all_data[i][6],all_data[i][11],all_data[i][12],all_data[i][17],all_data[i][18],
                  all_data[i][19],all_data[i][20],all_data[i][24],all_data[i][25],all_data[i][27],all_data[i][37],all_data[i][47]]
        writer.writerow(outrow)
        


