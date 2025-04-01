from database_manager import DatabaseManager

def run_demo():
    # Initialize and connect to database
    db = DatabaseManager('example.db')
    db.connect()

    # Load data from CSV
    print("\n1. Loading data from CSV file...")
    db.load_csv('example.csv', 'people')

    # Execute some example queries
    print("\n2. Selecting all records:")
    db.execute_query('SELECT * FROM people')

    print("\n3. Selecting people older than 30:")
    db.execute_query('SELECT name, age FROM people WHERE age > 30')

    print("\n4. Counting people by city:")
    db.execute_query('SELECT city, COUNT(*) as count FROM people GROUP BY city')

    print("\n5. Finding average age:")
    db.execute_query('SELECT AVG(age) as avg_age FROM people')

    # Close the database connection
    db.close()

if __name__ == '__main__':
    run_demo()