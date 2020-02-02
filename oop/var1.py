class Time:
    def __init__(self):
        self.seconds = None
        self.minutes = None
        self.hours = None

    def time_input(self):
        self.seconds = int(input('Seconds: '))
        self.minutes = int(input('Minutes: '))
        self.hours = int(input('hours: '))

    def time_print(self):
        print(f'{self.hours}:{self.minutes}:{self.seconds}')


a = Time()
a.time_input()
a.time_print()
