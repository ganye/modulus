from .environment import Environment
from exceptions import ModulusError
from colors import *

class Console(Environment):
    commands_list = {}

    def load_config(self):
        pass

    def load_commands(self):
        self.commands_list.update({
            'load': self.load_module,
            'set': self.set_arg,
            'run': self.run_moudle,
            'quit': exit,
        })

    def prompt_info(self):
        if self.current_module is not None:
            prompt = LightRed("> ")
        else:
            prompt = Green("(") + LightGreen(self.current_module) + \
                    Green(")") + Red(" > ")
        return input(prompt)

    def enter_input_loop(self):
        while True:
            user_input = self.prompt_input()
            self.handle_input(user_input)

    def start(self):
        self.load_config()
        self.load_commands()
        self.enter_input_loop()
