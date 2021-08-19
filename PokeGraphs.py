# Israel Méndez Crespo
# Scripting Languages
# COP 2830C Section 31462
# Project: Submit Graphic Loops

# Pókemon Graphics in Python
# Scenario project: This project stems from the first projects
# on the scenario prompts. However, this is much more a module
# of what would be a graphical implementation of the game. There
# are many parts that are not included in this module to simplify
# the development and demostrate the basic functionality that would
# be added from the module to the program. It uses various graphic
# techniques that are a part of the graphics module section of the
# course.

import random
import winsound

from graphics import *

# Create a window to play game with title and size as attributes

win = GraphWin("Poke Python", 1024, 576)


# Create a background with lines similar to GBA Pokemon games
# The lines start becoming lighter as they approach the center of
# the screen but stop before becoming lighter than RGB(175,175,175)

def draw_bg():
    for i in range(0, 5):
        bg_line = Rectangle(Point(0, (i * 25)), Point(win.getWidth(), (i + 1) * 25))
        bg_line.setFill(color_rgb(90 + (i * 15), 90 + (i * 15), 90 + (i * 15)))
        bg_line.draw(win)
        time.sleep(.1)

    for i in range(5, 25):
        bg_line = Rectangle(Point(0, (i * 25)), Point(win.getWidth(), (i + 1) * 25))
        bg_line.setFill(color_rgb(175, 175, 175))
        bg_line.draw(win)
        time.sleep(.1)


# Draws the battle Pokemon and animates then on screen.
# The start coordinates are used for the opponent position.
# There is an oval that represents the floor where the
# Pokemon is standing which uses the stand_start variables

def draw_battle():
    start_coord = Point(win.getWidth() + 150,
                        win.getHeight() - 450)
    stand_start1 = Point(1025, 175)
    stand_start2 = Point(1325, 275)

    opponentStand = Oval(stand_start1, stand_start2)
    opponentStand.setFill('gray')
    opponentStand.setOutline('red')
    opponentStand.setWidth(3)
    opponentStand.draw(win)

    myCorner1 = Point(-75, 350)
    myPokemon = Image(myCorner1, "backcharmander.gif")
    myPokemon.draw(win)

    # The proto variable is made to establish a list of
    # Polygon objects that will be used in the nested loops
    # below.

    proto = Polygon()
    tiles = [proto]

    # Creates floor tiles similar to GBA Pokemon battle scenes
    # https://www.spriters-resource.com/resources/sheets/8/8303.png?updated=1460953806

    for i in range(5):
        for j in range(4):
            tPoint1 = Point(1125 + (i * 25), 185 + (j * 20))
            tPoint2 = Point(1150 + (i * 25), 185 + (j * 20))
            tPoint3 = Point(1140 + (i * 25), 205 + (j * 20))
            tPoint4 = Point(1115 + (i * 25), 205 + (j * 20))

            vertices = [tPoint1, tPoint2, tPoint3, tPoint4]

            # The random function is used to specify a range for various
            # shades of gray to used for the tile sets.

            r = random.randrange(125, 175)

            tile = Polygon(vertices)
            tile.setFill(color_rgb(r, r, r))
            tile.draw(win)
            tiles.append(tile)

    charmander = Image(start_coord, "charmander.gif")
    charmander.draw(win)

    # Moves all the Pokemon images towards the screen at the same time
    # To move the group of tileset at the same time, a nested for loop
    # is used. Each iteration of the outer for loop will move all tiles
    # inside the tiles list one space to the left.

    for i in range(0, 27):
        charmander.move(-i, 0)
        opponentStand.move(-i, 0)
        myPokemon.move(i, 0)
        for x in range(len(tiles)):
            tiles[x].move(-i, 0)
        i += 1
        time.sleep(.03)


# Draws the battle menu text on screen. Upgrades would
# include entry object to make battle selections.

def draw_bm():
    box1 = Point(4, 400)
    box2 = Point(win.getWidth(), win.getHeight())

    box = Rectangle(box1, box2)
    box.setFill('white')
    box.setOutline('red')
    box.setWidth(3)
    box.draw(win)


# Uses a for loop to account for space needed for next
# letter. Monospaced letters would work best if available.

def prompt(message):
    for x in range(len(message)):
        corner = Point(25 + ((x + 1) * 25), 425)
        label = Text(corner, message[x])
        label.setFace("helvetica")
        label.setSize(26)
        label.draw(win)


# Demonstrates animation for flamethrower attack. Loops through
# a cycle of triangles that overlap and change colors.

# Each Polygon is drawn in its starting location and then moved
# through the use of a for loop. Color iteration is decided by
# a use of the modulus operator which will make each other iteration
# a different fill and outline color.

def flamethrower():
    firePolygon1 = Polygon(Point(350, 320), Point(380, 270), Point(400, 320))
    firePolygon1.setOutline('yellow')
    firePolygon1.setWidth(3)
    firePolygon1.setFill('red')
    firePolygon1.draw(win)

    firePolygon2 = Polygon(Point(360, 317), Point(390, 267), Point(410, 317))
    firePolygon2.setOutline('red')
    firePolygon2.setWidth(3)
    firePolygon2.setFill('yellow')
    firePolygon2.draw(win)

    firePolygon3 = Polygon(Point(370, 315), Point(400, 263), Point(420, 313))
    firePolygon3.setOutline('yellow')
    firePolygon3.setWidth(3)
    firePolygon3.setFill('red')
    firePolygon3.draw(win)

    # For loop will iterate 20 cycles between outline and fill colors
    # which illustrates an alternating sequence.

    for i in range(20):

        if i % 2 == 0:
            firePolygon1.setFill('red')
            firePolygon1.setOutline('yellow')

            firePolygon2.setFill('yellow')
            firePolygon2.setOutline('red')

            firePolygon3.setFill('red')
            firePolygon3.setOutline('yellow')

        else:
            firePolygon1.setFill('yellow')
            firePolygon1.setOutline('red')

            firePolygon2.setFill('red')
            firePolygon2.setOutline('yellow')

            firePolygon3.setFill('yellow')
            firePolygon3.setOutline('red')

        firePolygon1.move(i * 2, -i)
        firePolygon2.move(i * 2, -i)
        firePolygon3.move(i * 2, -i)
        time.sleep(0.1)

    firePolygon1.setOutline('white')
    firePolygon1.setFill('white')

    firePolygon2.setOutline('white')
    firePolygon2.setFill('white')

    firePolygon3.setOutline('white')
    firePolygon3.setFill('white')


# Creates a circular fill effect to be used after the
# opposing Pokemon is knocked out. It uses a for loop
# to increase circle radius.

def white_screen():
    for i in range(150):
        screenFill = Circle(Point(800, 100), i * 7)
        screenFill.setFill('white')
        screenFill.draw(win)


# Creates boxes for each Pokemon with their names or
# nicknames, health bar, and health points. Upgrades
# would include an iterative draw cycle to portray the
# effect of a health bar lowering.

def draw_ui():
    my_status_box = Rectangle(Point(700, 300), Point(1050, 400))
    my_status_box.setFill(color_rgb(240, 239, 208))
    my_status_box.draw(win)

    for x in range(len('Charmy')):
        corner = Point(705 + ((x + 1) * 25), 325)
        label = Text(corner, 'Charmy'[x])
        label.setFace("helvetica")
        label.setSize(26)
        label.draw(win)

    my_health_bar = Rectangle(Point(720, 350), Point(1000, 360))
    my_health_bar.setFill('green')
    my_health_bar.draw(win)

    for x in range(len('HP 31 / 31')):
        corner = Point(705 + ((x + 1) * 25), 385)
        label = Text(corner, 'HP 31 / 31'[x])
        label.setFace("helvetica")
        label.setStyle("bold italic")
        label.setSize(22)
        label.draw(win)

    opponent_status_box = Rectangle(Point(0, 0), Point(350, 100))
    opponent_status_box.setFill(color_rgb(240, 239, 208))
    opponent_status_box.draw(win)

    for x in range(len('Charmander')):
        corner = Point(5 + ((x + 1) * 25), 25)
        label = Text(corner, 'Charmander'[x])
        label.setFace("helvetica")
        label.setSize(26)
        label.draw(win)

    opponent_health_bar = Rectangle(Point(20, 50), Point(300, 60))
    opponent_health_bar.setFill('green')
    opponent_health_bar.draw(win)

    for x in range(len('HP 36 / 36')):
        corner = Point(5 + ((x + 1) * 25), 85)
        label = Text(corner, 'HP 36 / 36'[x])
        label.setFace("helvetica")
        label.setStyle("bold italic")
        label.setSize(22)
        label.draw(win)


# Main function calls other functions to display the battle graphics

def main():
    winsound.PlaySound("battle", winsound.SND_FILENAME | winsound.SND_ASYNC)
    draw_bg()
    draw_battle()
    draw_ui()

    draw_bm()
    prompt("Wild Charmander appears!")
    win.getMouse()

    draw_bm()
    prompt("1. Fight 2. Item 3. PKMN 4. Run")
    win.getMouse()

    draw_bm()
    prompt("1.Scratch 2.Flamethrower")
    win.getMouse()

    draw_bm()
    prompt("Charmander uses Flamethrower!")
    win.getMouse()

    flamethrower()
    white_screen()

    win.getMouse()


main()

