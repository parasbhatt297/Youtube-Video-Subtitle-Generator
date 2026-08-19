def format_timestamp(seconds):
    milliseconds = int(seconds * 1000)

    hours = milliseconds // 3_600_000
    milliseconds %= 3_600_000

    minutes = milliseconds // 60_000
    milliseconds %= 60_000

    seconds = milliseconds // 1_000
    milliseconds %= 1_000

    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


def generate_srt(words, output_path="subtitles.srt", words_per_caption=2):
    with open(output_path, "w", encoding="utf-8") as subtitle_file:

        subtitle_number = 1

        for i in range(0, len(words), words_per_caption):
            caption_words = words[i:i + words_per_caption]

            start = caption_words[0]["start"]
            end = caption_words[-1]["end"]

            text = " ".join(
                word["word"] for word in caption_words
            )

            subtitle_file.write(f"{subtitle_number}\n")
            subtitle_file.write(
                f"{format_timestamp(start)} --> "
                f"{format_timestamp(end)}\n"
            )
            subtitle_file.write(f"{text}\n\n")

            subtitle_number += 1