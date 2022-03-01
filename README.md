# shooty-game
[![Python](https://github.com/nerdinand/shooty-game/actions/workflows/python.yml/badge.svg)](https://github.com/nerdinand/shooty-game/actions/workflows/python.yml)

Game/Simulation which is a 2D-analog of Counter Strike as a target for Deep Reinforcement Learning.

## Setup

This uses [Poetry](https://python-poetry.org/) as a dependency manager. Python 3.9+ is supported. To install the dependencies just run:

```shell
pip install poetry
poetry install
```

## Usage

```
Usage: shooty.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  gui
  sim
```

shooty.py has 2 subcommands, `gui` and `sim`.

```
Usage: shooty.py gui [OPTIONS]

Options:
  --with-human                    Run simulation with a human (controllable
                                  with keyboard).
  --bot-count INTEGER             How many bots to spawn.
  --show-bots / --hide-bots       Show bots in GUI.
  --show-map / --hide-map         Show map (obstacles) in GUI.
  --show-visibility / --hide-visibility
                                  Show visibility (FOV cone and visible
                                  points) in GUI.
  --help                          Show this message and exit.
```

```
Usage: shooty.py sim [OPTIONS]

Options:
  --bot-count INTEGER  How many bots to spawn.
  --help               Show this message and exit.
```

If run with UI activated, this is what you should see:

![Screenshot of the Shooty GUI](doc/shooty-gui.png)

You can move the blue player with WASD, aim and shoot with the mouse, R is reload.

## Development

We use a bunch of utilities to ensure code quality. Run them like this:

```bash
poetry run bin/check.sh
```

## To Do

* [x] Write an adapter for [OpenAI Gym](https://gym.openai.com/) to test with a baseline RL algorithm
* [x] Write more tests for simulation part
* [ ] Add own position, health and bullets to observation
* [ ] Train a model that does something reasonable
* [ ] Parallelise training
* [ ] Describe training and playback in README
* [ ] Document ALL the things!

## License

__MIT License__

```
Copyright 2021 Ferdinand Niedermann

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
