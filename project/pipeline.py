import pandas as pd
from sqlalchemy import create_engine

def pipeline():

    print("Fetching data from Mobilithek for Road Accidents")
    # https://www.regionalstatistik.de/genesisws/downloader/00/tables/46241-01-03-4_00.csv

    roadAccidentDataFrame = pd.read_csv("https://www.regionalstatistik.de/genesisws/downloader/00/tables/46241-01-03-4_00.csv")
    print(roadAccidentDataFrame.head())

    roadAccidentDataFrame.dropna() # removing missing values
    # mode processing to be done
    # Question: use only munich data or multiple cities?

    print("Fetching data from kaggle for Weather Data in Munich")
    weatherDataFrame = pd.read_csv("https://www.kaggle.com/datasets/mexwell/weather-data-munich-1954-2022?select=weatherdata.csv")

    print(weatherDataFrame.head())
    weatherDataFrame.dropna() #removing missing values 

    ############################Creating db files############################
    print("Creating Road Accidents Data table")
    roadAccidentDataFrame.to_sql("accident_data",'accident_data.sqlite', if_exists='replace',index=False)

    print("Creating Weather Data table")
    weatherDataFrame.to_sql("weather_data",'weather_data.sqlite',if_exists='replace',index=False)

pipeline()
 