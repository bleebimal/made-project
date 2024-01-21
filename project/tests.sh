#Install required packages
pip install --upgrade pip
pip install -r ./project/requirements.txt

# Run testcase updates
pytest ./project/test/test_pipeline.py