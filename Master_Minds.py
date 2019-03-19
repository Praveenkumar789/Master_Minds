class Master_minds:
    def __init__(self):
        import pygame as Pygame
        import os as Os
        import time

        self.Pygame = Pygame
        self.Os = Os
        self.clock = self.Pygame.time.Clock()
        # music
        self.Pygame.mixer.init()
        #initialize pygame
        self.Pygame.init()
        # Colors
        self.blue = 0, 0, 255
        self.cyan = 0, 255, 255
        self.black = 0, 0, 0
        self.red = 255, 0, 0
        self.white = 255, 255, 255
        self.pale_blue = 190, 150, 255
        self.yellow = 255, 255, 0

        # Sys Main colors
        self.background_color = self.black
        self.block_color = self.pale_blue
        self.line_color = self.black
        self.Highlighting_color = self.white

        # Loading Images
        self.Large_Spheres = [self.Pygame.image.load('Large_Balls/Blue_Main_Ball.png'),
                         self.Pygame.image.load('Large_Balls/Green_Main_Ball.png'),
                         self.Pygame.image.load('Large_Balls/Red_Main_Ball.png'),
                         self.Pygame.image.load('Large_Balls/Black_Main_Ball.png'),
                         self.Pygame.image.load('Large_Balls/Yellow_Main_Ball.png'),
                         self.Pygame.image.load('Large_Balls/Brown_Main_Ball.png'),
                         self.Pygame.image.load('Large_Balls/Cyan_Main_Ball.png'),
                         self.Pygame.image.load('Large_Balls/Pink_Main_Ball.png')]

        self.Small_Spheres = [self.Pygame.image.load('Small_Balls/Negative_small_ball.png'),
                         self.Pygame.image.load('Small_Balls/Positive_small_ball.png')]

        #Loading background images
        self.Home_page_bgr = self.Pygame.image.load("Background_imgs/Home_page.jpg")
        self.Game_page_bgr = self.Pygame.image.load("Background_imgs/Home_page.jpg")
        self.End_page_bgr =  self.Pygame.image.load("Background_imgs/Home_page.jpg")
        self.WIn_page_bgr = self.Pygame.image.load("Background_imgs/Home_page.jpg")
        self.Loose_page_bgr = self.Pygame.image.load("Background_imgs/Home_page.jpg")

        #Loading Action_images
        self.play_bg = self.Pygame.image.load("Text_bg/Play_bg.png")
        self.master_bg = self.Pygame.image.load("Text_bg/MAster_minds_bg.png")
        # Loading Action_images
        self.Orange_Anim = self.Pygame.image.load("Action_blits/Orange_Anime.png")
        self.Blue_Anim   = self.Pygame.image.load("Action_blits/Blue_Anime.png")
        self.No_Music    = self.Pygame.image.load("Action_blits/Dont_play_music.png")
        self.High_Music  = self.Pygame.image.load("Action_blits/play_music.png")
        self.Settings    = self.Pygame.image.load("Action_blits/settings.png")
        self.Controls    = self.Pygame.image.load("Action_blits/Game_control.png")
        self.Info        = self.Pygame.image.load("Action_blits/Game_info.png")
        self.Leave       = self.Pygame.image.load("Action_blits/Yes_wanna_exit.png")
        self.Stay        = self.Pygame.image.load("Action_blits/No_wanna_stay.png")
        self.Lost        = self.Pygame.image.load("Action_blits/You_Loose.png")
        self.Won         = self.Pygame.image.load("Action_blits/You_won.png")

    def random_quad_generator(self, start=1, end=8):
        """
        This will generate a random quad within the start and end limits
        :param start:  It is the start number for choosing random
        :param end:   It is the end number for choosing random
        :return: returns a list of random quad
        """
        import random

        quad = []
        for i in range(4):
            Num = random.randint(start, end)
            quad.append(Num)
        return quad

    def compare_quads(self, drawn_balls, current_quad):
        """

        Compares and make decision upon comparision made
        :param drawn_balls: list of balls drawn by the player
        :param current_quad: The actual quad that the user have to guess
        :return: list of Decisions made on comparision
        1  : True in position
        0  : False not in position
       -1  : Nothing
        """
        ind = 0
        cnt = 0
        N_M = []
        Decision = []
        cpy = current_quad.copy()
        for ball in drawn_balls:
            if ball - current_quad[ind] == 0:
                cnt += 1
                cpy.remove(ball)
            else:
                N_M.append(ball)
            ind += 1
        Decision = Decision.__add__([1 for i in range(cnt)])
        for ball in N_M:
            if ball in cpy:
                Decision.append(0)
                cpy.remove(ball)
            else:
                Decision.append(-1)

        return Decision

    def Draw_hint(self, Decision, screen, positions, small_images):
        """
        It will draw the hint on the screen
        :param Decision: Decision based on the comparision of drawn_balls and current_quad
        :param screen: screen on which the images are drawn
        :param positions: list of positions for drawing the images
        :param small_images: small images self.white and yellow
        :return: Nothing
        """
        ones = Decision.count(1)
        zeros = Decision.count(0)
        pos = iter(positions)
        for one in range(ones):
            screen.blit(small_images[0], pos.__next__())
        for zero in range(zeros):
            screen.blit(small_images[1], pos.__next__())

    def Draw_Balls(self, Sequence, screen, positions, Large_images):
        """
        It will draw the hint on the screen
        :param Sequence: mbs[current_hand]
        :param screen: screen on which the images are drawn
        :param positions: list of positions for drawing the images
        :param Large_images: All main Ball Images
        :return: Nothing
        """
        pos = iter(positions)
        try:
            for val in Sequence:
                if val != -1:
                    screen.blit(Large_images[val - 1], pos.__next__())
        except StopIteration:
            pass

    def Drawing_Text(self, screen, x_pos, y_pos, text, text_style, text_size, text_color):
        """
        Draws text onto screen

        :param screen:
        :param x_pos:
        :param y_pos:
        :param text: text to be drawn
        :param text_style:
        :param text_size:
        :param text_color:
        :return: Ntg
        """
        myfont = self.Pygame.font.SysFont(text_style, text_size)
        Content = myfont.render(text, 1, text_color)
        screen.blit(Content, (x_pos, y_pos))

    def Create_Window(self, width, height, bg_color, caption):

        """
        Draws a window onto screen
        :param width: width of the window to be created
        :param height: Height of the window to be created
        :param bg_color: Back ground color of the window
        :param caption: Name of the window
        :return: a window
        """
        screen = self.Pygame.display.set_mode((width, height))
        screen.fill(self.background_color)
        self.Pygame.display.set_caption(caption)
        return screen

    def check_Choosen_quad_stat(self, choosen_quad):
        """
        This checks whether drawing four of main balls is done or not
        :param choosen_quad:
        :return:True on Succesion False on Failure
        """
        cnt = 0
        for ele in choosen_quad:
            if ele != -1:
                cnt += 1
        if cnt == 4:
            return True
        return False

    def check_game_end(self, current_quad, choosen_quad):
        """
        This checks whether the game finished positively or not
        :param current_quad:
        :param choosen_quad:
        :return: True on succession, false on Failure
        """
        n = iter(current_quad)
        cnt = 0
        for ele in choosen_quad:
            if ele - next(n) == 0:
                cnt += 1
        if cnt == 4:
            return True
        return False

    def Next_game_Iteration(self):
        """
        It is a generator continuously generate the next nums
        :return: int next game_iteration
        """
        time = 0
        while True:
            yield time
            time += 1

    def Ball_Draw_Positions(self):
        """
        Generates the next Main ball positions
        :return: yields positions
        """
        x_vals = [x for x in range(100, 260, 49)]
        incr = 0
        op = []
        while True:
            y_vals = [459 - incr for i in range(4)]
            op = []
            for i in range(4):
                op.append((x_vals[i], y_vals[i]))
            yield op
            incr += 50

    def Hint_Draw_Positions(self):
        """
        Generator for obtaining next hint positions
        :return: yields positions
        """
        x_vals = [351, 376]
        pr = 0
        while True:
            y_vals = [459 - pr, 484 - pr]
            yield [(x_vals[0], y_vals[0]), (x_vals[1], y_vals[0]), (x_vals[0], y_vals[1]), (x_vals[1], y_vals[1])]
            pr += 50

    def reDraw_window(self, screen, background_color, line_color, block_color, Highlight_color, current_hand_num,
                      Hint_Draw_Sequence, Balls_Draw_Sequence, y_limit_hint, y_limit_block,
                      Decision_seq, Main_block_seq):

        """
        This redraws things on the game main page

        :param screen: screen
        :param background_color: bg color
        :param line_color: line color
        :param block_color: block color
        :param Highlight_color: Highlighting color
        :param current_hand_num:
        :param Hint_Draw_Sequence: Contains Hint Ball positions
        :param Balls_Draw_Sequence: Contains Ball positions
        :param y_limit_hint: where to highlight blocks
        :param y_limit_block: where to highlight hints
        :param Decision_seq: Making decision for drawing hints
        :param Main_block_seq: making decision for drawing main balls
        :return: Ntg
        """
        flag = 0
        mouse_pos = self.Pygame.mouse.get_pos()
        # Describes which hand we are working on

        # display bg
        screen.blit(self.Game_page_bgr, (0, 0))
        # Drawing Main Rectangles
        self.Pygame.draw.rect(screen, line_color, self.Pygame.Rect(100, 8, 199, 502))
        self.Pygame.draw.rect(screen, line_color, self.Pygame.Rect(348, 8, 51, 502))

        # Drawing Down Rectangle
        self.Pygame.draw.rect(screen, line_color, self.Pygame.Rect(49, 530, 402, 52))

        # Drawing Main squares
        for y_pos in range(8, y_limit_block, 50):
            for x_pos in range(100, 251, 49):
                self.Pygame.draw.rect(screen, block_color, self.Pygame.Rect(x_pos + 2, y_pos + 2, 48, 48))

        # Drawing Hint squares
        flag = 1
        y_pos = 8
        x_pos = 348
        while (y_pos < y_limit_hint):
            for x_pos in range(348, 390, 24):
                self.Pygame.draw.rect(screen, block_color, self.Pygame.Rect(x_pos + 2, y_pos + 2, 23, 23))
            if flag == 1:
                flag = 0
                y_pos += 24
            else:
                flag = 1
                y_pos += 26
                # self.Pygame.draw.line(screen, background_color, (x_pos -26, y_pos), (x_pos + 26, y_pos), 1)
        # Drawing Down squares
        for x_pos in range(49, 449, 50):
            self.Pygame.draw.rect(screen, block_color, self.Pygame.Rect(x_pos + 2, 530 + 2, 48, 48))

        # Drawing sprite images
        # Large
        ind = 0
        for x_pos in range(49, 453, 50):
            if (ind == 8): break
            screen.blit(self.Large_Spheres[ind], (x_pos, 532 - 1))
            ind += 1

        # Highlighted_blocks
        for y_pos in range(y_limit_block, 508, 50):
            for x_pos in range(100, 251, 49):
                self.Pygame.draw.rect(screen, Highlight_color, self.Pygame.Rect(x_pos + 2, y_pos + 2, 48, 48))

        # Highlighted_hints
        """for y_pos in range(y_limit_hint, 508, 25):
            for x_pos in range(348, 390, 24):
                self.Pygame.draw.rect(screen, self.white, self.Pygame.Rect(x_pos + 2, y_pos + 2, 23, 23))
        """
        flag = 1
        y_pos = y_limit_hint
        x_pos = 348
        while (y_pos < 508):
            for x_pos in range(348, 390, 24):
                self.Pygame.draw.rect(screen, Highlight_color, self.Pygame.Rect(x_pos + 2, y_pos + 2, 23, 23))
            if flag == 1:
                flag = 0
                y_pos += 24
            else:
                flag = 1
                y_pos += 26
                # self.Pygame.draw.line(screen, background_color, (x_pos -26, y_pos), (x_pos + 26, y_pos), 1)

        # printing_balls as per the Main block sequence
        # printing hints as per the deision sequence
        start = 0
        for hand in range(current_hand_num + 1):
            try:
                self.Draw_Balls(Main_block_seq[start], screen, Balls_Draw_Sequence[hand], self.Large_Spheres)
            except IndexError as p:
                break
            start += 1

        start = 0
        for hand in range(current_hand_num):
            try:
                self.Draw_hint(Decision_seq[start], screen, Hint_Draw_Sequence[hand], self.Small_Spheres)
            except IndexError:
                break
            start += 1

    def color_generator(self):
        """
        It generates random color
        :return: Ntg
        """
        while True:
            yield (self.random_quad_generator(0, 255))[:3]

    def Home_page_maker(self, screen):
        """
        This is the home page
        :param screen: screen
        :return: Ntg
        """
        Homepage_loop_end = False
        future = 1
        self.Pygame.mixer.music.load("Sounds/Floating_Also.mp3")
        self.Pygame.mixer.music.play(-1)
        color = self.color_generator()
        while not Homepage_loop_end:
            pos_x, pos_y = 45, 234
            mouse_pos = self.Pygame.mouse.get_pos()
            #self.Pygame.draw.
            screen.fill(self.background_color)
            screen.blit(self.Home_page_bgr, (0, 0))
            screen.blit(self.master_bg, (1, 110))
            self.Drawing_Text(screen, 62, 113, "MASTER MINDS", "times", 50, color.__next__())
            self.Drawing_Text(screen, 162, 173, "-by PRAvEEN KuMaR", "times", 20, self.yellow)
            for ball in range(1,9):
                screen.blit(self.Large_Spheres[ball -1], (pos_x, pos_y))
                pos_x += 50
            screen.blit(self.play_bg, (156, 430))
            self.Drawing_Text(screen, 215,455, "PLAY", "times", 40, self.black)
            self.Pygame.draw.circle(screen, self.black, (62, 388), 40)
            self.Pygame.draw.circle(screen, self.pale_blue, (62, 388), 37)
            screen.blit(self.Settings, (37, 361))
            self.Pygame.draw.circle(screen, self.black, (438, 388), 40)
            self.Pygame.draw.circle(screen, self.pale_blue, (438, 388), 37)
            screen.blit(self.Controls, (413, 361))
            self.Pygame.draw.circle(screen, self.black, (252, 564), 35)
            self.Pygame.draw.circle(screen, self.pale_blue, (252, 564), 32)
            screen.blit(self.Info, (227, 539))

            for event in self.Pygame.event.get():
                if event.type == self.Pygame.QUIT:
                    self.Pygame.mixer.music.pause()
                    self.ARE_YOU_SURE(screen)
                    self.Pygame.mixer.music.unpause()
                if event.type == self.Pygame.MOUSEBUTTONDOWN:
                    if (170 < mouse_pos[0] < 350) and (440 < mouse_pos[1] < 505):
                        if self.Pygame.mouse.get_pressed()[0] == True:
                            Homepage_loop_end = True
                            self.Pygame.mixer.music.stop()
                    if (37 < mouse_pos[0] < 57) and (361 < mouse_pos[1] < 381):
                        if self.Pygame.mouse.get_pressed()[0] == True:
                            pass

                if event.type == self.Pygame.KEYDOWN:
                    print("key_down, key_down")
                    keypressed = self.Pygame.key.get_pressed()
                    if keypressed[self.Pygame.K_RETURN] == True:
                        Homepage_loop_end = True
                        self.Pygame.mixer.music.stop()
                        self.clock.tick(60)

            if (170 < mouse_pos[0] < 350) and (440 < mouse_pos[1] < 505):
                screen.blit(self.play_bg, (158, 433))
                self.Drawing_Text(screen, 217, 458, "PLAY", "times", 40, self.black)
            if (38 < mouse_pos[0] < 85) and (358 < mouse_pos[1] < 411):
                self.Pygame.draw.circle(screen, self.black, (62, 388), 40)
                self.Pygame.draw.circle(screen, self.cyan, (62, 388), 37)
                screen.blit(self.Settings, (37, 361))
            if (411 < mouse_pos[0] < 464) and (358 < mouse_pos[1] < 411):
                self.Pygame.draw.circle(screen, self.black, (438, 388), 40)
                self.Pygame.draw.circle(screen, self.cyan, (438, 388), 37)
                screen.blit(self.Controls, (413, 361))
            if (231 < mouse_pos[0] < 271) and (538 < mouse_pos[1] < 585):
                self.Pygame.draw.circle(screen, self.black, (252, 564), 35)
                self.Pygame.draw.circle(screen, self.cyan, (252, 564), 32)
                screen.blit(self.Info, (227, 539))
            self.Pygame.display.flip()
            self.clock.tick(600)

    def ARE_YOU_SURE(self,screen):
        """
        This is the confirmation window
        :param screen: screen
        :return: Ntg
        """
        AYS_page_end = False
        color = self.color_generator()
        while not AYS_page_end:
            mouse_pos = self.Pygame.mouse.get_pos()
            screen.fill(self.background_color)
            screen.blit(self.End_page_bgr, (0, 0))
            self.Pygame.draw.rect(screen, self.black, self.Pygame.Rect(150, 205, 218, 40))
            self.Drawing_Text(screen, 152, 209, "ARE YOU SURE", "times", 30, next(color))
            screen.blit(self.Leave, (55,310))
            screen.blit(self.Stay, (361, 310))
            self.Pygame.draw.rect(screen, self.pale_blue, self.Pygame.Rect(55, 424, 90, 40))
            self.Drawing_Text(screen,70 , 426, "YES", "times", 30, self.black)
            self.Pygame.draw.rect(screen, self.pale_blue, self.Pygame.Rect(357, 424, 90, 40))
            self.Drawing_Text(screen, 380, 426, "NO", "times", 30, self.black)

            for event in self.Pygame.event.get():
                if event.type == self.Pygame.QUIT:
                    AYS_page_end = True
                if event.type == self.Pygame.MOUSEBUTTONDOWN:
                    if (55 < mouse_pos[0] < 145) and (424 < mouse_pos[1] < 464):
                        self.gameLoop = False
                        self.Pygame.mixer.quit()
                        self.Pygame.quit()
                        self.Os._exit(0)

                    if (357 < mouse_pos[0] < 447) and (424 < mouse_pos[1] < 464):
                        if self.Pygame.mouse.get_pressed()[0] == True:
                            AYS_page_end = True

            if (55 < mouse_pos[0] < 145) and (424 < mouse_pos[1] < 464):
                self.Pygame.draw.rect(screen, self.red, self.Pygame.Rect(55, 424, 90, 40))
                self.Drawing_Text(screen, 70, 426, "YES", "times", 30, self.black)
            if (357 < mouse_pos[0] < 447) and (424 < mouse_pos[1] < 464):
                self.Pygame.draw.rect(screen, self.blue, self.Pygame.Rect(357, 424, 90, 40))
                self.Drawing_Text(screen, 380, 426, "NO", "times", 30, self.black)

            self.Pygame.display.flip()
            self.clock.tick(600)


    def GAME_WIN_PAGE(self, screen, No_of_turns, current_quad):
        """
        This is the Game win page
        :param screen: screen
        :param No_of_turns: How many turns did the player take to finish game
        :return:
        """
        win_page_end = False
        delta = 0
        STR = "YOU WON IN " + str(No_of_turns) + " CHANCE"
        color = self.color_generator()
        if No_of_turns > 1:
            STR += 'S'
            delta = 6
        while not win_page_end:
            posx, posy = 149,122
            mouse_pos = self.Pygame.mouse.get_pos()
            screen.fill(self.background_color)
            screen.blit(self.WIn_page_bgr, (0, 0))
            for ball in current_quad:
                screen.blit(self.Large_Spheres[ball -1], (posx, posy))
                posx += 50
            self.Pygame.draw.rect(screen, self.black, self.Pygame.Rect(72, 196, 357, 33))
            self.Drawing_Text(screen, 81- delta, 196, STR, "times", 30, next(color))
            screen.blit(self.Won, (212, 290))
            self.Pygame.draw.rect(screen, self.pale_blue, self.Pygame.Rect(55, 424, 100, 40))
            self.Drawing_Text(screen, 63, 426, "HOME", "times", 30, self.black)
            self.Pygame.draw.rect(screen, self.pale_blue, self.Pygame.Rect(357, 424, 100, 40))
            self.Drawing_Text(screen, 372, 426, "QUIT", "times", 30, self.black)

            for event in self.Pygame.event.get():
                if event.type == self.Pygame.QUIT:
                    self.ARE_YOU_SURE(screen)
                if event.type == self.Pygame.MOUSEBUTTONDOWN:
                    if (55 < mouse_pos[0] < 155) and (424 < mouse_pos[1] < 464):
                        if self.Pygame.mouse.get_pressed()[0] == True:
                            win_page_end = True
                    if (357 < mouse_pos[0] < 457) and (424 < mouse_pos[1] < 464):
                        if self.Pygame.mouse.get_pressed()[0] == True:
                            self.gameLoop = False
                            self.Pygame.mixer.quit()
                            self.Pygame.quit()
                            self.Os._exit(0)

            if (55 < mouse_pos[0] < 155) and (424 < mouse_pos[1] < 464):
                self.Pygame.draw.rect(screen, self.blue, self.Pygame.Rect(55, 424, 100, 40))
                self.Drawing_Text(screen, 63, 426, "HOME", "times", 30, self.black)
            if (357 < mouse_pos[0] < 457) and (424 < mouse_pos[1] < 464):
                self.Pygame.draw.rect(screen, self.red, self.Pygame.Rect(357, 424, 100, 40))
                self.Drawing_Text(screen, 372, 426, "QUIT", "times", 30, self.black)
            self.Pygame.display.flip()
            self.clock.tick(600)
        new_instance = Master_minds()
        new_instance.Master_Minds()


    def GAME_LOOSE_PAGE(self, screen, current_quad):
        """
        This is the game loose page
        :param screen:screen
        :param current_quad: current quad
        :return:
        """
        loose_page_end = False
        color = self.color_generator()
        while not loose_page_end:
            posx, posy = 149, 122
            mouse_pos = self.Pygame.mouse.get_pos()
            screen.fill(self.background_color)
            screen.blit(self.Loose_page_bgr, (0,0))
            for ball in current_quad:
                screen.blit(self.Large_Spheres[ball -1], (posx, posy))
                posx += 50
            self.Pygame.draw.rect(screen, self.black, self.Pygame.Rect(162, 196, 178, 33))
            self.Drawing_Text(screen, 166, 196,"YOU LOOSE" , "times", 30, next(color))
            screen.blit(self.Lost, (212, 290))
            self.Pygame.draw.rect(screen, self.pale_blue, self.Pygame.Rect(55, 424, 100, 40))
            self.Drawing_Text(screen, 63, 426, "HOME", "times", 30, self.black)
            self.Pygame.draw.rect(screen, self.pale_blue, self.Pygame.Rect(357, 424, 100, 40))
            self.Drawing_Text(screen, 372, 426, "QUIT", "times", 30, self.black)

            for event in self.Pygame.event.get():
                if event.type == self.Pygame.QUIT:
                    self.ARE_YOU_SURE(screen)
                if event.type == self.Pygame.MOUSEBUTTONDOWN:
                    if (55 < mouse_pos[0] < 155) and (424 < mouse_pos[1] < 464):
                        if self.Pygame.mouse.get_pressed()[0] == True:
                            loose_page_end = True
                    if (357 < mouse_pos[0] < 457) and (424 < mouse_pos[1] < 464):
                        if self.Pygame.mouse.get_pressed()[0] == True:
                            self.gameLoop = False
                            self.Pygame.mixer.quit()
                            self.Pygame.quit()
                            self.Os._exit(0)

            if (55 < mouse_pos[0] < 155) and (424 < mouse_pos[1] < 464):
                self.Pygame.draw.rect(screen, self.blue, self.Pygame.Rect(55, 424, 100, 40))
                self.Drawing_Text(screen, 63, 426, "HOME", "times", 30, self.black)
            if (357 < mouse_pos[0] < 457) and (424 < mouse_pos[1] < 464):
                self.Pygame.draw.rect(screen, self.red, self.Pygame.Rect(357, 424, 100, 40))
                self.Drawing_Text(screen, 372, 426, "QUIT", "times", 30, self.black)
            self.Pygame.display.flip()
            self.clock.tick(600)

        new_instance = Master_minds()
        new_instance.Master_Minds()


    def Master_Minds(self):
        """
        This is the main game function
        :return: Nothing
        """
        import time

        total_hands = 10
        y_limit_hint = 508
        y_limit_block = 508 - 50
        screen = self.Create_Window(500, 600, self.background_color, "Master_Minds")
        # Displaying the home page
        self.Home_page_maker(screen)

        current_hand_num = self.Next_game_Iteration()
        ch = current_hand_num.__next__()
        # Resricting_Area = Next_Restrict_Area()
        Hint_Draw_Position = self.Hint_Draw_Positions()
        curr_HDP = Hint_Draw_Position.__next__()
        Ball_Draw_Position = self.Ball_Draw_Positions()
        curr_BDP = Ball_Draw_Position.__next__()

        pos = 0

        Decision_sequence = []
        Main_Block_sequence = []

        # Where to draw hints
        Hint_Draw_Sequence = [curr_HDP]
        # Where to draw balls
        Ball_Draw_Sequence = [curr_BDP]

        # Initialising main block sequence with all -1
        for i in range(total_hands):
            Main_Block_sequence.append([-1, -1, -1, -1])

        choosen_quad = [-1, -1, -1, -1]
        # only one quad for a game to be guessed
        current_quad = self.random_quad_generator(1, 8)

        # stack for storing the last modified values
        store = []
        flag = True

        self.Pygame.mixer.music.load("Sounds/Rainbow_Forest.mp3")
        self.Pygame.mixer.music.play(-1)

        self.gameLoop = True
        while self.gameLoop:
            stat = False
            mouse_pos = self.Pygame.mouse.get_pos()

            screen.fill(self.background_color)

            self.reDraw_window(screen, self.background_color, self.line_color, self.block_color, self.Highlighting_color, ch, Hint_Draw_Sequence,
                          Ball_Draw_Sequence, y_limit_hint, y_limit_block, Decision_sequence, Main_Block_sequence)
            if not flag:
                self.Pygame.mixer.music.stop()
                self.GAME_LOOSE_PAGE(screen, current_quad)

            for event in self.Pygame.event.get():
                if event.type == self.Pygame.QUIT:
                    self.Pygame.mixer.music.pause()
                    self.ARE_YOU_SURE(screen)
                    self.Pygame.mixer.music.unpause()
                if event.type == self.Pygame.KEYDOWN:
                    key_pressed = self.Pygame.key.get_pressed()
                    if key_pressed[self.Pygame.K_DELETE] == True:
                        try:
                            for k in range(3, -1, -1):
                                if Main_Block_sequence[ch][k] != -1:
                                    store.append(Main_Block_sequence[ch][k])
                                    Main_Block_sequence[ch][k] = -1
                                    if pos > 0:
                                        pos -= 1
                                    self.clock.tick(60)
                                    break
                        except IndexError:
                            pass

                    if key_pressed[self.Pygame.K_INSERT] == True:
                        try:
                            for k in range(0, 4):
                                if Main_Block_sequence[ch][k] == -1:
                                    Main_Block_sequence[ch][k] = store.pop()
                                    if pos < 3:
                                        pos += 1
                                        self.clock.tick(60)
                                    break
                        except IndexError:
                            pass

                if event.type == self.Pygame.MOUSEBUTTONDOWN:
                    if 49 < mouse_pos[0] < 99 and 532 < mouse_pos[1] < 580:
                        self.Pygame.draw.rect(screen, self.white, self.Pygame.Rect(49 + 2, 530 + 2, 48, 48))
                        screen.blit(self.Large_Spheres[0], (50, 532 + 2))
                        if self.Pygame.mouse.get_pressed()[0] == True:
                            screen.blit(self.Large_Spheres[0], Ball_Draw_Sequence[ch][pos])
                            if choosen_quad[pos] == -1:
                                choosen_quad[pos] = 1
                                stat = True
                                Main_Block_sequence[ch] = choosen_quad

                    elif 99 < mouse_pos[0] < 149 and 532 < mouse_pos[1] < 580:
                        self.Pygame.draw.rect(screen, self.white, self.Pygame.Rect(99 + 2, 530 + 2, 48, 48))
                        screen.blit(self.Large_Spheres[1], (100, 532 + 2))
                        if self.Pygame.mouse.get_pressed()[0] == True:
                            screen.blit(self.Large_Spheres[1], Ball_Draw_Sequence[ch][pos])
                            if choosen_quad[pos] == -1:
                                choosen_quad[pos] = 2
                                stat = True
                                Main_Block_sequence[ch] = choosen_quad

                    elif 149 < mouse_pos[0] < 199 and 532 < mouse_pos[1] < 580:
                        self.Pygame.draw.rect(screen, self.white, self.Pygame.Rect(149 + 2, 530 + 2, 48, 48))
                        screen.blit(self.Large_Spheres[2], (150, 532 + 2))
                        if self.Pygame.mouse.get_pressed()[0] == True:
                            screen.blit(self.Large_Spheres[2], Ball_Draw_Sequence[ch][pos])
                            if choosen_quad[pos] == -1:
                                choosen_quad[pos] = 3
                                stat = True
                                Main_Block_sequence[ch] = choosen_quad

                    elif 199 < mouse_pos[0] < 249 and 532 < mouse_pos[1] < 580:
                        self.Pygame.draw.rect(screen, self.white, self.Pygame.Rect(199 + 2, 530 + 2, 48, 48))
                        screen.blit(self.Large_Spheres[3], (200, 532 + 2))
                        if self.Pygame.mouse.get_pressed()[0] == True:
                            screen.blit(self.Large_Spheres[3], Ball_Draw_Sequence[ch][pos])
                            if choosen_quad[pos] == -1:
                                choosen_quad[pos] = 4
                                stat = True
                                Main_Block_sequence[ch] = choosen_quad

                    elif 249 < mouse_pos[0] < 299 and 532 < mouse_pos[1] < 580:
                        self.Pygame.draw.rect(screen, self.white, self.Pygame.Rect(249 + 2, 530 + 2, 48, 48))
                        screen.blit(self.Large_Spheres[4], (250, 532 + 2))
                        if self.Pygame.mouse.get_pressed()[0] == True:
                            screen.blit(self.Large_Spheres[4], Ball_Draw_Sequence[ch][pos])
                            if choosen_quad[pos] == -1:
                                choosen_quad[pos] = 5
                                stat = True
                                Main_Block_sequence[ch] = choosen_quad
                                self.Pygame.mouse.get_rel()

                    elif 299 < mouse_pos[0] < 349 and 532 < mouse_pos[1] < 580:
                        self.Pygame.draw.rect(screen, self.white, self.Pygame.Rect(299 + 2, 530 + 2, 48, 48))
                        screen.blit(self.Large_Spheres[5], (300, 532 + 2))
                        if self.Pygame.mouse.get_pressed()[0] == True:
                            screen.blit(self.Large_Spheres[5], Ball_Draw_Sequence[ch][pos])
                            if choosen_quad[pos] == -1:
                                choosen_quad[pos] = 6
                                stat = True
                                Main_Block_sequence[ch] = choosen_quad

                    elif 349 < mouse_pos[0] < 399 and 532 < mouse_pos[1] < 580:
                        self.Pygame.draw.rect(screen, self.white, self.Pygame.Rect(349 + 2, 530 + 2, 48, 48))
                        screen.blit(self.Large_Spheres[6], (350, 532 + 2))
                        if self.Pygame.mouse.get_pressed()[0] == True:
                            screen.blit(self.Large_Spheres[6], Ball_Draw_Sequence[ch][pos])
                            if choosen_quad[pos] == -1:
                                choosen_quad[pos] = 7
                                stat = True
                                Main_Block_sequence[ch] = choosen_quad

                    elif 399 < mouse_pos[0] < 449 and 532 < mouse_pos[1] < 580:
                        self.Pygame.draw.rect(screen, self.white, self.Pygame.Rect(399 + 2, 530 + 2, 48, 48))
                        screen.blit(self.Large_Spheres[7], (400, 532 + 2))
                        if self.Pygame.mouse.get_pressed()[0] == True:
                            screen.blit(self.Large_Spheres[7], Ball_Draw_Sequence[ch][pos])
                            if choosen_quad[pos] == -1:
                                choosen_quad[pos] = 8
                                stat = True
                                Main_Block_sequence[ch] = choosen_quad
                    else:
                        pass

            if 49 < mouse_pos[0] < 99 and 532 < mouse_pos[1] < 580:
                self.Pygame.draw.rect(screen, self.Highlighting_color, self.Pygame.Rect(49 + 2, 530 + 2, 48, 48))
                screen.blit(self.Large_Spheres[0], (50, 532 + 2))

            elif 99 < mouse_pos[0] < 149 and 532 < mouse_pos[1] < 580:
                self.Pygame.draw.rect(screen, self.white, self.Pygame.Rect(99 + 2, 530 + 2, 48, 48))
                screen.blit(self.Large_Spheres[1], (100, 532 + 2))

            elif 149 < mouse_pos[0] < 199 and 532 < mouse_pos[1] < 580:
                self.Pygame.draw.rect(screen, self.white, self.Pygame.Rect(149 + 2, 530 + 2, 48, 48))
                screen.blit(self.Large_Spheres[2], (150, 532 + 2))

            elif 199 < mouse_pos[0] < 249 and 532 < mouse_pos[1] < 580:
                self.Pygame.draw.rect(screen, self.white, self.Pygame.Rect(199 + 2, 530 + 2, 48, 48))
                screen.blit(self.Large_Spheres[3], (200, 532 + 2))

            elif 249 < mouse_pos[0] < 299 and 532 < mouse_pos[1] < 580:
                self.Pygame.draw.rect(screen, self.white, self.Pygame.Rect(249 + 2, 530 + 2, 48, 48))
                screen.blit(self.Large_Spheres[4], (250, 532 + 2))

            elif 299 < mouse_pos[0] < 349 and 532 < mouse_pos[1] < 580:
                self.Pygame.draw.rect(screen, self.white, self.Pygame.Rect(299 + 2, 530 + 2, 48, 48))
                screen.blit(self.Large_Spheres[5], (300, 532 + 2))

            elif 349 < mouse_pos[0] < 399 and 532 < mouse_pos[1] < 580:
                self.Pygame.draw.rect(screen, self.white, self.Pygame.Rect(349 + 2, 530 + 2, 48, 48))
                screen.blit(self.Large_Spheres[6], (350, 532 + 2))

            elif 399 < mouse_pos[0] < 449 and 532 < mouse_pos[1] < 580:
                self.Pygame.draw.rect(screen, self.white, self.Pygame.Rect(399 + 2, 530 + 2, 48, 48))
                screen.blit(self.Large_Spheres[7], (400, 532 + 2))

            else:
                pass

            if stat == True:
                pos += 1
                if pos > 3:
                    pos = 0

            Result = self.check_Choosen_quad_stat(choosen_quad)
            if Result == True:
                if (self.check_game_end(current_quad, choosen_quad)):
                    print(current_quad)
                    self.Pygame.mixer.music.stop()
                    self.GAME_WIN_PAGE(screen, ch + 1, current_quad)
                store = []
                Decision = self.compare_quads(choosen_quad, current_quad)
                Decision_sequence.append(Decision)
                ch = current_hand_num.__next__()
                curr_HDP = Hint_Draw_Position.__next__()
                curr_BDP = Ball_Draw_Position.__next__()
                Hint_Draw_Sequence.append(curr_HDP)
                Ball_Draw_Sequence.append(curr_BDP)
                choosen_quad = [-1, -1, -1, -1]
                y_limit_hint -= 50
                if ch != 10:
                    y_limit_block -= 50

            if ch == 10:
                flag = False
            self.Pygame.display.flip()
            self.clock.tick(600)


if __name__ == "__main__":
    m = Master_minds()
    m.Master_Minds()
