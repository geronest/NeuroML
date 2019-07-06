import gym


class GymManager:
    def __init__(self, name_env = 'CartPole-v0'):
        self.env = gym.make(name_env)

    def get_env(self):
        return self.env

    

