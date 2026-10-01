
import os
import subprocess

os.makedirs("output", exist_ok=True)

scenes = [
    "Something was hidden beneath the forest.",
    "An explorer discovered an ancient stone door.",
    "A strange sound came from inside.",
    "The door slowly opened.",
    "But something was waiting in the darkness."
]

for i in range(1, 6):
    image = f"images/scene{i}.jpg"
    output = f"output/scene{i}.mp4"

    if not os.path.exists(image):
        raise FileNotFoundError(f"Missing image: {image}")

    subprocess.run([
        "ffmpeg", "-y",
        "-loop", "1",
        "-i", image,
        "-t", "12",
        "-vf",
        "scale=1080:1920:force_original_aspect_ratio=increase,"
        "crop=1080:1920,"
        "zoompan=z='min(zoom+0.0005,1.12)':"
        "d=360:s=1080x1920:fps=30,"
        f"drawtext=text='{scenes[i-1]}':"
        "fontcolor=white:fontsize=48:"
        "x=(w-text_w)/2:y=h-300:"
        "box=1:boxcolor=black@0.55:boxborderw=20",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output
    ], check=True)

with open("output/list.txt", "w") as f:
    for i in range(1, 6):
        f.write(f"file 'scene{i}.mp4'\n")

subprocess.run([
    "ffmpeg", "-y",
    "-f", "concat", "-safe", "0",
    "-i", "output/list.txt",
    "-c", "copy",
    "output/daily_mystery.mp4"
], check=True)
