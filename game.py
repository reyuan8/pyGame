import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Game1")

walkRight = [
	pygame.image.load('right_walk1.png'),
	pygame.image.load('right_walk2.png')
]

walkLeft = [
	pygame.image.load('left_walk1.png'),
	pygame.image.load('left_walk2.png')
]

rightStand = pygame.image.load('right_stand.png')
leftStand = pygame.image.load('left_stand.png')
bg = pygame.image.load('bg.jpg')

jumpImg_r = pygame.image.load('zombie_jump.png')
fallImg_r = pygame.image.load('zombie_fall.png')

jumpImg_l = pygame.image.load('zombie_jump_l.png')
fallImg_l = pygame.image.load('zombie_fall_l.png')

clock = pygame.time.Clock()

x = 50
y = 500 - 120 
width = 80
height = 110
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0

jumpAnim = False
fallAnim = False

lastMove = "right"

def drawWindow():
	global animCount
	win.blit(bg, (0, 0))

	if animCount + 1 >= 16:
		animCount = 0

	if left:
		win.blit(walkLeft[animCount // 8], (x, y))
		animCount += 1
	elif right:
		win.blit(walkRight[animCount // 8], (x, y))
		animCount += 1
	elif jumpAnim:
		if lastMove == "right":
			win.blit(jumpImg_r, (x, y))
		else:
			win.blit(jumpImg_l, (x, y))
	elif fallAnim:
		if lastMove == "right":
			win.blit(fallImg_r, (x, y))
		else:
			win.blit(fallImg_l, (x, y))
	else:
		if lastMove == "right":
			win.blit(rightStand, (x, y))
		else:
			win.blit(leftStand, (x, y))

	pygame.display.update()

run = True
while run:
	clock.tick(30)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_ESCAPE]:
		run = False

	if keys[pygame.K_LEFT] and x > 5:
		x -= speed
		left, right = True, False
		lastMove = "left"
	elif keys[pygame.K_RIGHT] and x < 500 - width - 5:
		x += speed
		left, right = False, True
		lastMove = "right"
	else:
		left = False
		right = False
		animCount = 0

	if not(isJump):
		if keys[pygame.K_SPACE]:
			isJump = True
	else:
		if jumpCount >= -10:
			if jumpCount < 0:
				y += (jumpCount**2) / 3
				jumpAnim, fallAnim = False, True
				
			else:
				y -= (jumpCount**2) / 3
				jumpAnim, fallAnim = True, False
			jumpCount -= 1
			right, left = False, False
		else:
			isJump, jumpAnim, fallAnim = False, False, False
			jumpCount = 10

	drawWindow()

pygame.quit()