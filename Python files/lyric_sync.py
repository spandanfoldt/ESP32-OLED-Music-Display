class LyricSync:


    def get_current_lyric(
            self,
            lyrics,
            current_time
        ):


        current_line = ""


        for timestamp, line in lyrics:


            if current_time >= timestamp:

                current_line = line


            else:

                break


        return current_line
