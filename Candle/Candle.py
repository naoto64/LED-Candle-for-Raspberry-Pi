class Candle(object):
    """docstring for Candle."""

    import RPi.GPIO as GPIO

    __pin = {}
    __brightness = {}
    __rate = {}
    __ratio = {}
    __led_x = {}
    __led_k = {}
    __led_w = {}

    def __init__(self, gpiomode=GPIO.BCM):
        super(Candle, self).__init__()
        import RPi.GPIO as GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(gpioMode)

    def create(self, pin, brightness=100, rate=100, ratio=100, pwmfreq=1000):
        import RPi.GPIO as GPIO
        GPIO.setup(pin, GPIO.OUT)
        self.__pin[pin] = GPIO.PWM(pin, pwmfreq)
        self.__pin[pin].start(0)
        self.__brightness[pin] = float(brightness) / 100.0
        self.__rate[pin] = float(rate) / 20000.0
        self.__ratio[pin] = float(ratio)
        self.__led_x[pin] = 0.0
        self.__led_k[pin] = 2.2904
        self.__led_w[pin] = 10

    def reset(self, pin=None):
        if pin is None:
            for i in self.__pin:
                self.__brightness[i] = 1.0
                self.__rate[i] = 0.005
                self.__ratio[i] = 100.0
                self.__led_x[i] = 0.0
                self.__led_k[i] = 2.2904
                self.__led_w[i] = 10
        else:
            self.__brightness[pin] = 1.0
            self.__rate[pin] = 0.005
            self.__ratio[pin] = 100.0
            self.__led_x[pin] = 0.0
            self.__led_k[pin] = 2.2904
            self.__led_w[pin] = 10

    def shuffle(self, min, max, pin=None):
        from random import randrange as random
        if pin is None:
            for i in self.__pin:
                self.__led_x[i] += self.__rate[i] * random(min, max)
        else:
            self.__led_x[pin] += self.__rate[pin] * random(min, max)

    def pin(self, beforepin, afterpin, pwmfreq=1000):
        import RPi.GPIO as GPIO
        del self.__pin[beforepin]
        GPIO.cleanup(beforepin)
        self.__pin[afterpin] = GPIO.PWM(afterpin, pwmfreq)
        self.__pin[afterpin].start(0)

    def brightness(self, brightness, pin=None):
        if pin is None:
            for i in self.__pin:
                self.__brightness[i] = float(brightness) / 100.0
        else:
            self.__brightness[pin] = float(brightness) / 100.0
    def rate(self, rate, pin=None):
        if pin is None:
            for i in self.__pin:
                self.__rate[i] = float(rate) / 20000.0
        else:
            self.__rate[pin] = float(rate) / 20000.0

    def ratio(self, ratio, pin=None):
        if pin is None:
            for i in self.__pin:
                self.__ratio[i] = float(ratio)
        else:
            self.__ratio[pin] = float(ratio)

    def parameter(self, value, pin=None):
        if pin is None:
            for i in self.__pin:
                self.__led_k[i] = float(value)
        else:
            self.__led_k[pin] = float(value)

    def wave(self, value, pin=None):
        if pin is None:
            for i in self.__pin:
                self.__led_w[i] = int(value)
        else:
            self.__led_w[pin] = int(value)

    def refresh(self, pin=None):
        from math import sin
        led_y = 0.0
        led_y_r = []
        if pin is None:
            for j in self.__pin:
                led_y = 0.0
                for i in range(self.__led_w[j]):
                    led_y += sin(self.__led_x[j] * self.__led_k[j] ** i) * self.__led_k[j] ** -i
                self.__led_x[j] += self.__rate[j]
                led_y += 1.75 + (100.0 - self.__ratio[j]) / (self.__ratio[j] / 2.0)
                led_y *= self.__ratio[j] * self.__brightness[j]
                led_y *= 0.3
                if led_y < 0.0:
                    led_y = 0.0
                elif led_y > 100.0:
                    led_y = 100.0
                led_y_r.append(led_y)
                self.__pin[j].ChangeDutyCycle(led_y)
        else:
            for i in range(self.__led_w[pin]):
                led_y += sin(self.__led_x[pin] * self.__led_k[pin] ** i) * self.__led_k[pin] ** -i
            self.__led_x[pin] += self.__rate[pin]
            led_y += 1.75 + (100.0 - self.__ratio[pin]) / (self.__ratio[pin] / 2.0)
            led_y *= self.__ratio[pin] * self.__brightness[pin]
            led_y *= 0.3
            if led_y < 0.0:
                led_y = 0.0
            elif led_y > 100.0:
                led_y = 100.0
            led_y_r.append(led_y)
            self.__pin[pin].ChangeDutyCycle(led_y)
        return led_y_r
