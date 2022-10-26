class PingService:

    def __init__(self, database):
        self.database = database

    def ping(self):
        with self.database.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchall()
            
        return {'message': 'pong'}