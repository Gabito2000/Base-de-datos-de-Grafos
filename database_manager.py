import sqlite3
import csv
import os
from typing import List, Any, Optional

class DatabaseManager:
    def __init__(self, db_name: str):
        """Initialize database connection."""
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self) -> None:
        """Establish database connection."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print(f"Successfully connected to {self.db_name}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def close(self) -> None:
        """Close database connection."""
        if self.conn:
            self.conn.close()
            print("Database connection closed")

    def load_csv(self, csv_file: str, table_name: str) -> None:
        """Load data from CSV file into SQLite table."""
        try:
            if not os.path.exists(csv_file):
                print(f"Error: CSV file {csv_file} not found")
                return

            with open(csv_file, 'r') as file:
                csv_reader = csv.reader(file)
                headers = next(csv_reader)  # Get column names from first row
                
                # Create table with columns from CSV headers
                columns = [f"\"{header}\" TEXT" for header in headers]
                create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
                self.cursor.execute(create_table_sql)

                # Insert data
                insert_sql = f"INSERT INTO {table_name} VALUES ({','.join(['?' for _ in headers])})"
                self.cursor.executemany(insert_sql, csv_reader)
                self.conn.commit()
                print(f"Successfully loaded data from {csv_file} into {table_name}")

        except (sqlite3.Error, csv.Error) as e:
            print(f"Error loading CSV data: {e}")

    def execute_query(self, query: str) -> Optional[List[Any]]:
        """Execute SQL query and return results."""
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            if query.strip().upper().startswith('SELECT'):
                # Get column names for SELECT queries
                columns = [description[0] for description in self.cursor.description]
                print("\nColumns:", columns)
                print("\nResults:")
                for row in results:
                    print(row)
            else:
                self.conn.commit()
                print("Query executed successfully")
            return results
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return None

def main():
    # Example usage
    db = DatabaseManager('example.db')
    db.connect()
    
    # Example: Load CSV file
    # db.load_csv('data.csv', 'my_table')
    
    # Example: Execute query
    # db.execute_query('SELECT * FROM my_table LIMIT 5')
    
    db.close()

if __name__ == '__main__':
    main()