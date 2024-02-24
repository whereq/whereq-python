import unittest

from src.example.regex.regex_practices import RegexPractice

class RegexPracticeTest(unittest.TestCase):
  def setUp(self):
    self.regex = RegexPractice()

  def test_match(self):
    self.assertIsNotNone(self.regex.match(r'\d+', '123abc'))
    self.assertIsNone(self.regex.match(r'\d+', 'abc'))

  def test_search(self):
    self.assertIsNotNone(self.regex.search(r'\d+', 'abc123def'))
    self.assertIsNone(self.regex.search(r'\d+', 'abcdef'))

  def test_find_all(self):
    self.assertEqual(self.regex.find_all(r'\d+', '123abc456def789'), ['123', '456', '789'])
    self.assertEqual(self.regex.find_all(r'\d+', 'abcdef'), [])

  def test_split(self):
    self.assertEqual(self.regex.split(r'\d+', '123abc456def789'), ['', 'abc', 'def', ''])
    self.assertEqual(self.regex.split(r'\d+', 'abcdef'), ['abcdef'])

if __name__ == '__main__':
  unittest.main()