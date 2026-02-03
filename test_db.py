import mysql.connector

def test_connection():
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'bimsara123',
        'database': 'student_analytics'
    }
    
    print(f"Attempting to connect to {config['host']} as {config['user']}...")
    try:
        conn = mysql.connector.connect(**config)
        print("✅ Connection successful!")
        
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("✅ Tables found:", tables)
        
        conn.close()
    except Exception as e:
        print("❌ Connection failed:")
        print(e)
        print("\nPossible fixes:")
        print("1. Ensure MySQL is running (XAMPP/WAMP).")
        print("2. Check if database 'student_analytics' exists.")
        print("3. Check password.")

if __name__ == "__main__":
    test_connection()
