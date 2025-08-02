# etl/run_etl.py

from extract import extract_csv
from transform import transform_data
from load import load_to_db

def run_etl():
    df = extract_csv('../data/sample_data.csv')
    df = transform_data(df)
    load_to_db(df)

if __name__ == '__main__':
    run_etl()
