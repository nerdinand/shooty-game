import time

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

  start_time = time.time()

  while not simulation.over() and not gui.should_quit():
    simulation.tick()

    gui.tick()

    gui.handle_key_events()
    gui.handle_mouse_events()
    
    if gui.is_render_necessary():
      gui.render(simulation)

    print_statistics(start_time, simulation.tick_count)
  print()

def run_without_gui(simulation):
  start_time = time.time()
  while not simulation.over():
    simulation.tick()
    print_statistics(start_time, simulation.tick_count)
  print()

def print_statistics(start_time, tick_count):
  current_time = time.time()
  print(f'Ticks: {tick_count}/{Simulation.MAX_TICKS} TPS: {round(tick_count / ((current_time - start_time)))}        ', end="\r")


if __name__ == '__main__':
  # main(with_gui=False)
  main(with_gui=True)
