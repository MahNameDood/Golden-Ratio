import math, pygame

direction_dic = {
	'up':'left',
	'left':'down',
	'down':'right',
	'right':'up'
}

def fibonacci(length):
	final = [0,1]
	for i in range(2, length-2, 1):
		final.append(final[i-2]+final[i-1])

	return final

def get_sides(seq):
	#final = []
	#for val in seq:
		#if val != 0:
			#final.append(math.sqrt(val))
	return [val for val in seq if val != 0]

def calc_rects(sides, start_pos):
	direction = 'up'
	pos = [start_pos[0], start_pos[1]]
	rects = []

	rects.append(('right', pygame.Rect(pos, (sides[0], sides[0]))))
	#print(sides)
	for i, side in enumerate(sides[1:], 1):	
		
		#print(f'SIDE: {i}\nSIDE VAL: {sides[i]}\nSIDE-1 VAL: {sides[i-1]}\n')

		# find pos
		if direction == 'up':
			pos[1] -= side
			pos[0] += sides[i-1] - side
		elif direction == 'left':
			pos[0] -= side
		elif direction == 'down':
			pos[1] += sides[i-1]
		else:
			pos[0] += sides[i-1]
			pos[1] += sides[i-1] - side
		

		#append rect
		tup = (direction, pygame.Rect(pos, (side,side)))
		rects.append(tup)
		direction = direction_dic[direction]

	return rects

def render_rects(win, rects, zoom, win_dim, cam):
	print(rects)
	for rect_tup in rects:
		print(rect_tup)
		rect = rect_tup[1]
		direction = rect_tup[0]
		pos = projected_pos(rect.topleft, zoom, win_dim, cam)
		pygame.draw.rect(win, (255,255,255), pygame.Rect(pos, (rect.size[0]*zoom, rect.size[1]*zoom)), round(1.0))

		#arc 
		angles = arc_angles(direction)
		new_rect = arc_rect(rect, direction)
		pygame.draw.arc(win, (255,255,0), pygame.Rect(projected_pos(new_rect.topleft, zoom, win_dim, cam), (new_rect.size[0]*zoom, new_rect.size[1]*zoom)), angles[0], angles[1], 1)


def projected_pos(pos, zoom, win_dim, cam):
	return zoomed_pos((pos[0]-cam[0], pos[1]-cam[1]), zoom, win_dim)

def zoomed_pos(pos, zoom, win_dim):
	new_pos = [pos[0], pos[1]]
	new_pos[0] -= win_dim[0]/2
	new_pos[1] -= win_dim[1]/2

	new_pos[0] *= zoom
	new_pos[1] *= zoom

	new_pos[0] += win_dim[0]/2
	new_pos[1] += win_dim[1]/2

	return new_pos

def arc_angles(direction):
	if direction == 'up':
		return 0, (math.pi/2)
	elif direction == 'left':
		return (math.pi/2), math.pi
	elif direction == 'down':
		return math.pi, 0-(math.pi/2)
	elif direction == 'right':
		return 0-(math.pi/2), 0

def arc_rect(og_rect, direction):
	pos = og_rect.topleft
	size = og_rect.size[0]
	if direction == 'up':
		return pygame.Rect((pos[0]-size, pos[1]), (size*2, size*2))
	elif direction == 'left':
		return pygame.Rect(pos, (size*2, size*2))
	elif direction == 'down':
		return pygame.Rect((pos[0], pos[1]-size), (size*2, size*2))
	elif direction == 'right':
		return pygame.Rect((pos[0]-size, pos[1]-size), (size*2, size*2))