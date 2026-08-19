from faster_whisper import WhisperModel


def transcribe_audio(audio_path):
    model = WhisperModel(
        "small",
        device="cpu",
        compute_type="int8"
    )

    segments, info = model.transcribe(
        audio_path,
        language="en",
        beam_size=5,
        word_timestamps=True
    )

    words = []

    for segment in segments:
        if segment.words:
            for word in segment.words:
                words.append({
                    "word": word.word.strip(),
                    "start": word.start,
                    "end": word.end
                })

    return words