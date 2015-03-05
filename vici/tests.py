import unittest
import vici

class TestVici(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = vici.Session()

    def test_version(self):
        v = set(x.decode('ascii') for x in self.s.version().keys())
        self.assertIn('version', v)
        self.assertIn('daemon', v)
        self.assertIn('sysname', v)
        self.assertIn('machine', v)
        self.assertIn('release', v)

