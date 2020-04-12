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
