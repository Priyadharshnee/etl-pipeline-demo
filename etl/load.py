import sqlite3
def load_to_db(df, db_path='database/etl_output.db'):
    import os
    os.makedirs('database', exist_ok=True)

    print("Data being loaded to DB:")
    print(df.head())  # print first 5 rows

    conn = sqlite3.connect(db_path)
    df.to_sql('users', conn, if_exists='replace', index=False)
    conn.close()
