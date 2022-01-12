import pgzrun
import pyautogui
from random import randint

HEIGHT = 600
WIDTH = 600

tank = Actor("tank_blue")
tank.x = WIDTH/2
tank.bottom = HEIGHT
tank.angle = 90
walls = []
bullets=[]
enemybullets=[]
enemies = []
score = 0
hp = 0
speed = 5
bulletspeed = 5
Wall = "False"
Gameover = False
flag = True

reds = []
darks = []
greens = []
sands = []

Click = Actor("mouse")

def create_red():
    enemyred = Actor("tank_red")
    enemyred.x = randint(100,WIDTH-100)
    enemyred.y = 10
    enemyred.angle = -90
    enemies.append(enemyred)
    reds.append(enemyred)

def create_green():
    enemygreen = Actor("tank_green")
    enemygreen.x = randint(100,WIDTH-100)
    enemygreen.y = 75
    enemygreen.angle = -90
    enemies.append(enemygreen)
    greens.append(enemygreen)

def create_dark():
    enemydark = Actor("tank_dark")
    enemydark.x = randint(100,WIDTH-100)
    enemydark.y = 115
    enemydark.angle = -90
    enemies.append(enemydark)
    darks.append(enemydark)

def create_sand():
    enemysand = Actor("tank_sand")
    enemysand.x = randint(100,WIDTH-200)
    enemysand.y = 175
    enemysand.angle = -90
    enemies.append(enemysand)
    sands.append(enemysand)

time = 1

item1 = Actor("wheel")
item2 = Actor("weapon")
item3 = Actor("hp")
item4 = Actor("bigwall")
item5 = Actor("steel(2)")

with open ("Highscore.txt","r") as file:
    firstline = file.readlines()
    print(firstline)
    if len(firstline) == 0:
        highscore = 0
        with open("Highscore.txt","a") as file:
             file.write("Highscore : 00")
             file.write("")
    else:
        temp = firstline[0][12:13]
        highscore = int(temp)
    print(highscore)

with open("HP.txt","r") as file2:
    secondline = file2.readlines()
    print(len(secondline))
    if len(secondline)== 0:
        with open("HP.txt","a") as file2:
            file2.write("HP : 1")
            file2.write("\n")
    else:
        temp = secondline[0][5:7]
        print("TEMP : "+ temp)
        hp = int(temp)

with open("Speed.txt","r") as file3:
    thirdline = file3.readlines()
    print(len(thirdline))
    if len(thirdline)== 0:
        with open("Speed.txt","a") as file3:
            file3.write("Speed : 5")
            file3.write("\n")
    else:
        temp = thirdline[0][8:9]
        print("TEMP : "+ temp)
        speed = int(temp)

with open("Bullet.txt","r") as file4:
    fourthline = file4.readlines()
    print(len(fourthline))
    if len(fourthline)== 0:
        with open("Bullet.txt","a") as file4:
            file4.write("Speed : 5")
            file4.write("\n")
    else:
        temp = fourthline[0][8:9]
        print("TEMP : "+ temp)
        bulletspeed = int(temp)

with open("Wall.txt","r") as file5:
    fifthline = file5.readlines()
    print(len(fifthline))
    if len(fifthline)== 0:
        with open("Wall.txt","a") as file5:
            file5.write("False")
            file5.write("\n")
    else:
        temp = fifthline[0][0:5]
        print("TEMP : "+ temp)
        Wall = "True"

def update_time_left():
    global time,gameover
    if time:
        time += 1
    if time % 3 == 0:
        create_dark()
        create_green()
        create_dark()
        create_sand()

def on_mouse_move(pos):
    Click.pos = pos

def on_mouse_down():
    if Gameover == True:
        if Click.colliderect(item1):
            if highscore >= 3:
                fin = open("Speed.txt", "rt")
                data = fin.read()
                data = data.replace("5","7")
                fin.close()
                fin = open("Speed.txt", "wt")
                fin.write(data)
                fin.close()
                print("Changed!")

        if Click.colliderect(item2):
            if highscore >= 3:
                fin = open("Bullet.txt", "rt")
                data = fin.read()
                data = data.replace("5","7")
                fin.close()
                fin = open("Bullet.txt", "wt")
                fin.write(data)
                fin.close()
                print("Changed!")

        if Click.colliderect(item3):
            if highscore >= 3:
                fin = open("HP.txt", "rt")
                data = fin.read()
                data = data.replace("1","3")
                fin.close()
                fin = open("HP.txt", "wt")
                fin.write(data)
                fin.close()
                print("Changed!")

        if Click.colliderect(item4):
            if highscore >= 3:
                fin = open("Wall.txt", "rt")
                data = fin.read()
                data = data.replace("False","True")
                fin.close()
                fin = open("Wall.txt", "wt")
                fin.write(data)
                fin.close()
                print("Changed!")

def draw():
    if Gameover == False:
        screen.clear()
        screen.blit("grass",(0,0))
        tank.draw()
        for wall in walls:
            wall.draw()
        for bullet in bullets:
            bullet.draw()
        for enemy in enemies:
            enemy.draw()
        for enemybullet in enemybullets:
            enemybullet.draw()
        screen.draw.text("Score : "+str(score),(450,50),fontsize = 35)
        screen.draw.text("Your overall highscore is : "+ str(highscore),(300,20),fontsize = 30, color="blue")
        screen.draw.text("HP : "+str(hp),(20,10),fontsize=30,color="blue")
        screen.draw.text("Seconds you survived : " + str(time), (5,50),fontsize = 30, color = "blue")

    else:        
        ShopScreen()
        global flag
        if flag:
            with open("Highscore.txt","a+") as file:
                prevhighscore = int(firstline[0][12:14])
                if prevhighscore < score:
                    fin = open("Highscore.txt", "rt")
                    data = fin.read()
                    data = data.replace(str(prevhighscore), str(score))
                    fin.close()
                    fin = open("Highscore.txt", "wt")
                    fin.write(data)
                    fin.close()
        flag = False

def update():
    global originalX, originalY
    originalX = tank.x
    originalY = tank.y
    move_tank()
    check_player_boundaries()
    #check_player_collision()
    check_bullet_collision()
    move_bullet()
    move_enemy_bullet()

def move_tank():
    if keyboard.left:
        tank.x -= speed
        tank.angle = -180
    elif keyboard.right:
        tank.x += speed
        tank.angle = 360
    elif keyboard.up:
        tank.y -= speed
        tank.angle = 90
    elif keyboard.down:
        tank.y += speed
        tank.angle = -90

def move_bullet():
    for bullet in bullets:
        if bullet.angle == -180:
            bullet.x -= 5
        elif bullet.angle == 360:
            bullet.x += 5
        elif bullet.angle == 90:
            bullet.y -= 5
        elif bullet.angle == -90:
            bullet.y += 5     

def move_enemy_bullet():
    for enemybullet in enemybullets:
        if enemybullet.angle == -180:
            enemybullet.x -= 5
        elif enemybullet.angle == 360:
            enemybullet.x += 5
        elif enemybullet.angle == 90:
            enemybullet.y -= 5
        elif enemybullet.angle == -90:
            enemybullet.y += 5

def check_player_boundaries():
    if tank.right > WIDTH:
        tank.right = WIDTH
    elif tank.left < 0:
        tank.left = 0
    if tank.top < 0:
        tank.top = 0
    elif tank.bottom > HEIGHT:
        tank.bottom = HEIGHT

def create_new_wall():

    for i in range(15):
        for j in range(10):
            if randint(0,100) > 50:
                wall = Actor("wall")
                wall.topleft = (i * 70, j * 70)
                walls.append(wall)

def check_player_collision():
    for wall in walls:
        if wall.colliderect(tank):
            tank.x = originalX
            tank.y = originalY

def check_bullet_collision():
    global score
    for enemybullet in enemybullets:
        for wall in walls:
            if enemybullet.colliderect(wall):
                enemybullets.remove(enemybullet)
                walls.remove(wall)
    
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1

    for bullet in bullets:
        if bullet.bottom < 0:
            bullets.remove(bullet)

    for enemybullet in enemybullets:
        if enemybullet.colliderect(tank):
            enemybullets.remove(enemybullet)
            global hp,Gameover
            hp = hp - 1
            if hp == 0:
                tank.image = "explosion3"
                Gameover = True

    for enemybullet in enemybullets:
        if enemybullet.bottom < 0:
            enemybullets.remove(enemybullet)

def on_key_down():
    global Gameover
    if Gameover == False:
        if keyboard.space:
            create_new_bullet()
        if keyboard.k:
            create_red_bullet()
        if keyboard.l:
            create_dark_bullet()
        if keyboard.p:
            create_green_bullet()
        if keyboard.o:
            create_sand_bullet()
        if keyboard.h:
            Gameover==True
    else:
        if keyboard.u:
            Gameover==False

def create_new_bullet():  
    bullet = Actor("bulletblue2")
    bullet.pos = tank.pos
    bullet.angle = tank.angle
    bullets.append(bullet)

def create_red_bullet():
    redbullet = Actor("bulletred2")
    for i in reds:
        redbullet.pos = i.pos
        redbullet.angle = i.angle
        enemybullets.append(redbullet)

def create_green_bullet():

    greenbullet = Actor("bulletgreen2")
    for i in greens:
        greenbullet.pos = i.pos
        greenbullet.angle = i.angle
        enemybullets.append(greenbullet)

def create_dark_bullet():
    darkbullet = Actor("bulletdark2")
    for i in darks:
        darkbullet.pos = i.pos
        darkbullet.angle = i.angle
        enemybullets.append(darkbullet)

def create_sand_bullet():
    sandbullet = Actor("bulletsand2")
    for i in sands:
        sandbullet.pos = i.pos
        sandbullet.angle = i.angle
        enemybullets.append(sandbullet)

def ShopScreen():
        screen.blit("shop",(0,0))
        item1.pos = (100,200)
        item2.pos = (400,200)
        item3.pos = (100,400)
        item4.pos = (400,400)
        item1.draw()
        item2.draw()
        item3.draw()
        item4.draw()
        screen.draw.text("Shop Screen",(250,10),fontsize=30,color="white")
        screen.draw.text("Increases Tank Speed, Highscore required : 3", (10,120), fontsize = 25, color = "white")
        screen.draw.text("Increses Bullet Speed, Highscore required : 3", (180,280), fontsize = 25, color = "white")
        screen.draw.text("Increases hit points, Highscore required : 3", (50,500), fontsize = 25, color = "white")
        screen.draw.text("Creates Random walls, Highscore required : 3 ", (100,570), fontsize = 25, color = "white")    

enemyred = Actor("tank_red")
enemyred.x = randint(100,WIDTH-100)
enemyred.y = 10
enemyred.angle = -90
enemies.append(enemyred)

enemygreen = Actor("tank_green")
enemygreen.x = randint(100,WIDTH-100)
enemygreen.y = 75
enemygreen.angle = -90
enemies.append(enemygreen)

enemydark = Actor("tank_dark")
enemydark.x = randint(100,WIDTH-100)
enemydark.y = 115
enemydark.angle = -90
enemies.append(enemydark)

enemysand = Actor("tank_sand")
enemysand.x = randint(100,WIDTH-200)
enemysand.y = 175
enemysand.angle = -90
enemies.append(enemysand)

create_dark_bullet()
create_red_bullet()
create_green_bullet()
create_sand_bullet()

if Wall == "True":
    create_new_wall()
if Gameover == False:
    clock.schedule_interval(update_time_left,1.0)
    clock.schedule_interval(create_dark_bullet, 3.0)
    clock.schedule_interval(create_sand_bullet, 3.0)
    clock.schedule_interval(create_green_bullet, 3.0)
    clock.schedule_interval(create_red_bullet, 3.0)


pgzrun.go()