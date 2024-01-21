#Install required packages
pip install --upgrade pip
pip install -r ./project/requirements.txt

# Run testcase updates
pytest ./project/tests/test_pipeline.py