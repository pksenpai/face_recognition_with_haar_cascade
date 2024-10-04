import cv2
from imgbeddings import imgbeddings
from PIL import Image

import fetcher
from database import Database
import os


def image_to_list(image, imgbd):
    pil_image = Image.fromarray(image) # if it was BGR use cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    embedded_img = imgbd.to_embeddings(pil_image)
    return embedded_img[0].tolist()

def init():
    """ Learn Faces """
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    """ Camera Settings """
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 500) # 1920, 1080, 720, ..
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500) # 1920, 1080, 720, ..

    if not cap.isOpened():
        raise IOError('Cannot open the camera!')
    
    return cap, face_cascade

def detect(method:str, name:str = 'Unknown'):
    """
    Face Detection with haar alg
    """
    
    imgbd = imgbeddings() # imgbeddings
    database = Database() # database
    cap, face_cascade = init() # cap & ML model
    with database as db:
        while True:
            ret, frame =cap.read()
            if not ret:
                break
            
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1,
                                                minNeighbors=5, minSize=(30, 30))
            
            for (x, y, h, w) in faces:
                # y -= 50
                # x -= 20
                # xw, yh = x+w+40, y+h+70
                
                xw, yh = x+w, y+h
                
                ''' Enhance(CLAHE) & Denoise(Gaussian) the image '''
                denoised_gray_frame = cv2.GaussianBlur(gray_frame , (3,3) , 0)
                clahe = cv2.createCLAHE(clipLimit=200, tileGridSize=(1,1))
                enhanced_gray_frame = clahe.apply(denoised_gray_frame)
                
                ''' Crop the Detected faces '''
                face = enhanced_gray_frame[y: yh, x: xw]
                resized_img = cv2.resize(face, (150, 150))
                embedded_img = image_to_list(face, imgbd)
                
                """ METHODS """
                if method == 'crop':
                    cv2.rectangle(frame, (x, y), (xw, yh), (255, 0, 0), 2)
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('If the blue square is only around your face, press C')
                     
                    if (cv2.waitKey(1) & 0xFF==ord('c')): # taking the picture!
                        _, face_path = fetcher.face_saver(face, name)

                        done = db.insert(face_path, name)

                        cap.release()
                        cv2.destroyAllWindows()
                        if done:
                            return name
                        return

                elif method == 'check':
                    authenticated = False
                    name = 'Unknown'
                    authenticated, name = fetcher.similar_face_searcher(resized_img)
                    
                    if authenticated:
                        cv2.rectangle(frame, (x, y), (xw, yh), (0, 255, 0), 2)
                        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                    else:
                        cv2.rectangle(frame, (x, y), (xw, yh), (0, 0, 255), 2)
                        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            
            cv2.imshow('Detected faces', frame)
            if (cv2.waitKey(1) & 0xFF==ord('q')):
                break

    cap.release()
    cv2.destroyAllWindows()
    
