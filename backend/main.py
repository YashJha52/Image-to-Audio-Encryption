from backend.image_processing import convert_to_gray, save_color_info
from backend.audio_conversion import image_to_audio
from backend.encryption import generate_hash, verify_hash
from backend.reconstruction import reconstruct_image
from scipy.io.wavfile import read


def main():

    img, gray = convert_to_gray("data/input.jpg")

    save_color_info(img, gray.shape)

    audio = image_to_audio(gray)

    key = generate_hash()

    print("\nGenerated Hash:", key)

    user_key = input("\nEnter hash key to reconstruct image: ")

    if verify_hash("output/audio.wav", user_key):

        rate, audio = read("output/audio.wav")

        reconstruct_image(audio)

        print("Image reconstructed")

    else:

        print("Invalid key")


if __name__ == "__main__":
    main()