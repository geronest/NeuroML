

class DataManager:
    def __init__(self, type_learning = 'RL-gym', name_data = 'CartPole-v0'):
        self.config = {
                        'type_learning': type_learning,
                        'name_data': name_data
                        }

        self.manager = None
        self.env = None # For RL
        self.data = None # For other data

        if type_learning == 'RL_gym':
            import data.gym.env_gym as eg
            self.manager = eg.GymManager(name_data)
            self.env = self.manager.get_env()

        if type_learning == 'SL':
            pass
    
    def get_config(self):
        return self.config

    def get_env(self):
        return self.env

    def get_batch(self, type_data = 'train'):
        pass


