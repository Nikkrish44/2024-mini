#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)


freq: float = 30
duration: float = 0.1  # seconds

print("Playing frequency (Hz):")

"""for i in range(64):
    print(freq)
    playtone(freq, duration)
    freq = int(freq * 1.1)
"""

bday  = [ 261, 261, 293, 261, 349, 329,
          261, 261, 293, 261, 392, 349,
          261, 261, 523, 440, 349, 329, 293,
          466, 466, 440, 349, 392, 349]

bdayT = [
  .261, .250, .25, .25, .25, .5,
  .25, .25, .25, .25, .25, .5,
  .25, .25, .25, .25, .25, .25, 0.5,
  .25, .25, .25, .25, .25, 0.5
]

playtone(8,1)

for i in range(25):
     print(bday[i])
     playtone(bday[i], bdayT[i])
     playtone(8,bdayT[i]*1.1)
     
    
# Turn off the PWM
quiet()
