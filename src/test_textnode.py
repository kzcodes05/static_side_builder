import unittest

from textnode import Textnode

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = Textnode("This is a text node", "bold")
    node2 = Textnode("This is a text node", "bold")
    self.assertEqual(node, node2)

  def test_eq_2(self):
    node1 = Textnode("Equal Nodes!", "italic")
    node2 = Textnode("Equal Nodes!", "italic")
    self.assertEqual(node1, node2)

  def test_not_eq(self):
    node1 = Textnode("Not Equal!", "bold")
    node2 = Textnode("So not equal!", "italic")
    self.assertNotEqual(node1, node2)

  def test_url_none(self):
    node = Textnode("No URL", "bold")
    self.assertIsNone(node.url)
  
  def test_url_not_none(self):
    node = Textnode("URL", "bold", "url.com")
    self.assertIsNotNone(node.url)

if __name__ == "__main__":
  unittest.main()