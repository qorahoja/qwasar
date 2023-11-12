# Welcome to My Ds Babel
***

## Task
The task is to create two functions in Python that can convert data between a SQLite database and a CSV formatted string. 
The first function, sql_to_csv, retrieves data from a SQLite database and returns it in CSV format. 
The second function, csv_to_sql, takes CSV formatted data and inserts it into a SQLite database.

## Description
The problem was solved by leveraging the Python sqlite3 library, which provides an API for interacting with SQLite databases, 
and the pandas library, which offers powerful data manipulation capabilities including reading/writing data in various formats such as CSV and SQL.

## Installation
To use these functions, you will first need to install the necessary Python packages if you haven't already.

## Usage
Here is how you can use these functions in your Python scripts:

To convert SQL data to CSV format:
```
csv_content = sql_to_csv('my_database.db', 'my_table')
print(csv_content)
```

To insert CSV data into an SQL database:
```
csv_to_sql(csv_content, 'my_database.db', 'my_table')
```

### The Core Team
Temitope Flourish Oke <br>
Ivan Makhambetov

<span><i>Made at <a href="https://qwasar.io">Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt="Qwasar SV -- Software Engineering School's Logo" src="https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png" width="20px"></span>
