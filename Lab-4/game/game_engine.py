import pygame
import random
from .hole import Hole
from .sounds import SoundBank

DARK_BROWN = (60, 40, 20)
MOLE_BROWN = (140, 95, 55)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PANEL = (245, 235, 210)
BUTTON = (90, 140, 70)
BUTTON_HOVER = (120, 175, 95)
EXIT_BUTTON = (170, 70, 60)
EXIT_BUTTON_HOVER = (205, 95, 80)

FPS = 60

DIFFICULTIES = {
    "Easy": {"spawn_chance": 0.012, "mole_up_frames": 70},
    "Medium": {"spawn_chance": 0.02, "mole_up_frames": 45},
    "Hard": {"spawn_chance": 0.035, "mole_up_frames": 26},
}

DIFFICULTY_KEYS = {
    pygame.K_1: "Easy",
    pygame.K_2: "Medium",
    pygame.K_3: "Hard",
    pygame.K_e: "Easy",
    pygame.K_m: "Medium",
    pygame.K_h: "Hard",
}


class GameEngine:
    def __init__(self, width, height, rows=3, cols=3):
        self.width = width
        self.height = height

        self.holes = []
        spacing_x = width // (cols + 1)
        spacing_y = (height - 80) // (rows + 1)
        for r in range(rows):
            for c in range(cols):
                cx = spacing_x * (c + 1)
                cy = 80 + spacing_y * (r + 1)
                self.holes.append(Hole(cx, cy))

        self.round_seconds = 30
        self.font = pygame.font.SysFont("Arial", 28)
        self.title_font = pygame.font.SysFont("Arial", 44, bold=True)
        self.small_font = pygame.font.SysFont("Arial", 20)
        self.sounds = SoundBank()

        self.buttons = []
        labels = list(DIFFICULTIES) + ["Exit"]
        button_w, button_h, gap = 200, 44, 12
        top = height // 2 - 10
        for i, label in enumerate(labels):
            rect = pygame.Rect(0, 0, button_w, button_h)
            rect.centerx = width // 2
            rect.top = top + i * (button_h + gap)
            self.buttons.append((label, rect))

        self.start_round("Medium")

    def start_round(self, difficulty):
        settings = DIFFICULTIES[difficulty]
        self.difficulty = difficulty
        self.spawn_chance = settings["spawn_chance"]
        self.mole_up_frames = settings["mole_up_frames"]
        self.time_left_frames = self.round_seconds * FPS
        self.score = 0
        self.misses = 0
        self.game_over = False
        for hole in self.holes:
            hole.active = False
            hole.timer = 0

    def handle_event(self, event):
        if self.game_over:
            self._handle_game_over_event(event)
            return
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._handle_click(event.pos)

    def _handle_game_over_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in DIFFICULTY_KEYS:
                self.start_round(DIFFICULTY_KEYS[event.key])
            elif event.key in (pygame.K_ESCAPE, pygame.K_q):
                self._request_exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for label, rect in self.buttons:
                if rect.collidepoint(event.pos):
                    if label == "Exit":
                        self._request_exit()
                    else:
                        self.start_round(label)
                    break

    def _request_exit(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    def _handle_click(self, pos):
        target = None
        for hole in self.holes:
            if hole.active and hole.contains(pos):
                if target is None or hole.distance_squared(pos) < target.distance_squared(pos):
                    target = hole

        if target is not None and target.whack():
            self.score += 1
            self.sounds.play("hit")
        else:
            self.misses += 1
            self.sounds.play("miss")

    def handle_input(self):
        pass

    def update(self):
        if self.game_over:
            return

        self.time_left_frames -= 1
        if self.time_left_frames <= 0:
            self.time_left_frames = 0
            self.game_over = True
            for hole in self.holes:
                hole.active = False
            self.sounds.play("end")
            return

        for hole in self.holes:
            hole.update()
            if not hole.active and random.random() < self.spawn_chance:
                hole.pop_up(self.mole_up_frames)

    def render(self, screen):
        for hole in self.holes:
            pygame.draw.circle(screen, DARK_BROWN, (hole.center_x, hole.center_y), 40)
            if hole.active:
                pygame.draw.circle(screen, MOLE_BROWN, (hole.center_x, hole.center_y), 32)

        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        seconds_left = max(0, (self.time_left_frames + FPS - 1) // FPS)
        timer_text = self.font.render(f"Time: {seconds_left}s", True, BLACK)
        screen.blit(timer_text, (self.width - 140, 10))

        level_text = self.small_font.render(self.difficulty, True, BLACK)
        screen.blit(level_text, level_text.get_rect(midtop=(self.width // 2, 16)))

        if self.game_over:
            self._render_game_over(screen)

    def _render_game_over(self, screen):
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))

        panel = pygame.Rect(0, 0, 320, 440)
        panel.center = (self.width // 2, self.height // 2)
        pygame.draw.rect(screen, PANEL, panel, border_radius=12)
        pygame.draw.rect(screen, DARK_BROWN, panel, width=3, border_radius=12)

        title = self.title_font.render("Time's Up!", True, DARK_BROWN)
        screen.blit(title, title.get_rect(midtop=(panel.centerx, panel.top + 18)))

        score = self.font.render(f"Final Score: {self.score}", True, BLACK)
        screen.blit(score, score.get_rect(midtop=(panel.centerx, panel.top + 78)))

        misses = self.small_font.render(f"Missed clicks: {self.misses}", True, BLACK)
        screen.blit(misses, misses.get_rect(midtop=(panel.centerx, panel.top + 116)))

        prompt = self.small_font.render("Play again or exit:", True, BLACK)
        screen.blit(prompt, prompt.get_rect(midtop=(panel.centerx, panel.top + 146)))

        mouse_pos = pygame.mouse.get_pos()
        for i, (label, rect) in enumerate(self.buttons):
            hovered = rect.collidepoint(mouse_pos)
            if label == "Exit":
                color = EXIT_BUTTON_HOVER if hovered else EXIT_BUTTON
                caption = "Exit (Esc)"
            else:
                color = BUTTON_HOVER if hovered else BUTTON
                caption = f"{label} ({i + 1})"
            pygame.draw.rect(screen, color, rect, border_radius=8)
            text = self.small_font.render(caption, True, WHITE)
            screen.blit(text, text.get_rect(center=rect.center))
