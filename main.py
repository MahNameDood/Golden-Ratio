import pygame, sys, random
from funcs import *

pygame.init()

WIDTH = 1900
HEIGHT = 1100
win_dim = (WIDTH, HEIGHT)
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

fib = fibonacci(30)
lens = get_sides(fib)
rects = calc_rects(lens, [900,500])

zoom = 1.0
cam = [0,0]
camspeed = 10

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	win.fill((0,0,0))
	keys = pygame.key.get_pressed()

	#inputs
	if keys[pygame.K_a]:
		cam[0] -= camspeed/zoom
	if keys[pygame.K_d]:
		cam[0] += camspeed/zoom
	if keys[pygame.K_w]:
		cam[1] -= camspeed/zoom
	if keys[pygame.K_s]:
		cam[1] += camspeed/zoom

	if keys[pygame.K_e]:
		zoom -= 0.1 * zoom
	if keys[pygame.K_q]:
		zoom += 0.1 * zoom

	render_rects(win, rects, zoom, win_dim, cam)

	pygame.display.update()
	clock.tick(60)