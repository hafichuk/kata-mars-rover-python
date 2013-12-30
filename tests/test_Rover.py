import unittest
from rover.Rover import Rover
from rover.Directions import *
import sys

class TestRover(unittest.TestCase):

    def test_roverDefaultStatus(self):
        self.assertDictEqual({'x':0,'y':0,'d':'north'}, Rover().getStatus())

    def test_roverIsAtDefaultOrientation(self):
        rover = Rover()
        self.assertTrue(rover.getOrientation() == North)

    def test_turnRightInCircle(self):
        rover = Rover()
        self.assertTrue(rover.right() == East)
        self.assertTrue(rover.right() == South)
        self.assertTrue(rover.right() == West)
        self.assertTrue(rover.right() == North)

    def test_turnLeftInCircle(self):
        rover = Rover()
        self.assertTrue(rover.left() == West)
        self.assertTrue(rover.left() == South)
        self.assertTrue(rover.left() == East)
        self.assertTrue(rover.left() == North)

    def test_roverIsAtDefaultPosition(self):
        rover = Rover()
        self.assertDictEqual({'x':0,'y':0}, rover.getPosition())

    def test_moveForwardNorth(self):
        self.assertDictEqual({'x':0,'y':1}, Rover(orientation=North).forward())

    def test_moveBackwardNorth(self):
        self.assertDictEqual({'x':0,'y':-1}, Rover(orientation=North).backward())

    def test_moveForwardEast(self):
        self.assertDictEqual({'x':1,'y':0}, Rover(orientation=East).forward())

    def test_moveBackwardEast(self):
        self.assertDictEqual({'x':-1,'y':0}, Rover(orientation=East).backward())

    def test_moveRight(self):
        path = 'r'
        rover = Rover()
        rover.move(path)
        self.assertTrue(rover.getOrientation() == East)
        self.assertDictEqual({'x':0,'y':0}, rover.getPosition())

    def test_moveLeft(self):
        path = 'l'
        rover = Rover()
        rover.move(path)
        self.assertTrue(rover.getOrientation() == West)
        self.assertDictEqual({'x':0,'y':0}, rover.getPosition())

    def test_moveForward(self):
        path = 'f'
        rover = Rover()
        rover.move(path)
        self.assertTrue(rover.getOrientation() == North)
        self.assertDictEqual({'x':0,'y':1}, rover.getPosition())

    def test_moveBackward(self):
        path = 'b'
        rover = Rover()
        rover.move(path)
        self.assertTrue(rover.getOrientation() == North)
        self.assertDictEqual({'x':0,'y':-1}, rover.getPosition())

    def test_moveFFRFF(self):
        path = 'ffrff'
        rover = Rover()
        rover.move(path)
        self.assertTrue(rover.getOrientation() == East)
        self.assertDictEqual({'x':2,'y':2}, rover.getPosition())

    def test_moveInvalid(self):
        rover = Rover()
        self.assertRaises(ValueError, rover.move, commands='ffrzff')