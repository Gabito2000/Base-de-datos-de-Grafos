import subprocess
import os


def load_database():
    """Load all database dumps into Neo4j"""
    print("\n=== Loading database dumps ===")
    try:
        # Create data directory if it doesn't exist
        data_dir = os.path.abspath("data")
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            print(f"Created data directory at: {data_dir}")
            print("Please place your .db.dump files in the data directory and run the script again.")
            return
            
        # Get all .dump files in data directory
        dump_files = [f for f in os.listdir(data_dir) if f.endswith(".db.dump")]
        
        if not dump_files:
            print("No .db.dump files found in the data directory.")
            print("Please add your database dump files and try again.")
            return
            
        print("Stopping container temporarily...")
        subprocess.run(
            "docker stop neo4j_container",
            check=True,
            shell=True
        )
        
        # Get all .dump files in data directory
        data_dir = os.path.abspath("data")
        dump_files = [f for f in os.listdir(data_dir) if f.endswith(".db.dump")]
        
        for dump_file in dump_files:
            db_name = dump_file.split(".db.dump")[0]
            print(f"\nLoading database: {db_name}")
            
            # Convert Windows paths to Docker-compatible format
            neo4j_data_path = os.path.join(os.environ["USERPROFILE"], "neo4j", "data").replace("\\", "/")
            import_data_path = data_dir.replace("\\", "/")
            
            # Create neo4j import directory if it doesn't exist
            neo4j_import_dir = os.path.join(os.environ["USERPROFILE"], "neo4j", "data", "import")
            if not os.path.exists(neo4j_import_dir):
                os.makedirs(neo4j_import_dir)
                print(f"Created Neo4j import directory at: {neo4j_import_dir}")

            # copy dump file to neo4j/import directory
            subprocess.run(
                f'xcopy "{os.path.join(import_data_path, dump_file)}" "{neo4j_import_dir}" /Y',
                check=True,
                shell=True
            )
            
            # Load database dump into Neo4j
            docker_command = (
                f'docker run --rm '
                f'--volume="{neo4j_data_path}:/data" '
                f'neo4j:community '
                f'neo4j-admin database load '
                f'{db_name} '
                f'--from-path=/data/import/{dump_file} '
                f'--overwrite-destination=true'
            )
            
            subprocess.run(
                docker_command,
                check=True,
                shell=True
            )
        
        print("Restarting container...")
        subprocess.run(
            "docker start neo4j_container",
            check=True,
            shell=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error loading database: {e}")
        raise


if __name__ == "__main__":
    load_database()
    print("\n=== Data load completed successfully ===")
    print("Access Neo4j at: http://localhost:7474")