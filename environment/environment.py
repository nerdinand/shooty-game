import gym
from gym import spaces
from simulation import Simulation
from simulation import PlayerFactory
from simulation import Visibility
import numpy as np
from pygame.math import Vector2
from simulation import Obstacle
from collections import OrderedDict
from gui import Gui

class Environment(gym.Env):
    def __init__(self, with_gui=False):
        super(Environment, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:

        self.with_gui = with_gui

        # W, A, S, D, R, Mouse1, look-, look+
        buttons_space = spaces.MultiBinary(8)
        self.action_space = buttons_space

        positions_space = spaces.Box(low=0.0, high=1.0, shape=(61, 2), dtype=np.float32)
        types_space = spaces.MultiBinary(61)
        self.observation_space = spaces.Dict({
            "positions": positions_space, 
            "types": types_space
        })

        self.player_factory = PlayerFactory()
        self.visibility = Visibility()

    def reset(self):
        self.agent = self.player_factory.agent()
        self.simulation = Simulation(agent=self.agent)
        if self.with_gui:
            self.gui = Gui(key_target_player=self.simulation.human)
            self.gui.initialize()
        return self.__get_observation()

    def step(self, action):
        direction_vector = Vector2()

        if action[0] == 1:
            direction_vector += Vector2(0, -1)
        if action[1] == 1:
            direction_vector += Vector2(-1, 0)
        if action[2] == 1:
            direction_vector += Vector2(0, 1)
        if action[3] == 1:
            direction_vector += Vector2(1, 0)

        if direction_vector.length_squared() != 0.0:
          direction_vector.normalize_ip()

        if action[4] == 1:
            self.agent.gun.start_reload()

        if action[5] == 1:
            self.agent.gun.shoot()

        look_direction = self.agent.look_direction
        if action[6] == 1:
            look_direction = look_direction - 1
        if action[7] == 1:
            look_direction = look_direction + 1
        self.agent.update_look_direction(look_direction)

        for i in range(10):
            self.simulation.tick()

        done = self.simulation.is_over()

        #        72000                      - 5 * 100000
        reward = self.simulation.tick_count - self.simulation.alive_players_count() * 100000

        return self.__get_observation(), reward, done, {}

    def render(self):
        self.gui.tick()
        self.gui.handle_key_events()
        self.gui.handle_mouse_events()
        if self.gui.is_render_necessary():
            self.gui.render(self.simulation)

    def __get_observation(self):
        visible_points = self.visibility.get_visible_points(self.simulation, self.agent)
        return OrderedDict([
            ('positions', np.array([(p.position.x, p.position.y) for p in visible_points])), 
            ('types', np.array([(0 if isinstance(p, Obstacle) else 1) for p in visible_points]))
        ])
