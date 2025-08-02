import pandas as pd

def transform_data(df):
    # Convert signup_date to datetime
    df['signup_date'] = pd.to_datetime(df['signup_date'])

    # Example transformation: Add a "member_years" column
    df['member_years'] = 2025 - df['signup_date'].dt.year

    return df
