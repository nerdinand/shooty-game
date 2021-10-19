from simulation import Simulation
from gui import Gui


def main(with_gui=True):
  simulation = Simulation()

  if with_gui:
    gui = Gui(key_target_player=simulation.human)
    gui.initialize()
  else:
    gui = None

  while not simulation.over() and not (gui and gui.should_quit()):
    simulation.tick()

    if not gui is None:
      gui.tick()

      gui.handle_key_events()
      gui.handle_mouse_events()
      
      if gui.is_render_necessary():
        gui.render(simulation)

if __name__ == '__main__':
  # main(with_gui=False)
  main(with_gui=True)
