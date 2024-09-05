from textnode import *
from htmlnode import *

def main():
  dummy = Textnode("Dummy Node", "bold", "google.com")
  print(dummy)
  dummyHTML = HTMLNode("tag", "value")
  print(dummyHTML)

main()