import mysql.connector
import hashlib
import streamlit as st

class AuthModel:
    def __init__(self):
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'bimsara123',
            'database': 'student_analytics'
        }

    def _get_connection(self):
        try:
            conn = mysql.connector.connect(**self.db_config)
            return conn
        except mysql.connector.Error as err:
            st.error(f"Database Error: {err}")
            return None

    def _hash_password(self, password):
        # Using simple SHA256 for demonstration. 
        # In production, use bcrypt or argon2.
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self, username, password):
        conn = self._get_connection()
        if not conn:
            return None

        cursor = conn.cursor(dictionary=True)
        hashed_pw = self._hash_password(password)
        
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        try:
            cursor.execute(query, (username, hashed_pw))
            user = cursor.fetchone()
            return user
        except mysql.connector.Error as err:
            st.error(f"Login failed: {err}")
            return None
        finally:
            cursor.close()
            conn.close()

    def register(self, username, email, password):
        conn = self._get_connection()
        if not conn:
            return False

        cursor = conn.cursor()
        hashed_pw = self._hash_password(password)

        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        try:
            cursor.execute(query, (username, email, hashed_pw))
            conn.commit()
            return True
        except mysql.connector.Error as err:
            if err.errno == 1062: # Duplicate entry
                st.warning("Username or Email already exists.")
            else:
                st.error(f"Registration failed: {err}")
            return False
        finally:
            cursor.close()
            conn.close()
