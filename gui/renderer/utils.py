class Utils:
  def to_screen_position(screen_size, position):
    return position.elementwise() * screen_size
