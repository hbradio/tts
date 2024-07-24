https://github.com/coqui-ai/TTS

```sh
conda create --name coqui python=3.9

conda activate coqui
pip install git+https://github.com/coqui-ai/TTS

tts --list_speaker_idxs --model_name "tts_models/multilingual/multi-dataset/xtts_v2" 
tts --text "Text for TTS" --model_name "tts_models/multilingual/multi-dataset/xtts_v2" --out_path ./s3.wav --speaker_idx 'Aaron Dreschner' --language_idx 'en'

cat adler2.txt | xargs -0 -I {} tts --text "{}" --model_name "tts_models/multilingual/multi-dataset/xtts_v2" --out_path ./s3.wav --speaker_idx 'Aaron Dreschner' --language_idx 'en'

tts --text "$(cat path_to_text_file.txt)" --model_name "tts_models/multilingual/multi-dataset/xtts_v2" --out_path ./s3.wav --speaker_idx 'Aaron Dreschner' --language_idx 'en'


pip install autocorrect==2.6.1



```