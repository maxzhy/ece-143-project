'''

'''
# new_data_cleaned.csv structure
# row[0]: Street Address
# row[1]: City
# row[2]: ZIP
# row[3], row[4]: Groups With Access Code, Access Days Time
# row[5]-row[8]: EV Level1 EVSE Num, EV Level2 EVSE Num, EV DC Fast Count, EV Other Info
# row[9], row[10]: Latitude,Longitude
# row[11]: ID
# row[12]: EV Connector Types
# row[13]: Facility Type

import csv

input_csv = './output_dataset/new_data_cleaned.csv'
output_csv = './output_dataset/new_data_cleaned2.csv'
all_data = []

with open(input_csv) as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        if row[7] != '':
            all_data.append(row)
f.close()


with open(output_csv, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    '''
    # 之前已经有表头了
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
    '''
    for line in all_data:
        writer.writerow(line)



