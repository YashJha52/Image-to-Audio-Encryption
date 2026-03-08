import cv2
import pickle
from backend.audio_conversion import audio_to_image


def reconstruct_image(audio_array):
    b, g, r, shape = pickle.load(open("output/color.pkl", "rb"))
    gray_image = audio_to_image(audio_array, shape)
    cv2.imwrite("output/reconstructed_gray.png", gray_image)
    colored = cv2.merge((b, g, r))
    cv2.imwrite("output/final_image.png", colored)