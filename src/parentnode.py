# an html node that has parents

from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag=None, value=None, children=None, props=None):
    if value is not None:
      raise Exception("ParentNodes are not allowed to have values")
    if children is None:
      raise Exception("ParentNodes must have children")
    super().__init__(tag, value, children, props)

  def to_html(self):
    if self.tag is None:
      raise ValueError("no tag provided")
    if self.children is None or self.children == []:
      raise ValueError("no children provided")

    test = ""

    for child in self.children:
      test += child.to_html()
    return f"<{self.tag}>{test}</{self.tag}>"        