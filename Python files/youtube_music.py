from playwright.sync_api import sync_playwright
import time


class YouTubeMusic:

    def __init__(self):

        self.playwright = sync_playwright().start()

        # Connect to already running Chrome
        self.browser = self.playwright.chromium.connect_over_cdp(
            "http://localhost:9222"
        )

        self.page = self.browser.contexts[0].pages[0]

        print("Connected to Chrome")


    def get_song(self):

        try:

            self.page.wait_for_selector(
                "ytmusic-player-bar .title",
                timeout=10000
            )

            title = self.page.locator(
                "ytmusic-player-bar .title"
            ).inner_text()


            artist = self.page.locator(
                "ytmusic-player-bar .byline"
            ).inner_text()


            # Remove extra information
            artist = artist.split("\n")[0]
            artist = artist.split("•")[0].strip()


            # Get current time
            current_time = self.page.locator(
                "#progress-bar"
            ).get_attribute("aria-valuetext")


            return title, artist, current_time


        except Exception as e:

            print("YouTube Music Error:", e)

            return None, None, None
