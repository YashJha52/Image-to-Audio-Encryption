import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os
from scipy.io.wavfile import read

from backend.image_processing import convert_to_gray, save_color_info
from backend.audio_conversion import image_to_audio
from backend.encryption import generate_hash, verify_hash
from backend.reconstruction import reconstruct_image


selected_image_path = None


def select_image():

    global selected_image_path

    selected_image_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
    )

    if selected_image_path:
        status_label.config(text="Status: Image Selected")


def convert_process():

    if not selected_image_path:
        messagebox.showerror("Error", "Select an image first")
        return

    try:

        img, gray = convert_to_gray(selected_image_path)

        save_color_info(img, gray.shape)

        audio = image_to_audio(gray)

        key = generate_hash()

        print("\nGenerated Hash Key:")
        print(key)

        messagebox.showinfo("Hash Key", f"Save this key:\n\n{key}")

        status_label.config(text="Status: Audio + Hash Generated")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def reconstruct_process():

    try:

        audio_path = filedialog.askopenfilename(
            title="Select Audio File",
            filetypes=[("WAV files", "*.wav")]
        )

        pkl_path = filedialog.askopenfilename(
            title="Select PKL File",
            filetypes=[("PKL files", "*.pkl")]
        )

        key = simpledialog.askstring("Hash Key", "Enter Hash Key")

        if not audio_path or not pkl_path or not key:
            messagebox.showerror("Error", "Missing inputs")
            return

        if verify_hash(audio_path, key):

            rate, audio = read(audio_path)

            os.replace(pkl_path, "output/color.pkl")

            reconstruct_image(audio)

            messagebox.showinfo("Success", "Image Reconstructed")

            status_label.config(text="Status: Reconstruction Complete")

        else:

            messagebox.showerror("Error", "Invalid Key")

    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()

root.title("Image → Audio → Hash System")

root.geometry("500x420")

root.configure(bg="#1e1e1e")


title = tk.Label(
    root,
    text="Image to Audio Hash Security System",
    font=("Helvetica", 16, "bold"),
    bg="#1e1e1e",
    fg="white"
)

title.pack(pady=30)


button_style = {
    "font": ("Helvetica", 12),
    "width": 25,
    "height": 2,
    "bd": 0
}


select_btn = tk.Button(
    root,
    text="Select Image",
    command=select_image,
    bg="#4CAF50",
    fg="white",
    **button_style
)

select_btn.pack(pady=10)


convert_btn = tk.Button(
    root,
    text="Convert Image → Audio + Hash",
    command=convert_process,
    bg="#2196F3",
    fg="white",
    **button_style
)

convert_btn.pack(pady=10)


reconstruct_btn = tk.Button(
    root,
    text="Reconstruct Image",
    command=reconstruct_process,
    bg="#f44336",
    fg="white",
    **button_style
)

reconstruct_btn.pack(pady=10)


status_label = tk.Label(
    root,
    text="Status: Waiting",
    font=("Helvetica", 11),
    bg="#1e1e1e",
    fg="lightgray"
)

status_label.pack(pady=40)


root.mainloop()