def format_timestamp(seconds):
    milliseconds = int(seconds * 1000)

    hours = milliseconds // 3_600_000
    milliseconds %= 3_600_000

    minutes = milliseconds // 60_000
    milliseconds %= 60_000

    seconds = milliseconds // 1_000
    milliseconds %= 1_000

    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


def generate_captions(words, max_words=3, max_duration=1.5, pause_threshold=0.3):
    captions = []
    current_caption = []

    for word in words:

        if not current_caption:
            current_caption.append(word)
            continue

        previous_word = current_caption[-1]

        gap = word["start"] - previous_word["end"]

        current_start = current_caption[0]["start"]
        current_duration = word["end"] - current_start

        ends_with_punctuation = previous_word["word"].endswith(
            (".", "!", "?", ",")
        )

        should_split = (
            len(current_caption) >= max_words
            or gap >= pause_threshold
            or current_duration > max_duration
            or ends_with_punctuation
        )

        if should_split:
            captions.append(current_caption)
            current_caption = [word]
        else:
            current_caption.append(word)

    if current_caption:
        captions.append(current_caption)

    return captions

def generate_srt(words, output_path="subtitles.srt"):
    captions = generate_captions(words)

    with open(output_path, "w", encoding="utf-8") as subtitle_file:

        for index, caption in enumerate(captions, start=1):

            start = caption[0]["start"]
            end = caption[-1]["end"]

            text = " ".join(
                word["word"] for word in caption
            )

            subtitle_file.write(f"{index}\n")
            subtitle_file.write(
                f"{format_timestamp(start)} --> "
                f"{format_timestamp(end)}\n"
            )
            subtitle_file.write(f"{text}\n\n")