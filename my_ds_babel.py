import csv
import sqlite3
import pandas as pd
from io import StringIO


def sql_to_csv(database, table_name):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")

    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    output = StringIO()

    df.to_csv(output, index=False, line_terminator='\n')
    csv_str = output.getvalue()

    conn.close()

    return csv_str.rstrip('\n')


def csv_to_sql(csv_content, database, table_name):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    table_exists = cursor.fetchone()

    if not table_exists:
        cursor.execute(f"CREATE TABLE {table_name} ('Volcano Name', 'Country', 'Type', 'Latitude (dd)', 'Longitude (dd)', 'Elevation (m)')")

    is_first_line = True
    for row in csv_content.readlines():
        
        if is_first_line:
            is_first_line = False
            continue

        cursor.execute(
                f"INSERT INTO {table_name} ('Volcano Name', 'Country', 'Type', 'Latitude (dd)', 'Longitude (dd)', 'Elevation (m)') VALUES (?, ?, ?, ?, ?, ?)",
                row.strip().split(',')
            )

    conn.commit()
    conn.close()


