import numpy as np
from scipy.io.wavfile import write
import os

def image_to_audio(gray):
    # ensure output folder exists
    if not os.path.exists("output"):
        os.makedirs("output")
    flat = gray.flatten()
    audio = flat / 255.0
    audio = audio * 2 - 1
    write("output/audio.wav", 44100, audio.astype(np.float32))
    return audio


def audio_to_image(audio_array, shape):
    pixels = ((audio_array + 1) / 2 * 255).astype(np.uint8)
    image = pixels.reshape(shape)
    return image