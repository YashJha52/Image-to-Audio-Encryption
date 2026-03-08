import hashlib
import pickle
import os


def generate_hash():

    audio_path = "output/audio.wav"

    if not os.path.exists(audio_path):
        raise FileNotFoundError(
            "audio.wav not found. Image must be converted to audio first."
        )

    with open(audio_path, "rb") as f:
        data = f.read()

    hash_key = hashlib.sha256(data).hexdigest()

    with open("output/hash.pkl", "wb") as f:
        pickle.dump(hash_key, f)

    print("\nGenerated Hash Key:")
    print(hash_key)

    return hash_key


def verify_hash(audio_path, user_key):

    with open(audio_path, "rb") as f:
        data = f.read()

    new_hash = hashlib.sha256(data).hexdigest()

    print("\nCalculated Hash:", new_hash)
    print("User Key:", user_key)

    return new_hash == user_key