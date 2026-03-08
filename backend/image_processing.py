import cv2
import pickle

def convert_to_gray(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("output/gray.png", gray)
    return img, gray

def save_color_info(img, shape):
    b, g, r = cv2.split(img)
    pickle.dump((b, g, r, shape), open("output/color.pkl", "wb"))