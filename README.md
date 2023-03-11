# ece-143-project
  *UCSD ECE143 G19 Group Project*

## File Tree
```
ece-143-project
├─── dataset
│   ├── California Energy Commission
│   │   ├── [New_ZEV_Sales_Last_updated_01-18-2023.xlsx]
|   |   └── Vehicle_Population_Last_updated_04-29-2022.xlsx
|   └── US Department of Energy
|       ├── Electric and Alternative Fuel Charging Stations.csv
|       └── new_fuel_stations.csv
├─── analysis
│   ├── ev_charger_type
│   │   └── ...
│   ├── mzy_charger_number_timeline
│   │   └── ...
│   ├── mzy_data_preprocess
│   │   └── ...
│   ├── mzy_heatmap
│   │   └── ...
│   └── yinlei_visualization
│       └── ...
├─── visualization
│   ├── ECE 143 Project visuals.ipynb
│   └── ...
├─── route_planner
│   ├── main.py
│   ├── api_call.py
│   ├── dbscan.py
│   ├── station_recommendation.py
│   ├── plot.py
│   ├── dataset
│   │   └── ...
│   ├── output maps
│   │   └── ...
│   ├── __pycache__
│   │   └── ...
│   └── jupyter notebook
│       └── ...
└─── documents
    ├── Proposal.pdf
    └── presentation slides.pdf
```

## How to Run

### Install requirements
```
pip install -r requirements.txt
```

### Visualizations

1. Go to *visualization* folder
2. Run [ECE 143 Project visuals.ipynb](https://github.com/maxzhy/ece-143-project/blob/main/visualization/ECE)

### Route planner

1. Go to *route_planner* folder
2. Open [api_call.py](https://github.com/maxzhy/ece-143-project/blob/main/route_planner/api_call.py) and add your [MapRequest API key](https://developer.mapquest.com/) to `url1` and `url2` and add your [NREL API key](https://developer.nrel.gov/docs/) to `url3`
3. Run [main.py](https://github.com/maxzhy/ece-143-project/blob/main/route_planner/main.py)
4. Enter the start city and end city in command line
5. Find the result it *output maps* folder
