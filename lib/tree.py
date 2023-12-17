class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):

    node_to_visit = [self.root]
    result = []

    while len(node_to_visit) > 0:
      node = node_to_visit.pop(0)
      if node['id'] == id:
        result.append(node)
        return result[0]
      node_to_visit = node['children'] + node_to_visit
    
    return None
      







    
      

