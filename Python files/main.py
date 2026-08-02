from youtube_music import YouTubeMusic
from lrclib import LRCLyrics
from lrc_parser import LRCParser
from lyric_sync import LyricSync
from serial_comm import SerialComm

import time
import os
import re

def format_time(time_string):

    match = re.search(
        r"(\d+) Minutes? (\d+) Seconds? of (\d+) Minutes? (\d+) Seconds?",
        time_string
    )

    if match:

        cur_min = int(match.group(1))
        cur_sec = int(match.group(2))

        total_min = int(match.group(3))
        total_sec = int(match.group(4))


        return (
            f"{cur_min}:{cur_sec:02d} / "
            f"{total_min}:{total_sec:02d}"
        )

    return time_string

yt = YouTubeMusic()

lr = LRCLyrics()

parser = LRCParser()

sync = LyricSync()

esp = SerialComm("COM3",115200)

old_song = ""

lyrics = []


while True:

    title, artist, current_time = yt.get_song()


    if title is None:
        time.sleep(1)
        continue



    # New song detected

    if title != old_song:

        print("\n======================")
        print("Song:", title)
        print("Artist:", artist)
        print("======================")

        print("Loading synced lyrics...")


        lrc = lr.get_synced_lyrics(
            title,
            artist
        )


        if lrc:

            lyrics = parser.parse(lrc)

            print(
                "Lyrics loaded:",
                len(lyrics),
                "lines"
            )


        else:

            lyrics = []

            print("No synced lyrics found")


        old_song = title



    # Convert YouTube Music time
    # Example:
    # "3 Minutes 27 Seconds of 6 Minutes 29 Seconds"

    match = re.search(
        r"(\d+) Minutes? (\d+) Seconds?",
        current_time
    )


    if match:

        minutes = int(match.group(1))
        seconds = int(match.group(2))

        total_seconds = (
            minutes * 60
            + seconds
        )

    else:

        total_seconds = 0



    # Get current lyric

    current_lyric = sync.get_current_lyric(
        lyrics,
        total_seconds
    )



    # OLED preview

    os.system("cls")


    print(title)

    print(artist)

    print("----------------")

    print(format_time(current_time))

    print()

    print(current_lyric)

    esp.send(
        title,
        artist,
        format_time(current_time),
        current_lyric
    )
    # Debug

    print("\nDEBUG")
    print("Seconds:", total_seconds)
    print("Lyrics:", len(lyrics))


    time.sleep(1)
