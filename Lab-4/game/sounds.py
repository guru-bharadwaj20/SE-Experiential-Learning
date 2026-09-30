import math
from array import array

import pygame


class SoundBank:
    def __init__(self):
        self.sounds = {}
        mixer_settings = pygame.mixer.get_init()
        if not mixer_settings:
            try:
                pygame.mixer.init()
            except pygame.error:
                return
            mixer_settings = pygame.mixer.get_init()
        if not mixer_settings or mixer_settings[1] != -16:
            return

        self.sample_rate = mixer_settings[0]
        self.channels = mixer_settings[2]
        self.sounds = {
            "hit": self._build([(880, 0.05), (1320, 0.08)]),
            "miss": self._build([(180, 0.12)]),
            "end": self._build([(660, 0.15), (520, 0.15), (390, 0.35)]),
        }

    def _build(self, notes, volume=0.4):
        samples = array("h")
        for frequency, seconds in notes:
            count = int(self.sample_rate * seconds)
            for i in range(count):
                fade = 1 - i / count
                value = math.sin(2 * math.pi * frequency * i / self.sample_rate)
                sample = int(32767 * volume * fade * value)
                for _ in range(self.channels):
                    samples.append(sample)
        return pygame.mixer.Sound(buffer=samples.tobytes())

    def play(self, name):
        sound = self.sounds.get(name)
        if sound:
            sound.play()
