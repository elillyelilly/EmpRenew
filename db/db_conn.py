from os import getenv
import pymssql

def get_connection():
    conn = pymssql.connect(
	    'spsrv55', 'sa', 'Sopure@5270', 'Man-Globe')
    return conn

def get_query(query_file_path):
    with open(query_file_path, 'r', encoding='utf-8') as f:
        query = f.read()
    return query

def run_query(query_file_path):
    with get_connection() as connection:
        with connection.cursor() as cur:
            query = get_query(query_file_path)
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                print(row)

if __name__ == "__main__":
    query_file_path = 'sql/keiykau_joho.sql'
    run_query(query_file_path)
    
