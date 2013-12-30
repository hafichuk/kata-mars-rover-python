import unittest
from rover.Directions import North, East, South, West
class TestDirections(unittest.TestCase):

    def setUp(self):
        pass

    def test_leftOfNorth(self):
        self.assertTrue(North.left() == West)

    def test_rightOfNorth(self):
        self.assertTrue(North.right() == East)

    def test_leftOfEast(self):
        self.assertTrue(East.left() == North)

    def test_rightOfEast(self):
        self.assertTrue(East.right() == South)

    def test_leftOfSouth(self):
        self.assertTrue(South.left() == East)

    def test_rightOfSouth(self):
        self.assertTrue(South.right() == West)

    def test_leftOfWest(self):
        self.assertTrue(West.left() == South)

    def test_rightOfWest(self):
        self.assertTrue(West.right() == North)