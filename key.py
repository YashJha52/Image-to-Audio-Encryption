import pickle

with open("output/hash.pkl","rb") as f:
    key = pickle.load(f)

print("Hash Key:", key)