# Face Recognition with Classic ML Method (face haar cascade)
* faces haar cascades as dataset & K-Nearest neighbor algorithm for face detection.
* this is a classic & old method, so it's normal that it's not as accurate as deep learning methods!
* used imgbeddings for embedding features & a database for store data.(ex. postgresql)
* used euclidean formula for clac similarity and face recognition.
<img src="..." width="500" height="600">
-----
## Preparation
1- Create a `.env` file --> copy the following text & paste it then enter your database information:
```.env
# .env
DB_NAME = face_recognition
DB_USER = postgres
DB_PASS = your_password
DB_HOST = localhost
DB_PORT = 5432
```

2- Install the required libraries using the [`requirements.txt`] file:
```console
pip install -r requirements.txt
```

3- Run [`create_database.sql`] script to create the tables & database.
> [!WARNING]
> i used `Postgresql`, if you use another database, change the query file.

4- Confidence is different in different cameras & distance between face & camera, Please adjust the [`confidence`] according to your own conditions!!!
```python
# fetcher.py
def similar_face_searcher(..., confidence: int = '>adjust here<'): ...
```

5- Run [`main.py`].

6- To `register`, a blue square must appear around your face, then look directly at the camera, & then press the `C button` to register!

[`requirements.txt`]: https://github.com/pksenpai/face_recognition_with_haar_cascade/blob/main/requirements.txt
[`create_database.sql`]: https://github.com/pksenpai/face_recognition_with_haar_cascade/blob/main/create_database.sql 
[`confidence`]: https://github.com/pksenpai/face_recognition_with_haar_cascade/blob/4780338ef35f0ee2907dff4cd6ef815309a0cf71/fetcher.py#L37
[`main.py`]: https://github.com/pksenpai/face_recognition_with_haar_cascade/blob/main/main.py
