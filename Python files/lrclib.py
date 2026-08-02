import requests


class LRCLyrics:

    def get_synced_lyrics(self, title, artist):

        url = "https://lrclib.net/api/get"

        params = {
            "track_name": title,
            "artist_name": artist
        }


        try:

            response = requests.get(
                url,
                params=params,
                timeout=10
            )


            if response.status_code == 200:

                data = response.json()

                return data.get("syncedLyrics")


            return None


        except Exception as e:

            print("LRCLIB Error:", e)

            return None
