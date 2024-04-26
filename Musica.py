import pygame

pygame.mixer.init()

pygame.mixer.music.load('two_sound.mp3')


def play():
    pygame.mixer.music.play(-1)


def stop():
    pygame.mixer.music.stop()

