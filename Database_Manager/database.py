import pymysql

class DBManager:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 3306
        self.user = "root"
        self.password = "Tintiniacrylic0405!"
        self.database = "hpacdb"
    
    def connect_DB(self):
        self.cable = pymysql.connect(
            host=self.host,
            user=self.user,
            port=self.port,
            password=self.password,
            database=self.database
        )
        self.kuryente = self.cable.cursor()