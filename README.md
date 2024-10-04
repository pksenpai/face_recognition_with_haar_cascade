- Create a .env file and then copy the following text in it and enter your database information:
```
DB_NAME = face_recognition
DB_USER = postgres
DB_PASS = your_password
DB_HOST = localhost
DB_PORT = 5432
```

- Install the required libraries using the requirements.txt file:
pip install -r requirements.txt

- Run create_database.sql script to create the table and database.(i used Postgresql, if you use another database, change the query file)

- Confidence is different in different cameras & distance between face & camera, Please adjust the confidence according to your own conditions!!!
```
# fetcher.py
def similar_face_searcher(..., confidence: int = '>adjust here<'): ...
```

- Run main.py

- To register, a blue square must appear around your face, then look directly at the camera, & then press the C button to register!

