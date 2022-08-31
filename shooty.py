import io
import time
from typing import Optional

import click

from gui import Gui
from gui.renderer.render_settings import RenderSettings
import simulation
from simulation import Simulation
import training
from training import Training, Player
import environment


@click.group()
def cli() -> None:
    """Run the main click group."""
    pass


@cli.command("train")
@click.option(
    "--training-conf",
    required=True,
    type=click.File(),
    help="Training configuration YAML file.",
)
@click.option(
    "--simulation-conf",
    required=True,
    type=click.File(),
    help="Simulation configuration YAML file.",
)
@click.option(
    "--environment-conf",
    required=True,
    type=click.File(),
    help="Environment configuration YAML file.",
)
def train(
    training_conf: io.TextIOBase,
    simulation_conf: io.TextIOBase,
    environment_conf: io.TextIOBase,
) -> None:
    """Train a model."""
    training_configuration = training.Configuration.from_file(training_conf)
    simulation_configuration = simulation.Configuration.from_file(simulation_conf)
    environment_configuration = environment.Configuration.from_file(environment_conf)
    t = Training(
        training_configuration, simulation_configuration, environment_configuration
    )
    t.train()


@cli.command("play")
@click.option(
    "--model",
    required=True,
    type=click.Path(exists=True),
    help="The model to play with.",
)
@click.option(
    "--simulation-conf",
    required=True,
    type=click.File(),
    help="Simulation configuration YAML file.",
)
@click.option(
    "--environment-conf",
    required=True,
    type=click.File(),
    help="Environment configuration YAML file.",
)
def play(
    model: str, simulation_conf: io.TextIOBase, environment_conf: io.TextIOBase
) -> None:
    """Play using a trained model."""
    simulation_configuration = simulation.Configuration.from_file(simulation_conf)
    environment_configuration = environment.Configuration.from_file(environment_conf)
    Player(
        model_path=model,
        number_of_episodes=10,
        simulation_configuration=simulation_configuration,
        environment_configuration=environment_configuration,
    ).play()


@cli.command("sim")
@click.option(
    "--simulation-conf",
    required=True,
    type=click.File(),
    help="Simulation configuration YAML file.",
)
def run_simulation(simulation_conf: io.TextIOBase) -> None:
    """Run a simulation."""
    configuration = simulation.configuration.Configuration.from_file(simulation_conf)
    sim = Simulation(configuration)

    start_time = time.time()

    while not sim.is_over():
        sim.tick()
        print_statistics(start_time, sim)

    print()


@cli.command("gui")
@click.option(
    "--simulation-conf",
    required=True,
    type=click.File(),
    help="Simulation configuration YAML file.",
)
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
    simulation_conf: io.TextIOBase,
    show_bots: bool,
    show_map: bool,
    show_visibility: bool,
    seed: Optional[int],
) -> None:
    """Run the GUI."""
    configuration = simulation.configuration.Configuration.from_file(simulation_conf)
    sim = Simulation(configuration)
    gui = Gui(
        key_target_player=sim.human,
        render_settings=RenderSettings(show_bots, show_map, show_visibility),
    )
    gui.initialize()

    start_time = time.time()

    while not sim.is_over() and not Gui.should_quit():
        sim.tick()

        gui.tick()

        gui.handle_key_events()
        gui.handle_mouse_events()

        if gui.is_render_necessary():
            gui.render(sim)

        print_statistics(start_time, sim)

    print()


def print_statistics(start_time: float, simulation: Simulation) -> None:
    """Print statistics about the game."""
    current_time = time.time()
    print(
        f"Ticks: {simulation.tick_count}/{Simulation.MAX_TICKS} \
TPS: {round(simulation.tick_count / ((current_time - start_time)))} \
Players: {simulation.alive_players_count()}        ",
        end="\r",
    )


if __name__ == "__main__":
    cli()
