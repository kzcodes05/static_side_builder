import unittest
from textnode import Textnode
from leafnode import LeafNode
from htmlnode import HTMLNode
from main import text_node_to_html_node

class TestToHTML(unittest.TestCase):
  def test_text(self):
    text_node = Textnode(text_type="text", text="hello")
    expected_node = LeafNode(tag=None, value="hello")
    self.assertEqual(text_node_to_html_node(text_node), expected_node)
  
  def test_bold(self):
    bold_node = Textnode(text_type="bold", text="hello")
    expected_node = LeafNode(tag="b", value="hello")
    self.assertEqual(text_node_to_html_node(bold_node), expected_node)

  def test_italic(self):
    italic_node = Textnode(text_type="italic", text="hello")
    expected_node = LeafNode(tag="i", value="hello")
    self.assertEqual(text_node_to_html_node(italic_node), expected_node)

  def test_code(self):
    code_node = Textnode(text_type="code", text="hello")
    expected_node = LeafNode(tag="code", value="hello")
    self.assertEqual(text_node_to_html_node(code_node), expected_node)

  def test_link(self):
    link_node = Textnode(text_type="link", text="hello", url="hello")
    expected_node = LeafNode(tag="a", value="hello", props={"href": "hello"})
    self.assertEqual(text_node_to_html_node(link_node), expected_node)

  def test_image(self):
    image_node = Textnode(text_type="image", text="hello", url="hello")
    expected_node = LeafNode(tag="img", value="", props={"src": "hello", "alt": "hello"})
    self.assertEqual(text_node_to_html_node(image_node), expected_node)

if __name__ == "__main__":
  unittest.main()