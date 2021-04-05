"""
Created on:
    May 1 2019
Developers:
    Yeshwanth Reddy
"""

import settings as st
import pygame

checkpoints = []


class Checkpoint(object):
    def __init__(self, pos):
        checkpoints.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], st.blockLength, st.blockLength)
