import pygame as pg 
import random as rnd

col_red=(255,0,0)
col_white=(255,255,255)
col_blue=(0,0,255)
col_green=(0,255,0)
col_black=(0,0,0)
col_bigrec=(218,165,32)
col_smallrec=(255,215,0)
col_scr=(132,112,255)

# key_up = pg.K_w
# key_down = pg.K_s
# key_right = pg.K_d
# key_left = pg.K_a
key_up = pg.K_UP
key_down = pg.K_DOWN
key_right = pg.K_RIGHT
key_left = pg.K_LEFT 

dot_radius = 10
clock_freq= 60
step_size= 5
win_dim = (400,400)

class Blob():
	def __init__ (self,radius,position,colour):
		self.radius = radius
		self.position = position
		self.colour = colour

class Ball():
	def __init__(self,radius,colour,vector,position):
		self.radius=radius
		self.colour=colour
		self.vector=vector
		self.position=position

def sqdist(a,b):
	return(((a[0] - b[0])**2) + ((a[1] - b[1])**2))

def place_balls(balls):
	balls.append(Ball(12,col_green,(int(3 + rnd.random()*3),int(3 + rnd.random()*3)),(0,2)))
	balls.append(Ball(12,col_green,(int(3 + rnd.random()*3),int(3 + rnd.random()*3)),(100,0)))
	balls.append(Ball(12,col_green,(int(3 + rnd.random()*3),int(3 + rnd.random()*3)),(200,0)))
	balls.append(Ball(12,col_green,(int(3 + rnd.random()*3),int(3 + rnd.random()*3)),(0,0)))
	balls.append(Ball(12,col_green,(int(3 + rnd.random()*3),int(3 + rnd.random()*3)),(0,100)))

def main():
	pg.init() 
	display=pg.display.set_mode(win_dim)
	pg.display.set_caption('CompSci Gamers')
	clock=pg.time.Clock()
	font=pg.font.Font(None,55)
	font_scr=pg.font.Font(None,60)

	(x,y)=(200,200)
	running=True
	(left,right,up,down)=(False,False,False,False)

	blobs=[]
	blobs.append(Blob(25,(50,100),col_blue))
	blobs.append(Blob(25,(225,50),col_blue))
	blobs.append(Blob(25,(150,200),col_blue))
	blobs.append(Blob(25,(275,300),col_blue))

	balls=[]
	place_balls(balls)

	alive = True
	score=0

	while running:
		if alive:
			score+=1

			for event in pg.event.get():
				if event.type == pg.QUIT:
					running=False
					break
				elif event.type == pg.KEYDOWN:
					if event.key == key_left: left = True
					elif event.key == key_right: right = True
					elif event.key == key_up: up = True
					elif event.key == key_down: down = True
				elif event.type == pg.KEYUP:
					if event.key == key_left: left = False
					elif event.key == key_right: right = False
					elif event.key == key_up: up = False
					elif event.key == key_down: down = False
				# print(event)

			# x_new = x
			# y_new = y
			# if left and not right: x_new-= step_size
			# if right and not left: x_new+= step_size
			# if up and not down: y_new-= step_size
			# if down and not up: y_new+= step_size

			# x_new = min(x_new, win_dim[0]-dot_radius)
			# x_new = max(x_new, dot_radius)
			# y_new = min(y_new, win_dim[1]-dot_radius)
			# y_new = max(y_new, dot_radius)

			for ball in balls:

				pos_x= ball.position[0]
				pos_y= ball.position[1]
				vec_x= ball.vector[0]
				vec_y= ball.vector[1]

				if pos_x > win_dim[0] - ball.radius:
					pos_x = win_dim[0] - ball.radius
					vec_x= -vec_x
				if pos_y > win_dim[1] - ball.radius:
					pos_y = win_dim[1] - ball.radius
					vec_y= -vec_y
				if pos_y < 0 + ball.radius:
					pos_y = 0 + ball.radius
					vec_y= -vec_y
				if pos_x < 0 + ball.radius:
					pos_x = 0 + ball.radius
					vec_x= -vec_x

				ball.position = (pos_x,pos_y)
				ball.vector = (vec_x,vec_y)

				ball.position = ((ball.position[0] + ball.vector[0]),(ball.position[1] + ball.vector[1]))

			x_new = x
			y_new = y
			if left and not right: x_new-= step_size
			if right and not left: x_new+= step_size
			if up and not down: y_new-= step_size
			if down and not up: y_new+= step_size

			x_new = min(x_new, win_dim[0]-dot_radius)
			x_new = max(x_new, dot_radius)
			y_new = min(y_new, win_dim[1]-dot_radius)
			y_new = max(y_new, dot_radius)

			collision=False

			for blob in blobs:
				if sqdist((x_new,y_new), blob.position) < ((dot_radius + blob.radius)**2):
					collision=True
					break

			for ball in balls:
				if sqdist((x_new,y_new), ball.position) < ((dot_radius + ball.radius)**2):
					alive=False
					break

			if not alive:
				print("You died!")
				print("Your score is: ",score)

			if not collision:
				x = x_new
				y = y_new

			#print("x = ",x,"y = ",y)
			display.fill(col_white)
			for ball in balls:
				pg.draw.circle(display, ball.colour, ball.position, ball.radius )
			for blob in blobs:
				pg.draw.circle(display, blob.colour, blob.position, blob.radius)
			pg.draw.circle(display, col_red, (x,y), dot_radius)
			pg.display.update()
			clock.tick(clock_freq)
		else:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					running=False
					break
				elif event.type == pg.KEYUP:
					if event.key == pg.K_n:
						alive = True
						score = 0
						balls=[]
						place_balls(balls)
						(up,down,left,right) = (False,False,False,False)
			display.fill(col_black)
			pg.draw.rect(display,col_bigrec,(80,45,240,110))
			pg.draw.rect(display,col_smallrec,(85,50,230,100))

			text=font.render("Game Over", True , col_red)
			display.blit(text,(100,85))
			text=font_scr.render("Your score is: "+str(score), True, col_scr)
			display.blit(text,(30,250))

			pg.display.update()
			clock.tick(clock_freq)




	#We've exited our game loops
	pg.quit()
	quit()

if __name__ == '__main__':
	main()
