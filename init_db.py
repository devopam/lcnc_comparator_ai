from utils.database import init_db
import sys

def main():
    try:
        print("Initializing database...")
        init_db()
        print("Database initialization completed successfully!")
        return 0
    except Exception as e:
        print(f"Error during database initialization: {str(e)}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())