
# Image to Audio Hash Security System 🔐🎵🖼️

This project converts an **image into audio**, generates a **secure SHA-256 hash**, and allows the image to be reconstructed only if the **correct hash key** is provided.

It demonstrates concepts from **image processing, audio encoding, and cryptographic hashing for integrity verification**.


# 📌 Features

* Convert image → grayscale → audio waveform
* Store audio as **WAV file**
* Generate **SHA-256 hash key** for security
* Store color information using **PKL**
* Reconstruct the original image from audio
* Verify integrity using the **hash key**
* GUI interface built with **Tkinter**


# 🧠 How It Works

### 1️⃣ Image Conversion

```
Image
 ↓
Grayscale Conversion
 ↓
Pixel Flattening
 ↓
Normalization
 ↓
Audio Signal
 ↓
audio.wav
```


### 2️⃣ Hash Generation

The generated audio file is hashed using **SHA-256**:

```
audio.wav
   ↓
SHA256 Hash
   ↓
Hash Key
```

Example hash:

```
9c3f0fbb8c1e0c0c3c4a2f8e9d3c5f1b...
```

This key must be saved to reconstruct the image.


### 3️⃣ Reconstruction

To reconstruct the image the user must provide:

```
audio.wav
color.pkl
hash key
```

Process:

```
Verify hash
      ↓
Decode audio → pixels
      ↓
Reconstruct grayscale image
      ↓
Merge color channels
      ↓
Final image
```


# 📁 Project Structure

```
project/
│
├── backend/
│   ├── image_processing.py
│   ├── audio_conversion.py
│   ├── encryption.py
│   └── reconstruction.py
│
├── output/
│
├── ui.py
├── main.py
├── run.sh
└── README.md
```

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/image-audio-hash-system.git
cd image-audio-hash-system
```

Create virtual environment (optional):

```
python -m venv ml
source ml/bin/activate
```

Install dependencies:

```
pip install numpy opencv-python scipy
```


# ▶️ Running the Project

### Run GUI version

```
python ui.py
```

### Run terminal version

```
python main.py
```

# 🖥️ Application Workflow

### Convert Image

1. Select image
2. Convert to audio
3. Generate hash key
4. Save hash key

Generated files:

```
output/
│
├── audio.wav
├── gray.png
├── color.pkl
├── hash.pkl
```


### Reconstruct Image

User must provide:

```
audio.wav
color.pkl
hash key
```

If the hash matches, the system reconstructs the image.


# 🔐 Security Concept

The system uses **SHA-256 hashing** to ensure **data integrity**.

If the audio file is modified even slightly:

```
Hash mismatch
Reconstruction denied
```

This demonstrates **tamper detection using cryptographic hashes**.

# 🛠 Technologies Used

* Python
* OpenCV
* NumPy
* SciPy
* Tkinter
* SHA-256 Hashing

# 🎯 Applications

* Secure image transmission
* Digital watermarking
* Data integrity verification
* Multimedia encryption research
* Educational cryptography demonstrations

# 👨‍💻 Author

**Yash Jha**


# 📜 License

This project is open source and available under the **MIT License**.
