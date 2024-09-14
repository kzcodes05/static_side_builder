import unittest
from textnode import Textnode
from split_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic_split(self):
        old_nodes = [Textnode("This is *bold* text", "text")]
        delimiter = "*"
        text_type = "bold"
        
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        expected = [
            Textnode("This is ", "text"),
            Textnode("bold", "bold"),
            Textnode(" text", "text")
        ]
        
        self.assertEqual(result, expected)

    def test_unmatched_delimiter(self):
        old_nodes = [Textnode("This is *bold text", "text")]
        delimiter = "*"
        text_type = "bold"
        
        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, delimiter, text_type)

    def test_non_text_nodes(self):
        old_nodes = [Textnode("This is code", "code")]
        delimiter = "*"
        text_type = "bold"
        
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        expected = [Textnode("This is code", "code")]
        
        self.assertEqual(result, expected)

    def test_multiple_delimiters(self):
        old_nodes = [Textnode("This *is* a *test*", "text")]
        delimiter = "*"
        text_type = "bold"
        
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        expected = [
            Textnode("This ", "text"),
            Textnode("is", "bold"),
            Textnode(" a ", "text"),
            Textnode("test", "bold"),
            Textnode("", "text")
        ]
        
        self.assertEqual(result, expected)

    def test_empty_content(self):
        old_nodes = [Textnode("", "text")]
        delimiter = "*"
        text_type = "bold"
        
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        expected = [Textnode("", "text")]
        
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()