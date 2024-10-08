# all the inline text, normal, bold, italic...

class Textnode:
  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url

  # tests if 2 nodes are equal (Im just tryna get used to writing comments)
  def __eq__(self, textnode2):
    return (
      self.text == textnode2.text and
      self.text_type == textnode2.text_type and
      self.url == textnode2.url
    )
  
  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type}, {self.url})"