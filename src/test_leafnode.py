import unittest
from leafnode import LeafNode
from htmlnode import HTMLNode

class TestLeafNode(unittest.TestCase):
  def test_init_without_value(self):
    with self.assertRaises(Exception) as context:
      LeafNode('p', value=None)
    self.assertTrue("LeafNodes must have a value" in str(context.exception))

  def test_init_with_children(self):
    with self.assertRaises(Exception) as context:
      LeafNode(tag='p', value="some value", children=["child"])
    self.assertTrue("LeafNodes are not allowed to have children" in str(context.exception))
  
  def test_to_html_with_tag(self):
    node = LeafNode(tag="p", value="Hello World")
    self.assertEqual(node.to_html(), "<p>Hello World</p>")

  def test_to_html_without_tag(self):
    node = LeafNode(tag=None, value=("Hello World"))
    self.assertEqual(node.to_html(), "Hello World")

if __name__ == "__main__":
  unittest.main()