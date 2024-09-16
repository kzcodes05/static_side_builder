from textnode import Textnode

def split_nodes_delimiter(old_nodes, delimiter, text_type): # old_notes = list
  nodes = []

  text_type_text="text"
  text_type_code="code"
  text_type_bold = "bold"
  text_type_italic = "italic"

  for old_node in old_nodes:
    if old_node.text_type == "text":
      segments = old_node.text.split(delimiter)
      for i in range(len(segments)):
        if i == 0 or i % 2 == 0:
          new_node = Textnode(segments[i], text_type_text)
        else:
          new_node = Textnode(segments[i], text_type)
        nodes.append(new_node)
      if len(segments) % 2 == 0:
        raise ValueError("Unmatched delimiters in input text")
    else:
      nodes.append(old_node)
  return nodes
