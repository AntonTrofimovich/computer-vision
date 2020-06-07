from graphics import GraphWin, Point, Polygon

def get_star_verticies():
    return [
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

def create_polygon(verticies, outline_color, outline_width, fill_color):
    polygon = Polygon(verticies)
    polygon.setOutline(outline_color)
    polygon.setWidth(outline_width)
    polygon.setFill(fill_color)

    return polygon

win = GraphWin('Fill a polygon', 350, 350)
star = create_polygon(get_star_verticies(), outline_color="black", outline_width=2, fill_color="green")
star.draw(win)

win.getMouse();
