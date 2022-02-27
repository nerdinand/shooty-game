import time
from typing import Optional

import click

from gui import Gui
from gui.renderer.render_settings import RenderSettings
from simulation import Simulation


@click.group()
def cli() -> None:
    pass


@cli.command("sim")
@click.option("--bot-count", default=4, help="How many bots to spawn.")
@click.option("--seed", type=int, help="Random seed for simulation.")
def run_simulation(bot_count: int, seed: Optional[int] = None) -> None:
    simulation = Simulation(bot_count=bot_count, random_seed=seed)
    start_time = time.time()

    while not simulation.is_over():
        simulation.tick()
        print_statistics(start_time, simulation)

    print()


@cli.command("gui")
@click.option(
    "--with-human",
    default=False,
    is_flag=True,
    help="Run simulation with a human (controllable with keyboard).",
)
@click.option("--bot-count", default=4, help="How many bots to spawn.")
@click.option("--show-bots/--hide-bots", default=True, help="Show bots in GUI.")
@click.option(
    "--show-map/--hide-map", default=True, help="Show map (obstacles) in GUI."
)
@click.option(
    "--show-visibility/--hide-visibility",
    default=False,
    help="Show visibility (FOV cone and visible points) in GUI.",
)
@click.option("--seed", type=int, help="Random seed for simulation.")
def run_gui(
    with_human: bool,
    bot_count: int,
    show_bots: bool,
    show_map: bool,
    show_visibility: bool,
    seed: Optional[int],
) -> None:
    simulation = Simulation(
        with_human=with_human, bot_count=bot_count, random_seed=seed
    )
    gui = Gui(
        key_target_player=simulation.human,
        render_settings=RenderSettings(show_bots, show_map, show_visibility),
    )
    gui.initialize()

    start_time = time.time()

    while not simulation.is_over() and not Gui.should_quit():
        simulation.tick()

        gui.tick()

        gui.handle_key_events()
        gui.handle_mouse_events()

        if gui.is_render_necessary():
            gui.render(simulation)

        print_statistics(start_time, simulation)

    print()


def print_statistics(start_time: float, simulation: Simulation) -> None:
    current_time = time.time()
    print(
        f"Ticks: {simulation.tick_count}/{Simulation.MAX_TICKS} \
TPS: {round(simulation.tick_count / ((current_time - start_time)))} \
Players: {simulation.alive_players_count()}        ",
        end="\r",
    )


if __name__ == "__main__":
    cli()
