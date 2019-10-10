#include <FastLED.h>

// How many leds in your strip?
#define NUM_LEDS 7
#define BRIGHTNESS 32
// Which pin are we going to send the data along?
#define DATA_PIN 3

// Define the array of leds
CRGB leds[NUM_LEDS];

void setup() { 
      // What type of LEDs are we using and which order are we sending the data in?
      FastLED.addLeds<WS2811, DATA_PIN, GRB>(leds, NUM_LEDS);
      // Dim the LEDs
      FastLED.setBrightness(BRIGHTNESS);
      
}

void loop() { 
  // Set the LED's value to be red
  leds[0] = CRGB::Red;
  // Send the data to the LEDs
  FastLED.show();
  // Pause for half a second
  delay(500);
  // Set the LED's value to be off
  leds[0] = CRGB::Black;
  // Send the data to the LEDs
  FastLED.show();
  // Pause for half a second
  delay(500);
}
