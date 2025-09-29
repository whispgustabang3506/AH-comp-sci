import pygame
import os 
import random  #will be used later for spawning random things 

pygame.init() # INITILIZES GAME 

#game window set up 
pygame.display.set_caption("vegetable samurai")
window = pygame.display.set_mode((1920,1080)) #creates game window  
gametime = pygame.time.Clock()

#assets
game_folder = os.path.dirname(__file__)
assets_folder = os.path.join(game_folder, "assets")
backgroundpath = os.path.join(assets_folder, "backgroundtest.jpg")

#Background related assets 
background = pygame.image.load(backgroundpath) 
background = pygame.transform.scale(background, (1920, 1080))

#veg related assets 
carrot_img = pygame.image.load(os.path.join(assets_folder, "carrot.png")) # not even sure what os.path join does 
carrot_img = pygame.transform.scale(carrot_img, (50, 50))  # scale to desired size

potato_img = pygame.image.load(os.path.join(assets_folder, "potato.png"))
potato_img = pygame.transform.scale(potato_img, (50, 50))

beetroot_img = pygame.image.load(os.path.join(assets_folder, "beetroot.png"))
beetroot_img = pygame.transform.scale(beetroot_img,(50,50))

pumpkin_img = pygame.image.load(os.path.join(assets_folder, "pumpkin.png"))
pumpkin_img = pygame.transform.scale(pumpkin_img, (100,100))

tomato_img = pygame.image.load(os.path.join(assets_folder, "tomato.png"))
tomato_img = pygame.transform.scale(tomato_img, (500,500))



# Array of vegetable objects - each has name, image, and score value
vegetable_types = [
    {
        "name": "carrot",
        "image": carrot_img,
        "score": 10
    },
    {
        "name": "potato", 
        "image": potato_img,
        "score": 15
    },
    {
        "name": "beetroot",
        "image": beetroot_img,
        "score": 15
    },
    {
        "name": "pumkin",
        "image": pumpkin_img,
        "score": 20
    },
    {
        "name": "tomato",
        "image": tomato_img,
        "score": 10
    }
]

class Vegetable:
    def __init__(self, x, y, veg_type):
        # x = horizontal position, y = vertical position  
        self.x = x  # where vegetable appears horizontally
        self.y = y  # where vegetable appears vertically (starts at bottom)
        # Minimum velocity = sqrt(2 * gravity * distance) = sqrt(2 * 0.5 * 540) = ~23, had to use a tut for this!
        min_velocity = -23  # minimum to reach middle
        max_velocity = -30  # maximum for variety
        horizontal_velocityMin = -5
        horizontal_velocityMax = 5
        self.velocity_x = random.uniform(horizontal_velocityMin, horizontal_velocityMax)
        self.velocity_y = random.uniform(min_velocity, max_velocity)  # guaranteed to reach middle
        self.gravity = 0.5     # how fast it falls back down
        self.active = True     # whether vegetable is still on screen
        self.veg_type = veg_type  # stores name, image, and score


    def update(self):
        if self.active:
            self.x += self.velocity_x  # move vegetable left or right
            self.y += self.velocity_y  # move vegetable up or down
            self.velocity_y += self.gravity  # gravity makes it fall faster
            
            # remove vegetable when it falls off bottom of screen
            if self.y > 1080:
                self.active = False

    
    def draw(self, surface):
        if self.active:
            surface.blit(self.veg_type["image"], (int(self.x), int(self.y))) #lets images be seen
    
    def get_rect(self):
        return pygame.Rect(int(self.x), int(self.y), 50, 50)

def check_simple_collision(mouse_pos, vegetable):
    """Simple collision: check if mouse is close to vegetable center"""
    mouse_x, mouse_y = mouse_pos # = x and y cords of mouse 
    veg_x, veg_y = vegetable.x, vegetable.y # same things just for vegetable 
        # Calculate distance between mouse and vegetable center
    distance = ((mouse_x - veg_x) ** 2 + (mouse_y - veg_y) ** 2) ** 0.5
    
    
    # If mouse is within 50 pixels of vegetable, it's a hit
    return distance < 50





#game variables 
score = 0
vegetables_on_screen = []
spawn_timer = 0
mouse_pressed = False #if statmeent for when if the mouse is being pressed blah blah you get it 

def spawn_vegetable():
    spawn_x = random.randint(100, 1820)  # random x position across screen
    spawn_y = 1080  # start from bottom of screen
    random_veg_type = random.choice(vegetable_types)
    new_veg = Vegetable(spawn_x, spawn_y, random_veg_type)
    vegetables_on_screen.append(new_veg)


#game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN: #alternative get it?
            if event.button == 1: #this is the left mouse right mouse would be 2 
                mouse_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP: # user not pressing mouse button
            if event.button == 1: #left mouse
                mouse_pressed = False

    if mouse_pressed:
        current_mouse_pos = pygame.mouse.get_pos()
        for veg in vegetables_on_screen[:]:
            if veg.active and check_simple_collision(current_mouse_pos, veg):
                #vegetable was sliced 
                score += veg.veg_type["score"]
                veg.active = False
                vegetables_on_screen.remove(veg)
    
    
        
  
    
            

    spawn_timer += 1
    if spawn_timer >= 90:
        spawn_vegetable()
        spawn_timer = 0

    # update vegetables
    for veg in vegetables_on_screen[:]:
        veg.update()
        if not veg.active:
            vegetables_on_screen.remove(veg)

    # draw everything
    window.blit(background, (0, 0))
    
    for veg in vegetables_on_screen:
        veg.draw(window)
    

    if mouse_pressed:
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(window, (255, 255, 255), mouse_pos, 25, 3)

    
    font = pygame.font.Font(None, 50)
    # Create black text for better visibility
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    window.blit(score_text, (0,0))


    




    pygame.display.flip()
    gametime.tick(60)

pygame.quit()
