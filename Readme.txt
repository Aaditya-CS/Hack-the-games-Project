TEAM ABSTRACT GAME SUBMISSION
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
TEAM MEMBERS :

1. Aaditya CS (f53c02c5)
2. Jessica R (90756f02)

THE GAME AND IT'S FEATURES :

1. The game involves you, the player (blue tank), who has to shoot down the enemy tanks (red tank, black tank, sandy tank, green tank).
2. The gameplay revolves around securing the highest possible highscore, and surviving for a long time.
3. The game also includes a shop menu which can be accessed once the player is eliminated, to improve various stats of the player.
4. The game has been automated with the help of template matching, so the game plays by itself to secure a high score.

PREREQUSITES FOR RUNNING THE PROGRAM :

1. PGZERO (can be installed with "pip install pgzero" in command prompt). The whole game is based on this module.
2. CV2, Numpy,Matplotlib (used to run template matching on sample images)
3. Pyautogui (used to automatically take screenshots at regular intervals)
4. Random function (used to create elements of chance within the game)
5. 5 empty text files in the same directory ("Highscore.txt", "HP.txt", "Speed.txt", "Bullet.txt","Wall.txt"). These are required for the shop function to work.
6. All the images attached with the program extracted in the same directory as the program.

EXPLANATION OF THE WORKING CODE :

1. The player, and the enemy tanks are spawned in the beginning of the game with the help of "Actors" from the pgzero module.
2. The highscore, HP, Speed, Bullet, Wall values from the respective files are read and updated in the current instance of the game.
3. A timer begins, counting the time elapsed since the start.
4. If the timer reaches a multiple of 3, new enemies are spawned.
5. At the same time, a screenshot is taken and template matching is run, with the template images as the four enemy images (green,red,dark,sand tanks).
6. The start and end values of the x-axis of the matched images are taken, and the midpoint is calculated.
7. The player is moved to the midpoint of the closest matched enemy, and shoots bullets.
8. If the player gets eliminated, the various values of the text files (Highscore, HP, Bullet, Wall, Speed) are updated in the respective files.
9. A shop screen opens, allowing the player to get different upgrades, so that they may secure a higher score the next time they run the game.

----------------------------------------------------------------------------------------------------------------------------------------------------------------
THANKS FOR READING!