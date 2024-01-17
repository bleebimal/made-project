import os
from project.pipeline import pipeline

def test_gender_data():
    pipeline()
    # Check if the gender_data.sqlite database is created or not
    assert os.path.isfile('./data/gender_data.sqlite')

def test_university_data():
    pipeline()
    # Check if the university_data.sqlite database is created or not
    assert os.path.isfile('./data/university_data.sqlite')

def test_province_data():
    pipeline()
    # Check if the province_data.sqlite database is created or not
    assert os.path.isfile('./data/province_data.sqlite')

def test_degree_data():
    pipeline()
    # Check if the degree_data.sqlite database is created or not
    assert os.path.isfile('./data/degree_data.sqlite')

