'''
Retangle Geometery Game

The objects required for this game are 
1. message -> string
2. coordinate -> float
3. rectangle -> [[int, int], [int, int]]
4. point -> [int, int]
'''
import math
import turtle
from random import randint


class Point:
    
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def falls_in_rectangle(self, rectangle):
        '''
        lowle:w
        ft is a list of x and y
        point2 is a list of x and y
        '''
        if rectangle.point1.x < self.x < rectangle.point2.x and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False
       
       
    def distance_from_point(self, point):
        '''
        Add a new distance method to the Point class. The method 
        should calculate the distance from the coordinates of the 
        current point (i.e., the self.x and self.y coordinates) to 
        the coordinates of any other given point, and such 
        coordinates can be provided as x and y arguments to the 
        distance method.
        '''
        distance = math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        return distance
    
# point1 = Point(2,3)
# point2 = Point(3,2)
# d = point1.distance_from_point(point2)
# print(d)


class Rectangle:
    
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)
    
class GuiRectangle(Rectangle):
    
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        
        #turtle.done()
       
class GuiPoint(Point):
    
    def draw(self, canvas, size = 5, color = 'red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)
              
            
# gui_rectangle = GuiRectangle(Point(randint(0, 400), randint(0, 400)), Point(randint(10, 400), randint(10, 400)))
# print(gui_rectangle.area())
    


gui_rectangle = GuiRectangle(Point(randint(0, 400), randint(0, 400)), Point(randint(10, 400), randint(10, 400)))

    

print("Rectangle Coordinates", gui_rectangle.point1.x, ",", gui_rectangle.point1.y, "and", gui_rectangle.point2.x, ",", gui_rectangle.point2.y)

user_point = GuiPoint(float(input("Guess X: ")), float(input("Guess Y: ")))
user_area = float(input("Guess rectangle area: "))

print("Is your point inside the rectangle? ", user_point.falls_in_rectangle(gui_rectangle))
print("Your area was off by:  ", gui_rectangle.area() - user_area)

my_turtle = turtle.Turtle()
gui_rectangle.draw(my_turtle)
user_point.draw(my_turtle)
turtle.done()

# pointx = Point(6,7)
# rectanglex = Rectangle(Point(5,6), Point(7,9))
# print(pointx.falls_in_rectangle(rectanglex))
 