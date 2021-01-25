from manim import *
import math

func = "sin(x)"
f = lambda x: eval(func, {'x': x, 'sin': math.sin, 'cos': math.cos, 'abs': abs})
x_min = -10
x_max = 10
y_min = -10
y_max = 10

class Plot(GraphScene):
    def __init__(self):
        GraphScene.__init__(
            self,
            x_min = x_min,
            x_max = x_max,
            y_min = y_min,
            y_max = y_max,
            graph_origin = ORIGIN
        )
        self.function_color = BLUE

    def construct(self):
        self.setup_axes(animate = True)
        graph = self.get_graph(f, color = BLUE)  
                                          
        self.play(ShowCreation(graph), run_time = 5)
        self.wait(2)