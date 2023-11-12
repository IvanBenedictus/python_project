import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

pygame.init()
width, height, rows = 500, 500, 20
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("TheArchitech - The Snake")

class Head():
    rows = rows

    def __init__(self, start, dx=1, dy=0, color=(255, 0, 0)):
        self.pos = start
        self.dx = dx
        self.dy = dy
        self.color = color

    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        self.pos = (self.pos[0]+self.dx, self.pos[1]+self.dy)

    def draw(self, eyes=False):
        dis = width//rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(win, self.color, (i*dis+1, j*dis+1, dis-1, dis-1))
        if eyes:
            center = dis//2
            radius = 2
            first_eyes = (i*dis+center-radius, j*dis+8)
            second_eyes = (i*dis+dis-radius*2, j*dis+8)
            pygame.draw.circle(win, (250, 250, 250), first_eyes, radius)
            pygame.draw.circle(win, (250, 250, 250), second_eyes, radius)

class Snake():
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = Head(pos) # head of the snakes
        self.body.append(self.head)
        self.dx = 0 # move in x direction
        self.dy = 1 # move in y direction

    def move(self):
        for index, cube in enumerate(self.body):
            p = cube.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                cube.move(turn[0], turn[1])
                if index == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if cube.dx == -1 and cube.pos[0] <= 0:
                    cube.pos = (cube.rows-1, cube.pos[1])
                elif cube.dx == 1 and cube.pos[0] >= cube.rows - 1:
                    cube.pos = (0, cube.pos[1])
                elif cube.dy == 1 and cube.pos[1] >= cube.rows - 1:
                    cube.pos = (cube.pos[0], 0)
                elif cube.dy == -1 and cube.pos[1] <= 0:
                    cube.pos = (cube.pos[0], cube.rows-1)
                else:
                    cube.move(cube.dx, cube.dy)

    def reset(self, pos):
        self.head = Head(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dx = 0
        self.dy = 1

    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.dx, tail.dy
 
        if dx == 1 and dy == 0:
            self.body.append(Head((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Head((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Head((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(Head((tail.pos[0],tail.pos[1]+1)))

        self.body[-1].dx = dx
        self.body[-1].dy = dy

    def draw(self):
        for index, cube in enumerate(self.body):
            if index == 0:
                cube.draw(True)
            else:
                cube.draw(False)

def draw_grid(width, rows):
    grid = width // rows

    x = 0
    y = 0

    for length in range(rows):
        x = x + grid
        y = y + grid

        pygame.draw.line(win, (250, 250, 250), (x, 0), (x, width)) # draw the vertical line
        pygame.draw.line(win, (250, 250, 250), (0, y), (width, y)) # draw the horizontal line    

def snack(item):
    position = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z : z.pos == (x, y), position))) > 0:
            continue
        else:
            break
    return (x, y)

def message(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def main():
    player = Snake((255, 0, 0), (10, 10))
    food = Head(snack(player), color = (0, 255, 0))
    running = True

    clock = pygame.time.Clock()

    while running:
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.dx = -1
                    player.dy = 0
                    player.turns[player.head.pos[:]] = [player.dx, player.dy]
                elif event.key == pygame.K_RIGHT:
                    player.dx = 1
                    player.dy = 0
                    player.turns[player.head.pos[:]] = [player.dx, player.dy]
                elif event.key == pygame.K_UP:
                    player.dx = 0
                    player.dy = -1
                    player.turns[player.head.pos[:]] = [player.dx, player.dy]
                elif event.key == pygame.K_DOWN:
                    player.dx = 0
                    player.dy = 1
                    player.turns[player.head.pos[:]] = [player.dx, player.dy]

        win.fill((0, 0, 0))
        draw_grid(width, rows)
        
        player.move()
        
        if player.body[0].pos == food.pos:
            player.add_cube()
            food = Head(snack(player), color = (0, 255, 0))

        for x in range(len(player.body)):
            if player.body[x].pos in list(map(lambda z : z.pos, player.body[x+1:])):
                score = len(player.body)
                message("You Lost!", f"Score: {score}")
                player.reset((10, 10))
                running = False
                break
        
        player.draw()
        food.draw()
       
        pygame.display.update()
    
    pygame.quit()  # Quit Pygame when the loop ends

if __name__ == "__main__":
    main()