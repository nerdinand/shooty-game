# shooty-game
Game/Simulation that's supposed to become a 2D-analog of Counter Strike as a target for Deep Reinforcement Learning.

## Setup

This uses [Poetry](https://python-poetry.org/) as a dependency manager. Python 3.9+ is supported. To install the dependencies just run:

```shell
pip install poetry
poetry install
```

## Usage

Run like this:

```shell
poetry run python shooty.py
```

If run with UI activated, this is what you should see:

<Insert image here>

## To Do

* [ ] Visibility checking for players: Only show obstacles and opponents in the field of view
* [ ] Write an adapter for [OpenAI Gym](https://gym.openai.com/) to test with a baseline RL algorithm

## License

__MIT License__

```
Copyright 2021 Ferdinand Niedermann

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
