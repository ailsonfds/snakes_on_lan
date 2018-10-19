# snake.py

from random import randint
import math

class Snake:
    __init_size=3
    __size=3
    head=None
    coords=[]
    score=0
    xlim=29
    ylim=29
    color='white'
    pattern=''
    coord=[]
    last='Up'

    def __init__(self, xlim=30, ylim=30, color=None):
        self.__init_size=3
        self.__size=self.__init_size
        self.head=[randint(0, self.xlim), randint(0, self.ylim)]
        self.coords=[self.head, [self.head[0],self.head[1]-1], [self.head[0],self.head[1]-2]]
        self.score=0
        self.xlim=30
        self.ylim=30
        self.color=color

    def walk(self, xval=0, yval=0, food=[]):
        # Calculates the new coordinates of the head of the snake. NOTE: len(snake) increases.
        # This is taken care of later at [1].
        print(self.head,xval,yval)
        self.coords.insert(0, [self.head[0] + xval, self.head[1] + yval])
        self.head=self.coords[0]

        # If snake crosses the boundaries, make it enter from the other side
        if self.head[0] < 0:
            self.head[0] = self.xlim
            self.coords[0][0] = self.xlim
        if self.head[1] < 0:
            self.head[1] = self.ylim
            self.coords[0][1] = self.ylim
        if self.head[0] > self.xlim:
            self.head[0] = 0
            self.coords[0][0] = 0
        if self.head[1] > self.ylim:
            self.head[1] = 0
            self.coords[0][1] = 0

        # Exit if snake crosses the boundaries (Uncomment to enable)
        #if self.coords[0][0] < 0 or self.coords[0][0] > self.xlim or self.coords[0][1] < 0 or self.coords[0][1] > self.ylim: return ('crash',[])

        # If snake runs over itself
        if self.coords[0] in self.coords[1:]:
            return ('crash',[])

        if self.coords[0] == food:                                            # When snake eats the food
            food = []
            self.score += 1
            while food == []:
                food = [randint(0, self.xlim), randint(0, self.ylim)]                # Calculating next food's coordinates
                if food in self.coords:
                    food = []

            return ('food',food)
        else:    
            last = self.coords.pop()                                          # [1] If it does not eat the food, length decreases
            return ('pop',last)

    def walk_l(self,*args):
        self.pattern, self.coord=self.walk(xval=-1)
        self.last='Left'

    def walk_r(self,*args):
        self.pattern, self.coord=self.walk(xval=1)
        self.last='Right'

    def walk_u(self,*args):
        self.pattern, self.coord=self.walk(yval=-1)
        self.last='Up'

    def walk_d(self,*args):
        self.pattern, self.coord=self.walk(yval=1)
        self.last='Down'
