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

## How to run

### install requirements

`pip install -r requirements.txt`

### Visualizations

1. Go to *visualization* folder
2. Run [ECE 143 Project visuals.ipynb](https://github.com/maxzhy/ece-143-project/blob/main/visualization/ECE 143 Project visuals.ipynb)

### Route planner

1. Go to *route_planner* folder
2. Run [main.py](https://github.com/maxzhy/ece-143-project/blob/main/route_planner/main.py)
3. Enter the start city and end city in command line
4. Find the result it *output maps* folder
