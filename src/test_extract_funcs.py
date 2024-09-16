import unittest
from main import text_node_to_html_node, extract_markdown_images, extract_markdown_links
from leafnode import LeafNode
from textnode import Textnode

class TestFunctions(unittest.TestCase):

    def test_text_node_to_html_node(self):
        # Test "text" type
        text_node = Textnode("This is text", "text")
        result = text_node_to_html_node(text_node)
        expected = LeafNode(tag=None, value="This is text")
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.value, expected.value)

        # Test "bold" type
        bold_node = Textnode("Bold text", "bold")
        result = text_node_to_html_node(bold_node)
        expected = LeafNode(tag="b", value="Bold text")
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.value, expected.value)

        # Test "italic" type
        italic_node = Textnode("Italic text", "italic")
        result = text_node_to_html_node(italic_node)
        expected = LeafNode(tag="i", value="Italic text")
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.value, expected.value)

        # Test "code" type
        code_node = Textnode("print('hello')", "code")
        result = text_node_to_html_node(code_node)
        expected = LeafNode(tag="code", value="print('hello')")
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.value, expected.value)

        # Test "link" type
        link_node = Textnode("Click here", "link", "https://example.com")
        result = text_node_to_html_node(link_node)
        expected = LeafNode(tag="a", value="Click here", props={"href": "https://example.com"})
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.value, expected.value)
        self.assertEqual(result.props, expected.props)

        # Test "image" type
        image_node = Textnode("Image description", "image", "https://example.com/image.png")
        result = text_node_to_html_node(image_node)
        expected = LeafNode(tag="img", value="", props={"src": "https://example.com/image.png", "alt": "Image description"})
        self.assertEqual(result.tag, expected.tag)
        self.assertEqual(result.value, expected.value)
        self.assertEqual(result.props, expected.props)

        # Test invalid type
        invalid_node = Textnode("Invalid type", "unknown")
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(invalid_node)
        self.assertTrue("invalid text type" in str(context.exception))

    def test_extract_markdown_images(self):
        # Test valid markdown image
        text = "This is an image ![alt text](https://example.com/image.jpg)"
        result = extract_markdown_images(text)
        expected = [("alt text", "https://example.com/image.jpg")]
        self.assertEqual(result, expected)

        # Test no images in text
        text = "This text has no images."
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result, expected)

        # Test multiple images
        text = "Image one ![one](https://example.com/one.jpg), Image two ![two](https://example.com/two.jpg)"
        result = extract_markdown_images(text)
        expected = [("one", "https://example.com/one.jpg"), ("two", "https://example.com/two.jpg")]
        self.assertEqual(result, expected)

        # Test malformed image markdown
        text = "Broken image ![alt text]https://example.com/image.jpg)"
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result, expected)

    def test_extract_markdown_links(self):
        # Test valid markdown link
        text = "This is a [link](https://example.com)."
        result = extract_markdown_links(text)
        expected = [("link", "https://example.com")]
        self.assertEqual(result, expected)

        # Test no links in text
        text = "This text has no links."
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result, expected)

        # Test multiple links
        text = "Here are two links: [link1](https://example1.com) and [link2](https://example2.com)."
        result = extract_markdown_links(text)
        expected = [("link1", "https://example1.com"), ("link2", "https://example2.com")]
        self.assertEqual(result, expected)

        # Test malformed link markdown
        text = "Broken link [text]https://example.com)"
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
