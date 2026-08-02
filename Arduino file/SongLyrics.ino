#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

String title = "";
String artist = "";
String timestamp = "";
String lyric = "";

void drawDisplay() {

  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);
  display.setTextSize(1);

  int y = 0;

  display.setCursor(0, y);
  display.println(title);
  y += 10;

  display.setCursor(0, y);
  display.println(artist);
  y += 10;

  display.setCursor(0, y);
  display.println(timestamp);
  y += 10;

  String text = lyric;

  while (text.length() > 0 && y < 64) {

    int maxChars = 21;
    int split = maxChars;

    if (text.length() <= maxChars) {
      display.setCursor(0, y);
      display.println(text);
      break;
    }

    while (split > 0 && text[split] != ' ')
      split--;

    if (split == 0)
      split = maxChars;

    display.setCursor(0, y);
    display.println(text.substring(0, split));

    text = text.substring(split);
    text.trim();

    y += 10;
  }

  display.display();
}


void parseData(String data) {

  int p1 = data.indexOf('|');
  int p2 = data.indexOf('|', p1 + 1);
  int p3 = data.indexOf('|', p2 + 1);

  if (p1 == -1 || p2 == -1 || p3 == -1)
    return;

  title = data.substring(0, p1);
  artist = data.substring(p1 + 1, p2);
  timestamp = data.substring(p2 + 1, p3);
  lyric = data.substring(p3 + 1);

  drawDisplay();
}


void setup() {

  Serial.begin(115200);

  Wire.begin(21, 22);

  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    while (true);
  }

  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);
  display.invertDisplay(false);
  display.setTextSize(1);
  display.setCursor(0, 0);
  display.println("Waiting for lyrics...");
  display.display();
}


void loop() {

  if (Serial.available()) {

    String data = Serial.readStringUntil('\n');

    data.trim();

    parseData(data);
  }
}