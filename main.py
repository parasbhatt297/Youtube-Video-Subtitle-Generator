from transcribe import transcribe_audio
from subtitle_generator import generate_srt


audio_file = "audio.m4a"

words = transcribe_audio(audio_file)

generate_srt(
    words,
    output_path="subtitles.srt",
    words_per_caption=2
)

print("Subtitles generated successfully!")