import serial
import time


class SerialComm:

    def __init__(self, port="COM3", baud=115200):

        self.ser = serial.Serial(
            port,
            baud,
            timeout=1
        )

        time.sleep(2)

        print("ESP32 connected")


    def send(self, title, artist, timestamp, lyric):

        message = (
            f"{title}|"
            f"{artist}|"
            f"{timestamp}|"
            f"{lyric}\n"
        )


        self.ser.write(
            message.encode("utf-8")
        )


    def close(self):

        self.ser.close()
