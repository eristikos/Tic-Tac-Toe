import pygame
pygame.init()
win = pygame.display.set_mode((600,600))
win.fill((0,0,0))
pygame.display.set_caption('Tic Tac Toe')
WHITE=(255,255,255)

cross = pygame.transform.smoothscale(pygame.image.load(r'C:\python_projects\my_projects\tic-tac-toe\cross.png').convert(), (180,180))
ooo = pygame.transform.smoothscale(pygame.image.load(r'C:\python_projects\my_projects\tic-tac-toe\ooo.png').convert(), (180,180))

class Field(object):
    instancelist = []
    def __init__(self, x, y, width, height, clicked):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.clicked = clicked
        Field.instancelist.append(self)
    def drawrect(self):
         pygame.draw.rect(win,WHITE,[self.x, self.y, self.width, self.height])

field1 = Field(15,15,180,180, False)
field2 = Field(210,15,180,180, False)
field3 = Field(405,15,180,180, False)
field4 = Field(15,210,180,180,False)
field5 = Field(210,210,180,180, False)
field6 = Field(405,210,180,180, False)
field7 = Field(15,405,180,180, False)
field8 = Field(210,405,180,180, False)
field9 = Field(405,405,180,180, False)

for instance in Field.instancelist:
    instance.drawrect()

###############################################################################
run = True
draw_object = 'x'
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos[0], pos[1])
            if pos[0] in range (field1.x, field1.width+field1.x) and pos[1] in range (field1.y, field1.height+field1.y) and field1.clicked==False:
                print("field1")
                if draw_object == 'x':
                    win.blit(cross, (field1.x, field1.y))
                    draw_object = 'o'
                else:
                    win.blit(ooo, (field1.x, field1.y))
                    draw_object = 'x'
                field1.clicked=True

            elif pos[0] in range (field2.x, field2.width+field2.x) and pos[1] in range (field2.y, field2.height+field2.y) and field2.clicked==False:
                print("field2")
                if draw_object == 'x':
                    win.blit(cross, (field2.x, field2.y))
                    draw_object = 'o'
                else:
                    win.blit(ooo, (field2.x, field2.y))
                    draw_object = 'x'
                field2.clicked=True

            elif pos[0] in range (field3.x, field3.width+field3.x) and pos[1] in range (field3.y, field3.height+field3.y) and field3.clicked==False:
                print("field3")
                if draw_object == 'x':
                    win.blit(cross, (field3.x, field3.y))
                    draw_object = 'o'
                else:
                    win.blit(ooo, (field3.x, field3.y))
                    draw_object = 'x'
                field3.clicked=True

            elif pos[0] in range (field4.x, field4.width+field4.x) and pos[1] in range (field4.y, field4.height+field4.y) and field4.clicked==False:
                print("field4")
                if draw_object == 'x':
                    win.blit(cross, (field4.x, field4.y))
                    draw_object = 'o'
                else:
                    win.blit(ooo, (field4.x, field4.y))
                    draw_object = 'x'
                field4.clicked=True

            elif pos[0] in range (field5.x, field5.width+field5.x) and pos[1] in range (field5.y, field5.height+field5.y) and field5.clicked == False:
                print("field5")
                if draw_object == 'x':
                    win.blit(cross, (field5.x, field5.y))
                    draw_object = 'o'
                else:
                    win.blit(ooo, (field5.x, field5.y))
                    draw_object = 'x'
                field5.clicked=True

            elif pos[0] in range (field6.x, field6.width+field6.x) and pos[1] in range (field6.y, field6.height+field6.y) and field6.clicked == False:
                print("field6")
                if draw_object == 'x':
                    win.blit(cross, (field6.x, field6.y))
                    draw_object = 'o'
                else:
                    win.blit(ooo, (field6.x, field6.y))
                    draw_object = 'x'
                field6.clicked=True

            elif pos[0] in range (field7.x, field7.width+field7.x) and pos[1] in range (field7.y, field7.height+field7.y) and field7.clicked == False:
                print("field7")
                if draw_object == 'x':
                    win.blit(cross, (field7.x, field7.y))
                    draw_object = 'o'
                else:
                    win.blit(ooo, (field7.x, field7.y))
                    draw_object = 'x'
                field7.clicked=True


            elif pos[0] in range (field8.x, field8.width+field8.x) and pos[1] in range (field8.y, field8.height+field8.y) and field8.clicked == False:
                print("field8")
                if draw_object == 'x':
                    win.blit(cross, (field8.x, field8.y))
                    draw_object = 'o'
                else:
                    win.blit(ooo, (field8.x, field8.y))
                    draw_object = 'x'
                field8.clicked=True

            elif pos[0] in range (field9.x, field9.width+field9.x) and pos[1] in range (field9.y, field9.height+field9.y) and field9.clicked == False:
                print("field9")
                if draw_object == 'x':
                    win.blit(cross, (field9.x, field9.y))
                    draw_object = 'o'
                else:
                    win.blit(ooo, (field9.x, field9.y))
                    draw_object = 'x'
                field9.clicked=True

            else:
                print("dzwig")

    pygame.display.update()
