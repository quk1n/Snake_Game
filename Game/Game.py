import parameters as p
from Button import *
from Object import *
from effects import *
from images import *
import random

class Game:
    def __init__(self):
        pygame.display.set_caption('Snake Game')
        pygame.display.set_icon(icon)

        self.cactus_options = [69, 449, 37, 410, 40, 420]
        self.img_counter = 0
        self.health = 3
        self.make_jump = False
        self.jump_counter = 30
        self.scores = 0
        self.max_scores = 0
        self.max_above = 0

    def show_menu(self):
        show = True

        start_btn = Button(280, 70)
        quit_btn = Button(125, 70)

        while show:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            display.blit(menu_bckgr, (0, 0))
            start_btn.draw(250, 250, 'Start game', self.start_game, 50)
            quit_btn.draw(350, 350, 'Quit ', quit, 50)

            pygame.display.update()
            clock.tick(60)

    def start_game(self):
        while self.game_cycle():
            self.scores = 0
            self.make_jump = False
            self.jump_counter = 30
            p.usr_y = p.display_height - p.usr_height - 100
            self.health = 3

    def game_cycle(self):
        game = True
        cactus_arr = []
        self.create_cactus_arr(cactus_arr)

        stone, cloud = self.open_random_objects()

        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.make_jump = True
            if keys[pygame.K_ESCAPE]:
                self.pause()

            if self.make_jump:
                self.jump()

            self.count_scores(cactus_arr)

            display.blit(land, (0, 0))
            print_text('Scores: ' + str(self.scores), 600, 10)

            self.draw_array(cactus_arr)
            self.move_objects(stone, cloud)

            self.draw_dino()

            if self.check_collision(cactus_arr):
                game = False

            self.show_health()

            pygame.display.update()
            clock.tick(70)
        return self.game_over()

    def jump(self):
        if self.jump_counter >= -30:
            p.usr_y -= self.jump_counter / 2.5
            self.jump_counter -= 1
        else:
            self.jump_counter = 30
            self.make_jump = False

    def create_cactus_arr(self, array):
        choice = random.randrange(0, 3)
        img = cactus_img[choice]
        width = self.cactus_options[choice * 2]
        height = self.cactus_options[choice * 2 + 1]
        array.append(Object(p.display_width + 20, height, width, img, 4))

        choice = random.randrange(0, 3)
        img = cactus_img[choice]
        width = self.cactus_options[choice * 2]
        height = self.cactus_options[choice * 2 + 1]
        array.append(Object(p.display_width + 300, height, width, img, 4))

        choice = random.randrange(0, 3)
        img = cactus_img[choice]
        width = self.cactus_options[choice * 2]
        height = self.cactus_options[choice * 2 + 1]
        array.append(Object(p.display_width + 600, height, width, img, 4))

    @staticmethod
    def find_radius(array):
        maximum = max(array[0].x, array[1].x, array[2].x)

        if maximum < p.display_width:
            radius = p.display_width
            if radius - maximum < 50:
                radius += 280
        else:
            radius = maximum

        choice = random.randrange(0, 5)
        if choice == 0:
            radius += random.randrange(10, 15)
        else:
            radius += random.randrange(250, 400)

        return radius

    def draw_array(self, array):
        for cactus in array:
            check = cactus.move()
            if not check:
                self.object_return(array, cactus)

    @staticmethod
    def open_random_objects():
        choice = random.randrange(0, 2)
        img_of_stone = stone_img[choice]

        choice = random.randrange(0, 2)
        img_of_cloud = cloud_img[choice]

        stone = Object(p.display_width, p.display_height - 80, 10, img_of_stone, 4)
        cloud = Object(p.display_width, 80, 70, img_of_cloud, 2)

        return stone, cloud

    @staticmethod
    def move_objects(stone, cloud):
        check = stone.move()
        if not check:
            choice = random.randrange(0, 2)
            img_of_stone = stone_img[choice]
            stone.return_self(p.display_width, 500 + random.randrange(10, 80), stone.width, img_of_stone)

        check = cloud.move()
        if not check:
            choice = random.randrange(0, 2)
            img_of_cloud = cloud_img[choice]
            cloud.return_self(p.display_width, random.randrange(10, 200), stone.width, img_of_cloud)

    def draw_dino(self):
        if self.img_counter == 25:
            self.img_counter = 0

        display.blit(dino_img[self.img_counter // 5], (p.usr_x, p.usr_y))
        self.img_counter += 1

    @staticmethod
    def pause():
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            print_text('Game paused, press Enter to continue', 160, 300)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                paused = False

            pygame.display.update()
            clock.tick(15)

    def object_return(self, objects, obj):
        radius = self.find_radius(objects)

        choice = random.randrange(0, 3)
        img = cactus_img[choice]
        width = self.cactus_options[choice * 2]
        height = self.cactus_options[choice * 2 + 1]

        obj.return_self(radius, height, width, img)

    def check_collision(self, barriers):
        for barrier in barriers:
            if barrier.y == 449:
                if not self.make_jump:
                    if barrier.x <= p.usr_x + p.usr_width - 35 <= barrier.x + barrier.width:
                        if self.check_health():
                            self.object_return(barriers, barrier)
                            return False
                        else:
                            return True

                elif self.jump_counter >= 0:
                    if p.usr_y + p.usr_height - 5 >= barrier.y:
                        if barrier.x <= p.usr_x + p.usr_width - 35 <= barrier.x + barrier.width:
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
                else:
                    if p.usr_y + p.usr_height - 10 >= barrier.y:
                        if barrier.x <= p.usr_x <= barrier.x + barrier.width:
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
            else:
                if not self.make_jump:
                    if barrier.x <= p.usr_x + p.usr_width - 5 <= barrier.x + barrier.width:
                        if self.check_health():
                            self.object_return(barriers, barrier)
                            return False
                        else:
                            return True
                elif self.jump_counter == 10:
                    if p.usr_y + p.usr_height - 5 >= barrier.y:
                        if barrier.x <= p.usr_x + p.usr_width - 5 <= barrier.x + barrier.width:
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
                elif self.jump_counter >= -1:
                    if p.usr_y + p.usr_height - 5 >= barrier.y:
                        if barrier.x <= p.usr_x + p.usr_width - 35 <= barrier.x + barrier.width:
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
                    else:
                        if p.usr_y + p.usr_height - 10 >= barrier.y:
                            if barrier.x <= p.usr_x <= barrier.x + barrier.width:
                                if self.check_health():
                                    self.object_return(barriers, barrier)
                                    return False
                                else:
                                    return True

        return False

    def count_scores(self, barriers):
        above_cactus = 0

        if -20 <= self.jump_counter < 25:
            for barrier in barriers:
                if p.usr_y + p.usr_height - 5 <= barrier.y:
                    if barrier.x <= p.usr_x <= barrier.x + barrier.width:
                        above_cactus += 1
                    elif barrier.x <= p.usr_x + p.usr_width <= barrier.x + barrier.width:
                        above_cactus = + 1

            self.max_above = max(self.max_above, above_cactus)
        else:
            if self.jump_counter == -30:
                self.scores += self.max_above
                self.max_above = 0

    def game_over(self):
        if self.scores > self.max_scores:
            self.max_scores = self.scores
        stopped = True
        while stopped:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            print_text('Game over, press Enter to play game or Esc to exit', 20, 300)
            print_text('Max scores: ' + str(self.max_scores), 300, 350)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                return True
            if keys[pygame.K_ESCAPE]:
                return False

            pygame.display.update()
            clock.tick(15)

    def show_health(self):
        show = 0
        x = 20
        while show != self.health:
            display.blit(health_img, (x, 20))
            x += 40
            show += 1

    def check_health(self):
        self.health -= 1
        if self.health == 0:
            return False
        else:
            return True
