import pandas as pd
from sqlalchemy import create_engine
import sqlite3

def pipeline():

    #Source 1
    print("Fetching data from Open Data Nepal for Gender Wise student distribution across Universities ")
    df_gender = pd.read_csv("https://opendatanepal.com/dataset/5fb1e284-d6a0-4d7d-8945-1632e32bf1f6/resource/3529bfab-cca9-4170-bf5c-599eb9e8e545/download/university-wise-student-enrollment-of-higher-education-by-sex-in-2074-bs.csv")
    print(df_gender.head())
    df_gender.dropna() # removing missing values

    #Source 2
    print("Fetching data from Open Data Nepal for University wise student enrollment")
    df_university = pd.read_csv("https://opendatanepal.com/dataset/cda79f68-e517-4666-9d92-8601418ceb80/resource/5193053a-b6fe-45e7-a6ba-8aae99ced378/download/university-wise-student-enrollment-of-higher-education-by-types-of-campuses-in-2074-bs.csv")
    print(df_university.head())
    df_university.dropna() #removing missing values 

    #Source 3
    print("Fetching data from Open Data Nepal for Province Wise student distribution across Universities")
    df_province = pd.read_csv("https://opendatanepal.com/dataset/df7ab4c7-384a-4175-bc19-044fade5c8f2/resource/f4674ab7-5f5f-4a04-ac11-f8cefc68f8c4/download/university-wise-student-enrollment-by-province-in-2074-bs.csv")
    print(df_province.head())
    df_province.dropna() # removing missing values

    #Source 4
    print("Fetching data from Open Data Nepal for Degree level Wise student distribution across Universities")
    df_degree = pd.read_csv("https://opendatanepal.com/dataset/aaba8c3f-b4d3-4f1c-9ef2-32fddbeb0876/resource/115f055f-3d15-4ba8-8bb4-a76b4522acfd/download/university-wise-student-enrollment-of-higher-education-by-levels-in-2074-bs.csv")
    print(df_degree.head())
    df_degree.dropna() # removing missing values



    ############################Creating db files############################
    print("Creating Gender Data table")
    conn1 = sqlite3.connect('./data/gender_data.sqlite')
    df_gender.to_sql('gender', conn1, index=False, if_exists='replace')
    conn1.close()
    
    # print("Creating Gender Data table")
    # df_gender.to_sql("gender_data",'sqlite:///gender_data.sqlite', if_exists='replace',index=False)

    print("Creating university type Data table")
    conn2 = sqlite3.connect('./data/university_data.sqlite')
    df_university.to_sql('university', conn2, index=False, if_exists='replace')
    conn2.close()

    # print("Creating university type Data table")
    # df_university.to_sql("university_data",'sqlite:///university_data.sqlite',if_exists='replace')

    print("Creating Province Data table")
    conn3 = sqlite3.connect('./data/province_data.sqlite')
    df_province.to_sql('province', conn3, index=False, if_exists='replace')
    conn3.close()

    # print("Creating Province Data table")
    # df_province.to_sql("province_data",'sqlite:///province_data.sqlite',if_exists='replace')

    print("Creating Degree Level Data table")
    conn4 = sqlite3.connect('./data/degree_data.sqlite')
    df_degree.to_sql('degree', conn4, index=False, if_exists='replace')
    conn4.close()

    # print("Creating Degree Level Data table")
    # df_degree.to_sql("degree_data",'sqlite:///degree_data.sqlite',if_exists='replace')

 