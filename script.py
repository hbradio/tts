import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

with open('output/output_7_manual.txt') as f:
    text = f.read()

tts.tts_to_file(text=text, speaker="Aaron Dreschner", language="en", file_path="chapter7_new.wav")