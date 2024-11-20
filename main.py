import asyncio
import pygame

from alien_invasion import AlienInvasion
from game_stats import GameStats

ai = AlienInvasion()

async def main(self):
    """"Start the main loop for the game"""
    while True:
        self._check_events()

        if self.stats.game_active:
            self.ship.update()
            self._update_bullets()
            self._update_aliens()

        self._update_screen()

        await asyncio.sleep(0)

asyncio.run(main(ai))
