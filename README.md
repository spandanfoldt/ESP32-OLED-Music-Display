# ESP32-OLED-Music-Display

An ESP32-based embedded music display system that shows currently playing YouTube Music track information and lyrics on an OLED display.

The project uses an ESP32 microcontroller with an SSD1306 OLED display to create a compact now-playing interface for displaying song details and lyrics.

## Features

- Displays currently playing song title and artist
- Shows synchronized lyrics on an OLED display
- SSD1306 OLED interfacing using I2C communication
- Smooth text rendering and scrolling
- Compact embedded music information display

## Hardware Used

- ESP32 Development Board
- 0.96 inch OLED Display (SSD1306, I2C)
- Breadboard
- Jumper wires

## Software Used

- Arduino IDE
- ESP32 Arduino Core
- Adafruit GFX Library
- Adafruit SSD1306 Library

## Circuit Connection

| OLED Pin | ESP32 Pin |
|----------|-----------|
| VCC      | 3.3V      |
| GND      | GND       |
| SDA      | GPIO 21   |
| SCK      | GPIO 22   |

## Working Principle

The ESP32 acts as the display controller for the music information system. Song metadata and lyrics obtained from YouTube Music are processed and displayed on an SSD1306 OLED screen.

The OLED communicates with the ESP32 through the I2C protocol, allowing efficient updates with minimal wiring.

## Libraries Used

- Adafruit SSD1306
- Adafruit GFX
