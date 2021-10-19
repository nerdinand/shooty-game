from simulation import Simulation
from gui import Gui


def main(with_gui=True):
  simulation = Simulation()

  if with_gui:
    run_with_gui(simulation)
  else:
    run_without_gui(simulation)

def run_with_gui(simulation):
  gui = Gui(key_target_player=simulation.human)
  gui.initialize()

  while not simulation.over() and not gui.should_quit():
    simulation.tick()

    gui.tick()

    gui.handle_key_events()
    gui.handle_mouse_events()
    
    if gui.is_render_necessary():
      gui.render(simulation)

def run_without_gui(simulation):
  while not simulation.over():
    simulation.tick()

if __name__ == '__main__':
  # main(with_gui=False)
  main(with_gui=True)
