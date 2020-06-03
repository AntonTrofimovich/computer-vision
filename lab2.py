from graphics import GraphWin, Point, Polygon

win = GraphWin('Draw a Triangle', 350, 350)

starVerticies = [
    Point(172.0, 37.0),
    Point(138.0, 121.0),
    Point(57.0, 122.0),
    Point(107.0, 177.0),
    Point(59.0, 258.0),
    Point(162.0, 205.0),
    Point(252.0, 252.0),
    Point(208.0, 178.0),
    Point(268.0, 123.0),
    Point(185.0, 116.0)
]

triangle = Polygon(starVerticies)
triangle.setFill('green')
triangle.setOutline('black')
triangle.setWidth(2)
triangle.draw(win)

win.getMouse();
