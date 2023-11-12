import random
import pygame

pygame.init()
pygame.mixer.init()

width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("TheArchitech - Pong Game")

sound = pygame.mixer.Sound("source/bounce.wav")

white = (255,255,255)
red = (255, 0, 0)

class Paddle:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def draw(self):
        width = 15
        height = 100
        paddle = pygame.draw.rect(win, white, (self.x, self.y, width, height))
        return paddle
    
class Ball:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.dx = 5
        self.dy = 5

    def move(self):
        self.x += self.dx
        self.y += self.dy
    
    def draw(self):
        radius = 10
        ball = pygame.draw.circle(win, white, (self.x, self.y), radius)
        return ball

def main():
    running = True
    game_running = False
    clock = pygame.time.Clock()

    paddleA = Paddle(10,250)
    paddleB = Paddle(775,250)
    ball = Ball(400, 300)

    scoreA = 0
    scoreB = 0

    while running:
        # Set the FPS to 60
        clock.tick(120)

        # Title
        font = pygame.font.SysFont("futura", 50)
        title_text = font.render("Pong Game", True, (255, 255, 255))  # Text, antialiasing, color
        title_rect = title_text.get_rect()
        title_rect.center = (width//2, 50)

        # Instruction
        font = pygame.font.SysFont("futura", 30)
        instruction_text = font.render("Press any key to start", True, (255, 255, 255))  # Text, antialiasing, color
        instruction_rect = instruction_text.get_rect()
        instruction_rect.center = (width//2, height//2)

        # Score Display
        font = pygame.font.SysFont("futura", 30)
        
        scoreA_text = font.render(f"Player A: {scoreA}", True, (255, 255, 255))  # Text, antialiasing, color
        scoreA_rect = scoreA_text.get_rect()
        scoreA_rect.center = (100, 50)

        scoreB_text = font.render(f"Player B: {scoreB}", True, (255, 255, 255))  # Text, antialiasing, color
        scoreB_rect = scoreB_text.get_rect()
        scoreB_rect.center = (700, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check for key press events
            if not game_running and event.type == pygame.KEYDOWN:
                scoreA = 0
                scoreB = 0
                # Start the game when any key is pressed
                game_running = True

            if game_running and (scoreA == 5 or scoreB == 5) and event.type == pygame.KEYDOWN:
                # Reset score
                scoreA = 0
                scoreB = 0

        if game_running == False:
            # Display the title
            win.blit(title_text, title_rect)
            win.blit(instruction_text, instruction_rect)
            # Draw the paddle
            paddleA.draw()
            paddleB.draw()
            pygame.display.update()
        
        if game_running and scoreA < 5 and scoreB < 5:
            # Clear the Window
            win.fill((0,0,0))

            # Display the score
            win.blit(scoreA_text, scoreA_rect)
            win.blit(scoreB_text, scoreB_rect)

            # Check the boarder
            if ball.x >= 780:
                ball.x = 400
                ball.y = 300
                ball.dx *= random.choice([-1,1])
                ball.dy *= random.choice([-1,1])
                scoreA += 1

            if ball.x <= 20:
                ball.x = 400
                ball.y = 300
                ball.dx *= random.choice([-1,1])
                ball.dy *= random.choice([-1,1])
                scoreB +=1

            if ball.y >= 580:
                ball.y = 580
                ball.dy *= -1
                sound.play()

            if ball.y <= 20:
                ball.y = 20
                ball.dy *= -1
                sound.play()

            # Keys
            keys = pygame.key.get_pressed()

            if paddleA.y > 10: 
                if keys[pygame.K_w]:
                    paddleA.y +=-10
            else:
                paddleA.y = 10
            
            if paddleA.y < 490:
                if keys[pygame.K_s]:
                    paddleA.y +=10
            else:
                paddleA.y = 490

            if paddleB.y > 10: 
                if keys[pygame.K_UP]:
                    paddleB.y +=-10
            else:
                paddleB.y = 10
            
            if paddleB.y < 490:
                if keys[pygame.K_DOWN]:
                    paddleB.y +=10
            else:
                paddleB.y = 490

            # Paddle and Bounce
            if (ball.x > 765 and ball.x < 780) and ball.y < (paddleB.y + 100) and ball.y > paddleB.y:
                ball.x = 765
                ball.dx *= -1
                sound.play()

            if (ball.x > 20 and ball.x < 35) and ball.y < (paddleA.y + 100) and ball.y > paddleA.y:
                ball.x = 35
                ball.dx *= -1
                sound.play()
            
            # Move the ball
            ball.move()
            ball.draw()

            # Draw the paddle
            paddleA.draw()
            paddleB.draw()

            pygame.display.update()

        if scoreA == 5:
            win.fill((0,0,0))
            font = pygame.font.SysFont("futura", 50)
            winner_text = font.render(f"Player A wins!", True, (255, 255, 255))  # Text, antialiasing, color
            winner_rect = title_text.get_rect()
            winner_rect.center = (width//2, height//2)
            # Display the winner
            win.blit(scoreA_text, scoreA_rect)
            win.blit(scoreB_text, scoreB_rect)
            win.blit(winner_text, winner_rect)
            # Draw the paddle
            paddleA.draw()
            paddleB.draw()
            pygame.display.update()

        if scoreB == 5:
            win.fill((0,0,0))
            font = pygame.font.SysFont("futura", 50)
            winner_text = font.render(f"Player B wins!", True, (255, 255, 255))  # Text, antialiasing, color
            winner_rect = title_text.get_rect()
            winner_rect.center = (width//2, height//2)
            # Display the winner
            win.blit(scoreA_text, scoreA_rect)
            win.blit(scoreB_text, scoreB_rect)
            win.blit(winner_text, winner_rect)
            # Draw the paddle
            paddleA.draw()
            paddleB.draw()
            pygame.display.update()
            
    pygame.quit()

if __name__ == "__main__":
    main()