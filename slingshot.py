import pygame
import math

pygame.init()

width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("TheArchitech - Gravitational Slingshot Effect")

planet_mass = 100
ship_mass = 5
G = 5
planet_size = 50
object_size = 5
velocity_scale = 100

background = pygame.transform.scale(pygame.image.load("source/background.jpg"), (width, height))
planet = pygame.transform.scale(pygame.image.load("source/jupiter.png"), (planet_size * 2, planet_size * 2))

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

class Planet:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass
    
    def draw(self):
        win.blit(planet, (self.x - planet_size, self.y - planet_size))

class Spacecraft:
    def __init__(self, x, y, vel_x, vel_y, mass):
        self.x = x
        self.y = y
        self.vel_x = -vel_x
        self.vel_y = -vel_y
        self.mass = mass

    def move(self, planet):
        distance = math.sqrt((self.x - planet.x)**2 + (self.y - planet.y)**2)
        force = (G * self.mass * planet.mass) / distance ** 2
        
        acceleration = force / self.mass
        angle = math.atan2(planet.y - self.y, planet.x - self.x)

        acceleration_x = acceleration * math.cos(angle)
        acceleration_y = acceleration * math.sin(angle)

        self.vel_x += acceleration_x
        self.vel_y += acceleration_y

        self.x += self.vel_x
        self.y += self.vel_y
    
    def draw(self):
        pygame.draw.circle(win, red, (int(self.x), int(self.y)), object_size)

def create_ship(location, mouse):
    t_x, t_y = location
    m_x, m_y = mouse
    vel_x = (m_x - t_x) / velocity_scale
    vel_y = (m_y - t_y) / velocity_scale
    obj = Spacecraft(t_x, t_y, vel_x, vel_y, ship_mass)
    return obj

def main():
    running = True
    clock = pygame.time.Clock()

    planet = Planet(width // 2, height // 2, planet_mass)
    objects = []
    temp_obj_pos = None

    while running:
        clock.tick(60)
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                temp_obj_pos = mouse_pos

            if event.type == pygame.MOUSEBUTTONUP:
                obj = create_ship(temp_obj_pos, mouse_pos)
                objects.append(obj)
                temp_obj_pos = None

        win.blit(background, (0, 0))

        if temp_obj_pos and pygame.MOUSEBUTTONDOWN:
            pygame.draw.line(win, white, temp_obj_pos, mouse_pos, 2)
            pygame.draw.circle(win, red, temp_obj_pos, object_size)
        
        for obj in objects[:]:
            obj.draw()
            obj.move(planet)
            off_screen = obj.x < 0 or obj.x > width or obj.y < 0 or obj.y > height
            collided = math.sqrt((obj.x - planet.x)**2 + (obj.y - planet.y)**2) <= planet_size
            if off_screen or collided:
                objects.remove(obj)

        planet.draw()

        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()