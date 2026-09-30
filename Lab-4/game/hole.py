class Hole:
    def __init__(self, center_x, center_y, hit_radius=32):
        self.center_x = center_x
        self.center_y = center_y
        self.hit_radius = hit_radius
        self.active = False
        self.timer = 0

    def pop_up(self, duration_frames):
        self.active = True
        self.timer = duration_frames

    def update(self):
        if self.active:
            self.timer -= 1
            if self.timer <= 0:
                self.active = False

    def whack(self):
        was_active = self.active
        if was_active:
            self.active = False
            self.timer = 0
        return was_active

    def distance_squared(self, pos):
        dx = pos[0] - self.center_x
        dy = pos[1] - self.center_y
        return dx * dx + dy * dy

    def contains(self, pos):
        return self.distance_squared(pos) <= self.hit_radius * self.hit_radius
