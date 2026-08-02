import re


class LRCParser:

    def parse(self, lrc_text):

        lyrics = []

        if not lrc_text:
            return lyrics


        pattern = r"\[(\d+):(\d+\.\d+)\](.*)"


        for line in lrc_text.splitlines():

            match = re.match(pattern, line)


            if match:

                minutes = int(match.group(1))

                seconds = float(match.group(2))


                timestamp = (
                    minutes * 60
                    + seconds
                )


                lyric = match.group(3).strip()


                lyrics.append(
                    (timestamp, lyric)
                )


        return lyrics
