# Python-Pokemon
 Miniature Pokemon game utilizing Python and ASCII art.

The graphic techniques used for this representation include:

The use of a for loop that iterates trough a rectangles that make up the deepest background layer. The upper part of the background starts at the darkest hue and becomes lighter until about 3 / 8ths of the screen where the color is at its lightest and stays the same.

Another for loops controls the animation where both Pokemon appear on the screen by sliding on the x axis. The animation moves three main parts of graphics.

1. It moves the images of the Pokemon which are gifs of the front and back of Charmander.

2. It moves an oval which represents the ground the opponent Pokemon is standing in.

3. It moves a tileset that is created before the animation comes in. 

The tileset is made of nested for loops which allow for easier creation of grid type layout shapes. The creation of the tileset also includes the use of the random function with narrow parameters in order to produce shades of gray that are similar in hue to the background.

The animation of the flamethrower attack is made using a for loop iteration of triangles which alternate their colors as they move towards the target. The movement makes use of translation techniques to edit the course of the "flames"  towards the targets.

Text generation is also used in for loops in order to maintain a somewhat left-bearing text generator. When a text is to be outputted on the screen, the iteration will account for the change in coordinates so that staying on the center is not so much a concern.

Lastly, the final animation will take up the whole screen as if it caused an explosion and also as a transition effect to what would be the next part of the program should the program end.

Needless to say, there is much to be added to this program so it can become a fully compatible module to the previous ASCII miniature Pokemon game, but it demonstrates the basic functionality that would offer should it be ever fully linked to the simpler game.
