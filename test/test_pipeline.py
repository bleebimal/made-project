import sys
import unittest
import pathlib as pl
import pandas as pd
import os


class TestCase(unittest.TestCase):
    def test_SQLiteFileExists():
        directory_path = os.getcwd()
        assert os.path.exists(os.path.dirname(directory_path)+"\project\data\degree_data.sqlite")
        assert os.path.exists(os.path.dirname(directory_path)+"\project\data\university_data.sqlite")
        assert os.path.exists(os.path.dirname(directory_path)+"\project\data\province_data.sqlite")
        assert os.path.exists(os.path.dirname(directory_path)+"\project\data\degree_data.sqlite")
         

if __name__ == "__main__":
    unittest.main()