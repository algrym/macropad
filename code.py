#!/usr/bin/env python3
"""
Driver for Adafruit MacroPad.
"""
from adafruit_macropad import MacroPad
from rainbowio import colorwheel

macropad = MacroPad()

text_lines = macropad.display_text(title="MacroPad \nInfo")
keypress_count = 0

while True:
    key_event = macropad.keys.events.get()
    if key_event:
        if key_event.pressed:
            text_lines[1].text = "Key {}!".format(key_event.key_number)
            macropad.pixels[key_event.key_number] = colorwheel(
                int(255 / 12) * (key_event.key_number +
                                 keypress_count)
            )
            keypress_count += 1
        else:
            macropad.pixels.fill((0, 0, 0))
    text_lines[2].text = "Encoder {}".format(macropad.encoder)
    text_lines.show()
