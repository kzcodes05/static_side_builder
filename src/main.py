from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *

def main():
  dummy = Textnode("Dummy Node", "bold", "google.com")
  print(dummy)
  dummyHTML = HTMLNode("tag", "value")
  print(dummyHTML)

def text_node_to_html_node(text_node):
  match text_node.text_type:
    case "text":
      return LeafNode(tag=None, value=text_node.text)
    case "bold":
      return LeafNode(tag="b", value=text_node.text)
    case "italic":
      return LeafNode(tag="i", value=text_node.text)
    case "code":
      return LeafNode(tag="code", value=text_node.text)
    case "link":
      return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    case "image":
      return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text}) 
    case _:
      raise Exception("invalid text type")

main()