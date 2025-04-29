class ComponentX:
  def __init__(self, name):
    if self.__class__.__qualname__ == 'ComponentX':
      raise RuntimeError('Please rename class name')
    self.name = name

  def print_component(self):
    raise RuntimeError('You should implement this')
