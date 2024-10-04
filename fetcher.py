import os
import cv2
import numpy as np


""" saving... """
def face_saver(face_img, face_name, folder_path: str = "faces"):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    
    face_img = cv2.resize(face_img, (150, 150))

    faces_path = os.path.join(folder_path, face_name + '.jpg')
    cv2.imwrite(faces_path, face_img)
    
    return True, faces_path

""" searching... """
def all_face_extractor(folder_path: str = "faces"):
    img_lst = []
    filename_lst = []
    for filename in os.listdir(folder_path):
        if not filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            continue

        img_path = os.path.join(folder_path, filename)

        img_lst.append(cv2.imread(img_path, cv2.IMREAD_GRAYSCALE))
        filename_lst.append(filename)

    return img_lst, filename_lst

def euclidean_distance_calculator(auth_face, new_face):
    distance = np.linalg.norm(auth_face - new_face)
    return distance

def similar_face_searcher(new_face, confidence: int = 30000):
    # Warning: Confidence is different in different cameras & distance between face & camera,
    #  Please adjust the confidence according to your own conditions!!!
    
    authenticated_faces_id, authenticated_faces_name = all_face_extractor()
    distance_lst = []
    for auth_face in authenticated_faces_id:
        distance = euclidean_distance_calculator(auth_face, new_face)
        print('--------->>>', distance)
        distance_lst.append(distance)

    best_similarity = min(distance_lst)

    if best_similarity < confidence:
        return True, authenticated_faces_name[distance_lst.index(best_similarity)].split('.')[0]
    return False, 'Unknown'
