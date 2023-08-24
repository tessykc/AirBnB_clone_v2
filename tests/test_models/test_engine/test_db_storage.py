import unittest
from models.engine.dbstorage import DBStorage
from models.base_model import BaseModel
from os import getenv
import MySQLdb


@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "DB storage only")
class TestDBStorage(unittest.TestCase):
    """
    Test the DBStorage class
    """
    def setUp(self):
        """
        Create the DBStorage instance and establish a database connection
        """
        self.db = MySQLdb.connect(
            host=getenv('HBNB_MYSQL_HOST'),
            user=getenv('HBNB_MYSQL_USER'),
            passwd=getenv('HBNB_MYSQL_PWD'),
            db=getenv('HBNB_MYSQL_DB'),
            port=3306
        )
        self.cur = self.db.cursor()

    def tearDown(self):
        """
        Close the database connection and clear the tables
        """
        self.cur.close()
        self.db.close()

    def test_all(self):
        """
        Test the all() method of DBStorage
        """
        self.assertEqual(type(storage.all()), dict)
        self.assertIs(storage.all(), storage._DBStorage__objects)

    def test_new(self):
        """
        Test the new() method of DBStorage
        """
        new_model = BaseModel()
        storage.new(new_model)
        self.assertIn(new_model, list(storage._DBStorage__session))
        self.assertEqual(len(list(storage.all())), 1)

    def test_save(self):
        """
        Test the save() method of DBStorage
        """
        new_model = BaseModel()
        storage.new(new_model)
        storage.save()
        query = "SELECT COUNT(*) FROM {}".format(type(new_model).__name__)
        self.cur.execute(query)
        result = self.cur.fetchone()
        self.assertEqual(result[0], 1)

    def test_delete(self):
        """
        Test the delete() method of DBStorage
        """
        new_model = BaseModel()
        storage.new(new_model)
        storage.save()
        storage.delete(new_model)
        query = "SELECT COUNT(*) FROM {}".format(type(new_model).__name__)
        self.cur.execute(query)
        result = self.cur.fetchone()
        self.assertEqual(result[0], 0)

    def test_reload(self):
        """
        Test the reload() method of DBStorage
        """
        storage.reload()
        self.assertTrue(isinstance(storage._DBStorage__engine, type(self.db)))
        self.assertTrue(isinstance(storage._DBStorage__session, type(self.cur)))


if __name__ == '__main__':
    unittest.main()
