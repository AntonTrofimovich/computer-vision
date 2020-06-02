from graphics import GraphWin, Line, Circle, Oval, Point

win = GraphWin(width=620, height=250)

line = Line(Point(10, 10), Point(190, 190))
line.draw(win)

circle = Circle(Point(350, 110), 100)
circle.draw(win)

ellipse = Oval(Point(510, 10), Point(610, 190))
ellipse.setFill('green');
ellipse.draw(win)

win.getMouse()