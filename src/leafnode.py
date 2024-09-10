# a single HTML tag with no children
from htmlnode import HTMLNode

class LeafNode(HTMLNode):
  def __init__(self, tag=None, value=None, children=None, props=None):
    if children is not None:
      raise Exception(f"LeafNodes are not allowed to have children. provided: {children}")
    if value is None:
      raise Exception("LeafNodes must have a value")
    
    super().__init__(tag, value, children, props)

  def to_html(self):
    
    if self.tag is None:
      return f"{self.value}"
    else:
      return f"<{self.tag}>{self.value}</{self.tag}>"