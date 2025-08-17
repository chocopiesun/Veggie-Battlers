import time

class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def is_time_up(self):
        if self.start_time is None:
            return True
        return (time.time() - self.start_time) >= self.duration

    def reset(self):
        self.start_time = None
