from faster_whisper import WhisperModel


def format_timestamp(seconds):
    milliseconds = int(seconds * 1000)

    hours = milliseconds // 3_600_000
    milliseconds %= 3_600_000

    minutes = milliseconds // 60_000
    milliseconds %= 60_000

    seconds = milliseconds // 1_000
    milliseconds %= 1_000

    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

segments, info = model.transcribe(
    "audio.m4a",
    language="en",
    beam_size=5
)

with open("subtitles.srt", "w", encoding="utf-8") as subtitle_file:

    for index, segment in enumerate(segments, start=1):
        start = format_timestamp(segment.start)
        end = format_timestamp(segment.end)

        subtitle_file.write(f"{index}\n")
        subtitle_file.write(f"{start} --> {end}\n")
        subtitle_file.write(f"{segment.text.strip()}\n\n")

print("Subtitles generated successfully!")