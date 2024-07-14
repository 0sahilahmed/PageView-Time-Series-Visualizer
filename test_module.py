import unittest
import matplotlib
matplotlib.use('Agg')
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

class DataCleaningTestCase(unittest.TestCase):
    def setUp(self):
        # Set up any required state or variables
        pass
    
    def test_draw_line_plot(self):
        fig = draw_line_plot()
        self.assertTrue(fig is not None, "Line plot figure is None")
        self.assertTrue(isinstance(fig, matplotlib.figure.Figure), "Output is not a Matplotlib figure")
    
    def test_draw_bar_plot(self):
        fig = draw_bar_plot()
        self.assertTrue(fig is not None, "Bar plot figure is None")
        self.assertTrue(isinstance(fig, matplotlib.figure.Figure), "Output is not a Matplotlib figure")
    
    def test_draw_box_plot(self):
        fig = draw_box_plot()
        self.assertTrue(fig is not None, "Box plot figure is None")
        self.assertTrue(isinstance(fig, matplotlib.figure.Figure), "Output is not a Matplotlib figure")

if __name__ == '__main__':
    unittest.main()
