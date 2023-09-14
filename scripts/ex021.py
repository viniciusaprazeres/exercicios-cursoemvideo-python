import pygame

pygame.init()
pygame.mixer.music.load('raindrops.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()