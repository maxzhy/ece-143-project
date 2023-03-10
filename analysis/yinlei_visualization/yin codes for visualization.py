'''
@author: yinlei
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_for_sales_over_time(location_sale):
    '''
    location gives the directory for the excel file, "New_ZEV_Sales_Last_updated_01-18-2023.xlsx"
    '''
    dfs = pd.read_excel(location_sale, 'County')
    dfs= dfs[~(dfs['FUEL_TYPE'] =='Hydrogen')]
    dfs_newsale_amount_over_time = dfs.groupby('Data Year').sum()
    plt.figure(figsize=(8, 6))
    plt.plot(dfs_newsale_amount_over_time.index, dfs_newsale_amount_over_time["Number of Vehicles"], marker = '.')
    plt.xlabel('Data Year')
    plt.ylabel('No. of Vehicles Sold')
    plt.title('Vehicles Sold Over the Years')
    plt.show()

def plot_for_sale_in_counties(location_sale):
    '''
    gives the plot of all vehcles sold in different counties
    '''
    dfs = pd.read_excel(location_sale, 'County')
    dfs= dfs[~(dfs['FUEL_TYPE'] =='Hydrogen')]
    dfs_amount_over_places = dfs.groupby(by = 'County')['Number of Vehicles'].sum()
    dfs_amount_over_places = dfs_amount_over_places.sort_values()
    plt.figure(figsize=(8, 6))
    plt.bar(dfs_amount_over_places.index, dfs_amount_over_places)
    plt.xlabel('Counties in CA')
    plt.ylabel('Total No. of Vehicles Sold')
    plt.title('Vehicles Sold in Different Regions of CA')
    plt.show()

def recent_trend_of_pref_between_elec_and_phev(location_sale):
    '''
    gives the plot of sales of ev cars and phev over the past 10 years
    '''
    dfs = pd.read_excel(location_sale, 'County')
    dfs= dfs[~(dfs['FUEL_TYPE'] =='Hydrogen')]
    dfs_recent = dfs[dfs['Data Year'] > 2009]
    dfs_recent_group = dfs_recent.groupby('FUEL_TYPE')
    dfs_recent_sum = {}
    for kind in ['Electric', 'PHEV']:
        dfs_recent_sum[kind] = dfs_recent_group.get_group(kind).groupby(by="Data Year")["Number of Vehicles"].sum()
        
    plt.figure(figsize=(8, 6))
    plt.plot(dfs_recent_sum['Electric'].index, dfs_recent_sum['Electric'], 'r-', dfs_recent_sum['Electric'].index, dfs_recent_sum['PHEV'], 'b-', marker = '.')
    plt.xlabel('Sale Year')
    plt.ylabel('Total No. of Vehicles Sold')
    plt.title('Different Types of EVs Sold in CA Over the Years')
    plt.legend(loc='upper left', shadow=True, fontsize='x-large', labels = ['Purely Electric', "Plug-in Hybrid"])
    plt.show()
    
def recent_brand_pref(location_sale):
    '''
    gives the pie chart of recent sales of the predominant ev brands
    '''
    dfs = pd.read_excel(location_sale, 'County')
    dfs= dfs[~(dfs['FUEL_TYPE'] =='Hydrogen')]
    dfs_recent = dfs[dfs['Data Year'] > 2009]
    dfs_recent_brand = dfs_recent.groupby(by = 'MAKE')['Number of Vehicles'].sum()
    dfs_recent_brand = dfs_recent_brand.sort_values()
    dfs_recent_brand['The rest'] = 0
    dfs_recent_brand_mono = dfs_recent_brand
    for brand in ['Audi', 'BMW', 'Bentley', 'Cadillac', 'Chevrolet', 'Chrysler', 'FIAT', 'Ferrari', 'Fisker', 'Ford', 'GMC', 'Genesis', 'Honda', 'Hyundai', 'Jaguar', 'Jeep', 'Karma', 'Kia', 'Land Rover', 'Lexus', 'Lincoln', 'Lucid', 'MINI', 'Mazda', 'McLaren', 'Mercedes-Benz', 'Mitsubishi', 'Nissan', 'Polestar', 'Porsche', 'Rivian', 'Scion', 'Smart', 'Subaru', 'Tesla', 'Toyota', 'Toyota/Subaru', 'Volkswagen', 'Volvo']:
        if dfs_recent_brand_mono[brand] < dfs_recent_brand_mono['Honda']:
            dfs_recent_brand_mono['The rest'] += dfs_recent_brand_mono[brand]
            del dfs_recent_brand_mono[brand]
    plt.figure(figsize=(10, 8))
    plt.pie(dfs_recent_brand_mono, labels = dfs_recent_brand_mono.keys(), autopct='%1.1f%%')
    plt.title('Percentages of Total Sales Made by Each Brand')
    plt.show()

def pie_chart_car_population(location_population):
    '''
    gives the pie chart of percentage of each fuel type in ca
    this chart uses a different excel file, called 'Vehicle_Population_Last_updated_04-29-2022.xlsx'
    '''

    dfp = pd.read_excel(location_population)
    dfp_most_recent = dfp.groupby(by = 'Data Year')
    dfp_most_recent.groups.keys()
    dfp_2021 = dfp_most_recent.get_group(2021)
    dfp_cur_ft = dfp_2021.groupby(by = 'Fuel Type')['Number of Vehicles'].sum()
    plt.figure(figsize=(11, 11))
    plt.pie(dfp_cur_ft, labels = dfp_cur_ft.keys(), autopct='%1.1f%%')
    plt.title('Percentages of Each Fuel Type in CA')
    plt.show()
