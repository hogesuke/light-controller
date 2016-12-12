import wiringpi

class ServoController:

    def __init__(self, pin=18):
        self.pin = pin

        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(self.pin, 2)
        wiringpi.pwmSetMode(0)
        wiringpi.pwmSetRange(1024)
        wiringpi.pwmSetClock(375)

    def move(self, degree):
        if -90 < degree < 90:
            raise RuntimeError('可動域を超えた度数が指定されています。')

        move_deg = int(81 + 41 / 90 * degree)
        wiringpi.pwmWrite(self.pin, move_deg)
