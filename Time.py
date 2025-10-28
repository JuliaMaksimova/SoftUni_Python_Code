class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self,hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def next_second(self):
        if self.seconds < Time.max_seconds:
            self.seconds += 1
            return self.get_time()
        else:
            if self.minutes < Time.max_minutes:
                self.minutes += 1
                self.seconds = 0
                return self.get_time()
            else:
                if self.hours < Time.max_hours:
                    self.hours += 1
                    self.minutes = 0
                    self.seconds = 0
                    return self.get_time()
                else:
                    self.hours = 0
                    self.minutes = 0
                    self.seconds = 0
                    return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())

time2 = Time(10, 59, 59)ii
print(time2.next_second())

time3 = Time(23, 59, 59)
print(time3.next_second())


