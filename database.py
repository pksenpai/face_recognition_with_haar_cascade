from decouple import config
import psycopg2
import logging
from time import sleep
from datetime import datetime as dt

# logging:
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s(%(asctime)s): %(name)s --> %(message)s"
)

class Database:
    def __init__(self):
        """ connect to database """
        self.__conn = None
        self._cur = None
        while self.__conn is None:
            
            try:
                self.__conn = psycopg2.connect(
                                database = config('DB_NAME', cast=str),
                                user     = config('DB_USER', cast=str),
                                password = config('DB_PASS', cast=str),
                                host     = config('DB_HOST', cast=str),
                                port     = config('DB_PORT', cast=str)
                            )

                logging.info("Database connected successfully!!!")
            except:
                logging.error("Database NOT connected successfully!!!")
                sleep(1)
                
    def __enter__(self) -> object:
        """ create & return cursor """
        self._cur = self.__conn.cursor()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """ commit query & disconnect from database """
        self.__conn.commit()
        self._cur.close()
        self.__conn.close()
        # check committing successfully:
        logging.error(exc_val) if exc_val else logging.info("Done!")
    
    def insert(self, face_path, name):
        print(face_path)

        self._cur.execute(
            """
            INSERT INTO faces (face_name, face_path)
            VALUES (%s, %s);
            """,
            (name, face_path)
        )

        return True

