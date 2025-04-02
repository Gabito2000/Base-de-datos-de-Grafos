import sqlite3

def connect_to_db(db_number):
    """Connect to a specific database by number (1, 2, or 3)"""
    base_path = r'c:\Users\gabri\OneDrive\Escritorio\Facultad\Base de datos de Grafos\Clase 1 - Introducción'
    db_path = f"{base_path}\\webgraph{db_number}.db"
    return sqlite3.connect(db_path)

def query_graph(db_number, query):
    """Execute a query on the specified database and return results"""
    try:
        conn = connect_to_db(db_number)
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Example queries
    queries = {
        "Total edges": "SELECT COUNT(*) FROM edges",
        "Most connected nodes": """
            SELECT source, COUNT(*) as connections 
            FROM edges 
            GROUP BY source 
            ORDER BY connections DESC 
            LIMIT 5
        """
    }

    # Query each database
    for db_num in [1, 2, 3]:
        print(f"\nAnalyzing webgraph{db_num}.db:")
        for description, query in queries.items():
            results = query_graph(db_num, query)
            print(f"\n{description}:")
            if results:  # Check if results is not None before iterating
                for row in results:
                    print(row)