'''
The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, or "populated" or "unpopulated".
Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent.
At each step in time, the following transitions occur:

******************************************************************************************************
   1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
   2. Any live cell with two or three live neighbours lives on to the next generation.
   3. Any live cell with more than three live neighbours dies, as if by overpopulation.
   4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
*******************************************************************************************************

The initial pattern constitutes the seed of the system.

The first generation is created by applying the above rules simultaneously to every cell in the seed—births and deaths occur simultaneously,
and the discrete moment at which this happens is sometimes called a tick (in other words, each generation is a pure function of the preceding one).

The rules continue to be applied repeatedly to create further generations.
'''

from tkinter import *
import random


#  Square class: For each cell
class Square:

    #  Initialization function (all the precalled things)
    def __init__(self, coords, length, size, state=False, active_col='black', inactive_col='white'):

        self.length = length                   # Size of map
        self.coords = coords                   # Top left corner
        self.size = size                       # Length of one side
        self.state = state                     # Alive or dead
        self.active_colour = active_col        # Colour if alive
        self.inactive_colour = inactive_col    # Colour if dead

    #  Gives the bottom right values of square
    def rect(self):
        # x+size, y+size
        return (self.coords[0]+self.size, self.coords[1]+self.size)

    #  Returns whether a coordinate is inbounds in the grid
    def inbounds(self, coord):
        (x, y) = coord

        #  Checks if x value is >= 0 and if the right side of the square is not off the board as x value is top left
        #  Checks if y value is >= 0 and if the bottom side of the square is not off the board as y value is top left
        #  True or false
        return (x >= 0 and x <= self.length-self.size) and (y >= 0 and y <= self.length-self.size)

    #  Returns all the neighbours to the object
    def neighbours(self):
        #  self.coords is a tuple. Extracting the x and y of it
        (x, y) = self.coords

        #  filter(func, iterable) loops over each value and keeps the value if the function called per value is true.
        #  I convert back to list as filter object isn't easy to deal with in my program
        #  Each item in the list is dictated by the current x or y +/- size.
        return list(filter(self.inbounds, [
                    (x-self.size, y+self.size), (x, y+self.size), (x+self.size, y+self.size),
                    (x-self.size, y),                                      (x+self.size, y),
                    (x-self.size, y-self.size), (x, y-self.size), (x+self.size, y-self.size),
                ]))

    #  Returns a colour whether the object is alive or dead
    def get_colour(self):
        #  Short hand if statement
        #  If object is alive return alive colour
        #  Or else (only two options possible) return dead colour
        return self.active_colour if self.state else self.inactive_colour


#  Grid class: The map of each square
class Grid:

    #  Initialization function (all the precalled things)
    def __init__(self, length, size, tolerance, active_col='black', inactive_col='white'):

        self.length = length                    # The length of the map
        self.tolerance = tolerance              # The tolerance of generating alive cells randomly
        self.active_col = active_col            # Alive colour
        self.inactive_col = inactive_col        # Dead colour

        self.squares = self.make_squares(size)  # The dictionary of square objects

    #  Creates a dictionary of square objects
    def make_squares(self, size):
        #  Blank dictionary to add to
        squares = {}
        #  (Rows) Loop through the 'length' in steps of 'size' (so as to get the right top left corner each time)
        for y in range(0, self.length, size):
            #  (Cells) Loop through the 'length' in steps of 'size' (so as to get the right top left corner each time)
            for x in range(0, self.length, size):
                #  If the random float is less than tolerance then make it start dead
                if random.random() < self.tolerance:
                    squares[(x, y)] = Square((x, y),
                                             self.length,
                                             size,
                                             active_col=self.active_col,
                                             inactive_col=self.inactive_col)
                #  Otherwise make it alive
                else:
                    squares[(x, y)] = Square((x, y),
                                             self.length,
                                             size,
                                             state=True,
                                             active_col=self.active_col,
                                             inactive_col=self.inactive_col)

        #  Returns a dictionary of squares
        #  { coordinate of square: square object }
        return squares

    #  Takes a list of coordinates and makes them alive cells
    #  Not used but can be used to set alive squares
    def set_squares(self, on_coordinates):
        #  Loops through the dictionary of squares
        for coord, square in self.squares:
            #  If the square is in the list of coordinates
            if coord in on_coordinates:
                #  Square is alive
                square.state = True

    #  A set of rules , as defined at the top of this script, to be applied to the grid
    def rules(self):
        #  Looping through each square
        for coord, square in self.squares.items():
            #  Create a variable to keep track of alive neighbours. Refreshes each square
            alive_neighbours = 0
            #  Grab all the squares neighbours
            neighbours = square.neighbours()

            #  Loop through each neighbour
            for neighbour in neighbours:
                #  If the neighbour is alive
                if self.squares[neighbour].state:
                    #  Increment the counter of alive neighbours
                    alive_neighbours += 1

            #  If the square is alive
            if square.state:
                #  RULE 1.
                if alive_neighbours < 2:
                    #  Kill the square
                    square.state = False
                #  RULE 3.
                elif alive_neighbours > 3:
                    #  Kill the square
                    square.state = False
                #  RULE 2.
                else:
                    #  Keep it alive
                    continue

            #  If the square isn't alive
            else:
                #  RULE 4.
                if alive_neighbours == 3:
                    #  Bring the square to life
                    square.state = True


#  App class: the actual tkinter usage
class App:

    #  Initialization function (all the precalled things)
    def __init__(self, length, size, tolerance=0.8):

        #  length % size NEEDS to = 0
        self.length = length  # Length of side of window
        self.size = size      # Length of square

        #  If the size of the boxes isn't a factor of the window size
        if not self.length % self.size == 0:
            #  The boxes don't fit evenly.
            raise Exception("The squares don't fit evenly on the screen." +
                            " Box size needs to be a factor of window size.")

        #  Create a grid object which can manipulate the squares
        self.grid = Grid(self.length, self.size, tolerance, active_col='#008080', inactive_col='white')

        #  tkinter event
        self.root = Tk()

        #  Canvas object to display squares
        self.canvas = Canvas(self.root, height=self.length, width=self.length)
        #  Set on to the window
        self.canvas.pack()

        #  updates canvas
        self.items = self.update_canvas()

        #  Creates a loop within the mainloop
        self.root.after(5, self.refresh_screen)
        #  Mainloop in tkinter, run the code and loop it until exit called
        self.root.mainloop()

    # Refreshes the screen
    def refresh_screen(self):
        #  Applies the rules to the squares
        self.grid.rules()
        #  Updates canvas
        self.update_canvas(canvas_done=True, canvas_items=self.items)

        #  Reruns the loop
        self.root.after(5, self.refresh_screen)

    #  Updates canvas
    def update_canvas(self, canvas_done=False, canvas_items={}):

        #  The dict.items() of each square
        #  { coord of square: square object }
        square_items = self.grid.squares

        #  If the canvas hasn't already been populated with the .create_rect()
        if not canvas_done:
            #  Loop through the squares
            for coords, square in square_items.items():
                (b_r_x, b_r_y) = square.rect()  #  The bottom right coordinates
                (t_l_x, t_l_y) = coords         #  Top left coordinates

                #  Draws a rectangle and stores the data in a dict corresponding to the rectangle drawn
                #  Need this to update the rectangles' colours later
                canvas_items[coords] = self.canvas.create_rectangle(t_l_x, t_l_y, b_r_x, b_r_y, fill=square.get_colour())

            #  Return the canvas items
            #  { coordinates of square drawn: canvas_rectangle object }
            return canvas_items

        #  The canvas has already been populated with squares
        #  Need this as tkinter doesn't draw on top.
        else:
            #  If canvas_items has been specified
            if canvas_items:
                #  Loop through the canvas items
                for coords, item in canvas_items.items():
                    #  Update the canvas to the new colour
                    self.canvas.itemconfig(item, fill=square_items[coords].get_colour())
            #  No canvas_items so raise a value error
            else:
                #  Throws out an error
                raise ValueError("No canvas_items given for re-iterating over canvas squares.")


# If running of the base script and not imported
if __name__ == '__main__':
    #  Create an app object
    #  Cell Size: higher it is. the faster the computer updates canvas (doesn't matter about amount of cells, just size)
    #  ^I don't know why
    app = App(1000, 10, tolerance=0.7)