import sqlite3
import os

def create_and_populate_db(input_file, db_name):
    # Create database connection
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS edges (
            source INTEGER,
            target INTEGER
        )
    ''')

    # Read the TSV file and insert data
    with open(input_file, 'r') as f:
        for line in f:
            source, target = map(int, line.strip().split('\t'))
            cursor.execute('INSERT INTO edges (source, target) VALUES (?, ?)', (source, target))

    # Create indices for better query performance
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_source ON edges(source)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_target ON edges(target)')

    # Commit and close
    conn.commit()
    conn.close()

def main():
    base_path = r'c:\Users\gabri\OneDrive\Escritorio\Facultad\Base de datos de Grafos\Clase 1 - Introducción'
    
    # Process each file
    files = ['webgraph1.txt', 'webgraph2.txt', 'webgraph3.txt']
    
    for file in files:
        input_file = os.path.join(base_path, file)
        db_name = os.path.join(base_path, f'{os.path.splitext(file)[0]}.db')
        
        print(f'Processing {file}...')
        create_and_populate_db(input_file, db_name)
        print(f'Created database: {db_name}')

if __name__ == '__main__':
    main()