#coding=utf-8
import os
import unittest
from NAME.ex47 import Room

class TestEx47(unittest.TestCase):
    def setup(self):
        print("SETUP！")

    def teardown(self):
        print("TEAR DOWN!")

    def test_room(self):
        gold = Room("GoldRoom","This room has gold in it you can grab.There's a door to the north.")
        self.assertEqual(gold.name,"GoldRoom")
        self.assertEqual(gold.paths,{})

    def test_room_paths(self):
        center = Room("Center","Test room in the center.")
        north = Room("Center","Test room in the north.")
        south = Room("Center","Test room in the south.")

        center.add_paths({'north':north,'south':south})
        self.assertEqual(center.go('north'),north)
        self.assertEqual(center.go('south'),south)

    def test_map(self):
        start = Room("start","You can go west and down a hole.")
        west = Room("Trees","There are trees here, you can go east.")
        down = Room("Dungeon", "It's dark down here,you can go up.")

        start.add_paths({'west':west,'down':down})
        west.add_paths({'east':start})
        down.add_paths({'up':start})

        self.assertEqual(start.go('west'),west)
        self.assertEqual(start.go('west').go('east'),start)
        self.assertEqual(start.go('down').go('up'),start)

if __name__ == "__main__":
    unit = unittest.TestSuite()
    unit.addTest(TestEx47("test_room"))
    unit.addTest(TestEx47("test_room_paths"))
    unit.addTest(TestEx47("test_map"))
    runner = unittest.TextTestRunner()
    runner.run(unit)
