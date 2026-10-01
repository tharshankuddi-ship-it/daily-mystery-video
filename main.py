import os
import subprocess

os.makedirs("output", exist_ok=True)

scenes = [
    "Something was hidden beneath the forest.",
    "The explorer discovered an old stone door.",
    "A strange sound came from inside.",
    "The door slowly opened.",
    "But something was already waiting there."
]

for i, text in enumerate(scenes, 1):
    subprocess.run([
        "ffmpeg", "-y",
        "-f", "lavfi",
        "-i", "color=c=black:s=1080x1920:d=12",
        "-vf",
        f"drawtext=text='{text}':fontcolor=white:fontsize=55:x=(w-text_w)/2:y=(h-text_h)/2",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        f"output/scene{i}.mp4"
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
