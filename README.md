LED-Candle-for-Raspberry-Pi
====

## Overview

LED candle library for Raspberry Pi. Using this library, you can create LED candles. Combine multiple frequencies to simulate candle fluctuations.
With this library, you can change brightness, speed, fluctuation and more. This can be used for illumination as well as candles.

## Demo

````python:example
from Candle import Candle
import time
import RPi.GPIO as GPIO

sleep_ms = lambda ms: time.sleep(ms / 1000.0)

candle = Candle()
candle.create(24)
candle.shuffle(0, 1000)

for times in range(2000):
    candle.refresh()
    sleep_ms(10)

GPIO.cleanup()
````

## Usage

#### Method

````python:example
Candle(gpiomode=GPIO.BCM)
````

gpiomode: How to specify GPIO number

Create an instance.

````python:example
create(pin, brightness=100, rate=100, ratio=100, pwmfreq=1000)
````

pin: GPIO pin number  
brightness: Brightness level(optional)  
rate: Speed ​​of change(optional)  
ratio: The magnitude of the fluctuation(optional)  
pwmfreq: PWM frequency(optional)

Creates a candle on the specified pin.

````python:example
reset(pin=None)
````

pin: GPIO pin number(optional)

Resets the settings of the specified pin.
If the argument is omitted, it is executed on all pins.

````python:example
shuffle(min, max, pin=None)
````

min: Lower bound of shuffle range  
max: Upper limit of shuffle range  
pin: GPIO pin number(optional)

Shuffles the start of the waveform to the specified pin between min and max.
If pin is omitted, execute on all pins.

````python:example
pin(beforepin, afterpin, pwmfreq=1000)
````

beforepin: Pin before change  
afterpin: Pin after change  
pwmfreq: PWM frequency(optional)

Change the output pin.
If pin is omitted, execute on all pins.

````python:example
brightness(brightness, pin=None)
````

brightness: Brightness level  
pin: GPIO pin number(optional)

Change the brightness.
If pin is omitted, execute on all pins.

````python:example
rate(rate, pin=None)
````

rate: Speed ​​of change  
pin: GPIO pin number(optional)

Change the speed of change.
If pin is omitted, execute on all pins.

````python:example
ratio(ratio, pin=None)
````

ratio: The magnitude of the fluctuation  
pin: GPIO pin number(optional)

Change the size of the fluctuation.
If pin is omitted, execute on all pins.

````python:example
parameter(value, pin=None)
````

value: Parameter value  
pin: GPIO pin number(optional)

Change the value of a parameter.
If pin is omitted, execute on all pins.

````python:example
wave(value, pin=None)
````

value: Number of sine waves to combine  
pin: GPIO pin number(optional)

Change the number of sine waves to combine.
If pin is omitted, execute on all pins.

````python:example
refresh(pin=None)
````

pin: GPIO pin number(optional)

PWM output to the specified pin.
If the argument is omitted, it is executed on all pins.

## License

MIT
