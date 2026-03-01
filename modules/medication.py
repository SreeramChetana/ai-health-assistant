from modules.database import get_connection

class MedicationTracker:

    def add_medication(self, name, time):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO medications (name, time) VALUES (?, ?)",
            (name, time)
        )

        conn.commit()
        conn.close()

    def get_medications(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT name, time FROM medications")
        data = cursor.fetchall()

        conn.close()
        return data