import enum

class AbstractNode:
    def __init__(self, type, children=None, leaf=None):
         self.type = type
         if children:
              self.children = children
         else:
              self.children = [ ]
         self.leaf = leaf


class NodeType(enum.Enum):
    ROOT = 1