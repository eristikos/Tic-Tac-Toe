import pygame
pygame.init()
win = pygame.display.set_mode((600,600))
win.fill((0,0,0))
pygame.display.set_caption('Tic Tac Toe')
WHITE=(255,255,255)
run = True
draw_object = 'x'


cross = pygame.transform.smoothscale(pygame.image.load(r'C:\python_projects\my_projects\tic-tac-toe\cross.png').convert(), (180,180))
ooo = pygame.transform.smoothscale(pygame.image.load(r'C:\python_projects\my_projects\tic-tac-toe\ooo.png').convert(), (180,180))

def command1():
    print("wygrales X \n"*50)



def command2():
    print("wygrales O \n"*50)


class Field(object):
    instancelist = []
    circleFields = []
    crossFields = []

    def __init__(self, x, y, width, height, clicked):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.clicked = clicked
        Field.instancelist.append(self)


    def drawrect(self):
         pygame.draw.rect(win,WHITE,[self.x, self.y, self.width, self.height])

    def test(self):
        if pos[0] in range (self.x, self.width+self.x) and pos[1] in range (self.y, self.height+self.y) and self.clicked==False:
            global draw_object
            if draw_object == 'x':
                win.blit(cross, (self.x, self.y))
                Field.crossFields.append(Field.instancelist.index(self)+1)
                print("pola Xowe: ", Field.crossFields)
                draw_object = 'o'


            elif draw_object =='o':
                win.blit(ooo, (self.x, self.y))
                Field.circleFields.append(Field.instancelist.index(self)+1)
                print("pola kolkowe: ", Field.circleFields)
                draw_object = 'x'

            self.clicked=True
        else:
            pass

    def test2(self):
        if pos[0] in range (self.x, self.width+self.x) and pos[1] in range (self.y, self.height+self.y):
            print("field",(Field.instancelist.index(self)+1))



field1 = Field(15,15,180,180, False,)
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
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos[0], pos[1])
            for instance in Field.instancelist:
                instance.test()
                instance.test2()

        if 1 in Field.crossFields and 2 in Field.crossFields and 3 in Field.crossFields:
            command1()
            continue
        elif 1 in Field.circleFields and 2 in Field.circleFields and 3 in Field.circleFields:
            command2()
            continue
        elif 4 in Field.crossFields and 5 in Field.crossFields and 6 in Field.crossFields:
            command1()
            continue
        elif 4 in Field.circleFields and 5 in Field.circleFields and 6 in Field.circleFields:
            command2()
            continue
        elif 7 in Field.crossFields and 8 in Field.crossFields and 9 in Field.crossFields:
            command1()
            continue
        elif 7 in Field.circleFields and 8 in Field.circleFields and 9 in Field.circleFields:
            command2()
            continue
        elif 1 in Field.crossFields and 4 in Field.crossFields and 7 in Field.crossFields:
            command1()
            continue
        elif 1 in Field.circleFields and 4 in Field.circleFields and 7 in Field.circleFields:
            command2()
            continue
        elif 1 in Field.crossFields and 5 in Field.crossFields and 9 in Field.crossFields:
            command1()
            continue
        elif 1 in Field.circleFields and 5 in Field.circleFields and 9 in Field.circleFields:
            command2()
            continue
        elif 3 in Field.crossFields and 5 in Field.crossFields and 7 in Field.crossFields:
            command1()
            continue
        elif 3 in Field.circleFields and 5 in Field.circleFields and 7 in Field.circleFields:
            command2()
            continue
        elif 2 in Field.crossFields and 5 in Field.crossFields and 8 in Field.crossFields:
            command1()
            continue
        elif 2 in Field.circleFields and 5 in Field.circleFields and 8 in Field.circleFields:
            command2()
            continue
        elif 3 in Field.crossFields and 6 in Field.crossFields and 9 in Field.crossFields:
            command1()
            continue
        elif 3 in Field.circleFields and 6 in Field.circleFields and 9 in Field.circleFields:
            command2()
            continue
        else:
            pass







    pygame.display.update()
