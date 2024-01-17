import os
from pipeline import pipeline


def test_gender_data():
    pipeline()
    # Check if the asia_covid.sqlite database is created or not
    assert os.path.isfile('./data/gender_data.sqlite')

def test_university_data():
    pipeline()
    # Check if the europe_covid.sqlite database is created or not
    assert os.path.isfile('./data/university_data.sqlite')

def test_province_data():
    pipeline()
    # Check if the europe_covid.sqlite database is created or not
    assert os.path.isfile('./data/province_data.sqlite')

def test_degree_data():
    pipeline()
    # Check if the europe_covid.sqlite database is created or not
    assert os.path.isfile('./data/degree_data.sqlite')