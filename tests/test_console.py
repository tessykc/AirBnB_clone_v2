#!/usr/bin/python3
"""Test for HBNBCommand class (console.py)"""
import unittest
import sys
import os
import io
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):
    """Test for HBNBCommand class"""

    def setUp(self):
        """Set up environment"""
        self.console_o = HBNBCommand()
        self.basemodel_o = BaseModel()
        self.user_o = User()
        self.place_o = Place()
        self.state_o = State()
        self.city_o = City()
        self.amenity_o = Amenity()
        self.review_o = Review()
        self.all_list = [self.basemodel_o, self.user_o, self.place_o,
                         self.state_o, self.city_o, self.amenity_o,
                         self.review_o]

    def tearDown(self):
        """Tear down environment"""
        pass

    def test_emptyline(self):
        """Test for emptyline"""
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            self.console_o.onecmd("\n")
            self.assertEqual(f.getvalue(), '')

    def test_help(self):
        """Test for help"""
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            self.console_o.onecmd("help\n")
            self.assertGreater(len(f.getvalue()), 0)

    def test_create(self):
        """Test for create"""
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            for i in self.all_list:
                self.console_o.onecmd("create {}\n".format(i.__class__.__name__))
                self.assertGreater(len(f.getvalue()), 0)

    def test_show(self):
        """Test for show"""
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            for i in self.all_list:
                self.console_o.onecmd("show {} {}\n".format(i.__class__.__name__, i.id))
                self.assertGreater(len(f.getvalue()), 0)
            self.console_o.onecmd("show BaseModel\n")
            self.assertEqual(f.getvalue(), '** instance id missing **\n')
            self.console_o.onecmd("show BaseModel {}\n".format(self.basemodel_o.id))
            self.assertEqual(f.getvalue(), str(self.basemodel_o) + '\n')
            self.console_o.onecmd("show BaseModel {}\n".format("invalid_id"))
            self.assertEqual(f.getvalue(), "** no instance found **\n")
            self.console_o.onecmd("show InvalidClass {}\n".format("invalid_id"))
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_destroy(self):
        """Test for destroy"""
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            for i in self.all_list:
                self.console_o.onecmd("destroy {} {}\n".format(i.__class__.__name__, i.id))
                self.assertEqual(f.getvalue(), '')
                self.assertEqual(storage.all().get("{}.{}".format(i.__class__.__name__, i.id)), None)
            self.console_o.onecmd("destroy BaseModel\n")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
            self.console_o.onecmd("destroy BaseModel {}\n".format(self.basemodel_o.id))
            self.assertEqual(f.getvalue(), '')
            self.console_o.onecmd("destroy BaseModel {}\n".format("invalid_id"))
            self.assertEqual(f.getvalue(), '** no instance found **\n')
            self.console_o.onecmd("destroy InvalidClass {}\n".format("invalid_id"))
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_all(self):
        """Test for all"""
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            self.console_o.onecmd("all\n")
            self.assertGreater(len(f.getvalue()), 0)
            self.console_o.onecmd("all InvalidClass\n")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_count(self):
        """Test for count"""
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            self.console_o.onecmd("count\n")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
            self.console_o.onecmd("count BaseModel\n")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_update(self):
        """Test for update"""
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            for i in self.all_list:
                self.console_o.onecmd("update {} {} id \"{}\"\n".format(
                    i.__class__.__name__, i.id, "new_id"))
                self.assertEqual(f.getvalue(), '')
                self.assertEqual(i.id, "new_id")
                i.save()
            self.console_o.onecmd("update BaseModel\n")
            self.assertEqual(f.getvalue(), '** instance id missing **\n')
            self.console_o.onecmd("update BaseModel {}\n".format(self.basemodel_o.id))
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")
            self.console_o.onecmd("update BaseModel {} {}\n".format(self.basemodel_o.id, "name"))
            self.assertEqual(f.getvalue(), "** value missing **\n")
            self.console_o.onecmd("update BaseModel {} name \"name\"\n".format(self.basemodel_o.id))
            self.assertEqual(f.getvalue(), '')
            self.assertEqual(self.basemodel_o.name, "name")
            self.console_o.onecmd("update BaseModel {} name name\n".format(self.basemodel_o.id))
            self.assertEqual(f.getvalue(), '')
            self.assertEqual(self.basemodel_o.name, "name")
            self.console_o.onecmd("update BaseModel {} name 25\n".format(self.basemodel_o.id))
            self.assertEqual(f.getvalue(), '')
            self.assertEqual(self.basemodel_o.name, 25)
            self.console_o.onecmd("update BaseModel {} name 25.5\n".format(self.basemodel_o.id))
            self.assertEqual(f.getvalue(), '')
            self.assertEqual(self.basemodel_o.name, 25.5)
            self.console_o.onecmd("update BaseModel {} name \"name\"\n".format(self.basemodel_o.id))
            self.assertEqual(f.getvalue(), '')
            self.assertEqual(self.basemodel_o.name, "name")
            self.console_o.onecmd("update BaseModel {} name \"new name\"\n".format("invalid_id"))
            self.assertEqual(f.getvalue(), "** no instance found **\n")
            self.console_o.onecmd("update InvalidClass {} name \"new name\"\n".format("invalid_id"))
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_quit(self):
        """Test for quit"""
        with self.assertRaises(SystemExit), patch('sys.stdout', new_callable=io.StringIO) as f:
            self.console_o.onecmd("quit")
            self.assertGreater(len(f.getvalue()), 0)

    def test_EOF(self):
        """Test for EOF"""
        with self.assertRaises(SystemExit), patch('sys.stdout', new_callable=io.StringIO) as f:
            self.console_o.onecmd("EOF")
            self.assertGreater(len(f.getvalue()), 0)

    def test_unknown(self):
        """Test for unknown commands"""
        with patch('sys.stdout', new_callable=io.StringIO) as f:
            self.console_o.onecmd("unknown\n")
            self.assertGreater(len(f.getvalue()), 0)


if __name__ == '__main__':
    unittest.main()

