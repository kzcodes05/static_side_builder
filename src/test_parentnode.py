import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
  def test_initialization_without_value(self):
    with self.assertRaises(Exception) as context:
      ParentNode(tag="div", value="This should raise an Error", children=[LeafNode(tag="span", value="some value")])
    self.assertTrue("ParentNodes are not allowed to have values" in str(context.exception))

  def test_initialization_without_children(self):
    with self.assertRaises(Exception) as context:
      ParentNode(tag="div", children=None)
    self.assertTrue("ParentNodes must have children" in str(context.exception))
  
  def test_initialization_with_correct_parameters(self):
    node = ParentNode(tag="div", children=[LeafNode(tag="span", value="some value")])
    self.assertEqual(node.tag, "div")
    self.assertEqual(len(node.children), 1)

  def test_to_html_method_with_valid_data(self):
    child_node = LeafNode(tag="span", value="Hello")
    parent_node = ParentNode(tag="div", children=[child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>Hello</span></div>")

  def test_to_html_method_with_missing_tag(self):
    parent_node = ParentNode(tag=None, children=[LeafNode(tag="span", value="some value")])
    with self.assertRaises(ValueError) as context:
      parent_node.to_html()
    self.assertTrue("no tag provided" in str(context.exception))

  def test_to_html_with_missing_children(self):
    parent_node = ParentNode(tag="div", children=[])
    with self.assertRaises(ValueError) as context:
      parent_node.to_html()
    self.assertTrue("no children provided" in str(context.exception))


  def test_to_html_with_nested_children(self):
    child_node1 = LeafNode(tag="span", value="Hello")
    child_node2 = LeafNode(tag="a", value="Link")
    parent_node = ParentNode(tag="div", children=[child_node1, child_node2])
    self.assertEqual(parent_node.to_html(), "<div><span>Hello</span><a>Link</a></div>")

if __name__ == "__main__":
  unittest.main()