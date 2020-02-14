class Time:
    def __init__(self):
        self.seconds = None
        self.minutes = None
        self.hours = None

    def time_input(self):
        self.seconds = int(input('Seconds: '))
        self.minutes = int(input('Minutes: '))
        self.hours = int(input('hours: '))

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'

a = Time()
a.time_input()
print(a)
