class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag # string
    self.value = value # string
    self.children = children # list
    self.props = props # dict

    # overriden by child classes
  def to_html(self):
    raise NotImplementedError
    
  def props_to_html(self):
    return str(self.props)
    
  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"