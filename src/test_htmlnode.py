import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
  def test_init(self):
    node = HTMLNode(tag='div', value='hello', children=["child1", "child2"], props={"class": "container"})
    self.assertEqual(node.tag, 'div')
    self.assertEqual(node.value, "hello")
    self.assertEqual(node.children, ["child1", "child2"])
    self.assertEqual(node.props, {"class": "container"})

    node_default = HTMLNode()
    self.assertIsNone(node_default.tag)
    self.assertIsNone(node_default.value)
    self.assertIsNone(node_default.children)
    self.assertIsNone(node_default.props)

  def test_to_html_not_implemented(self):
    node = HTMLNode()
    with self.assertRaises(NotImplementedError):
      node.to_html()
  

if __name__ == "__main__":
  unittest.main()