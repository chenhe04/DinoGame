class SpeedManager:
    def __init__(self, start_speed=9, speed_interval=5, max_speed=19):
        self.speed = start_speed
        self.speed_interval = speed_interval
        self.max_speed = max_speed

    def update_speed(self, score):
        if score >= 100:
            self.speed = 21
        elif score > 0 and score % self.speed_interval == 0:
            self.speed = min(self.speed + 1, self.max_speed)

    def get_speed(self):
        return self.speed
