class Time:
    def __init__(self):
        self.seconds = None
        self.minutes = None
        self.clock = None

    def time_enter(self):
        self.seconds = input('Seconds: ')
        self.minutes = input('Minutes: ')
        self.clock = input('Clock: ')

    def time_print(self):
        print(f'{self.clock}.{self.minutes}.{self.seconds}')


a = Time()
a.time_enter()
a.time_print()
