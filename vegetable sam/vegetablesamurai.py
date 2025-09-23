import pygame, sys #sys allows me to interact with the runtime enviroment 
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

vegetable_types = [
    {
        "name": "carrot",
        "image": carrot_img,
        "score": 10
    }
]
#dont understand what half of this means 
class Vegetable: #basically the attributes of what it actually does 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_y = random.uniform(-12, -18)  # upward velocity
        self.gravity = 0.5  # gravity - pulls vegetable back down 
        self.active = True
        # Track if this vegetable is still in the game or has been sliced/removed
        self.image = carrot_img 
        # What image this vegetable uses (currently all vegetables use carrot image)
    
    def update(self):
        if self.active:
            self.y += self.velocity_y  # move vegetable up or down
            self.velocity_y += self.gravity  # gravity makes it fall faster
            
            # remove vegetable when it falls off bottom of screen
            if self.y > 1080:
                self.active = False
    
    def draw(self, surface):
        if self.active:
            surface.blit(self.image, (int(self.x), int(self.y)))
    
    def get_rect(self):
        return pygame.Rect(int(self.x), int(self.y), 50, 50)


#game variables 
score = 0  #player score 
lives = 3  #player lives 
veg_screen = [] # array of vegetables for actual random
vegetable = ["carrot"] #array of vegetables 
spawn_timer = 0

def spawn_vegetable():
    spawn_x = random.randint(100, 1820)  # random x position across screen
    spawn_y = 1080  # start from bottom of screen
    random_veg_type = random.choice(vegetable_types)
    new_veg = Vegetable(spawn_x, spawn_y, random_veg_type)
    veg_screen.append(new_veg)

#   lets the game run
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    spawn_timer += 1 #calls spawn veg from before 
    if spawn_timer >= 90:
        spawn_vegetable()
        spawn_timer = 0

    # update vegetables
    for veg in veg_screen[:]:
        veg.update()
        if not veg.active:
            veg_screen.remove(veg)

    # draw background
    window.blit(background, (0, 0))

    # update display
    pygame.display.update()
    gametime.tick(60)
    spawn_timer += 1
    if spawn_timer >= 90:
        spawn_vegetable()
        spawn_timer = 0

    # update vegetables
    for veg in veg_screen[:]:
        veg.update()
        if not veg.active:
            veg_screen.remove(veg)

    for veg in veg_screen:
        veg.draw(window)

pygame.quit()
sys.exit()







 
