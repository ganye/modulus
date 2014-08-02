import os
import shlex
import importlib

from exceptions import ModulusError

class Environment(object):
    """
    Base class for creating new `modulus` applications, used for storing
    information about the environment, such as the current module, possible
    arguments for the module, and any currently loaded arguments. Also handles
    the loading of modules and arguments.
    """
    current_module = None
    possible_args = []
    current_args = {}

    def load_module(self, module_source):
        """
        Takes a module path (`module_source`) in dot notation and attempts to 
        store it as the environment's `current_module`. Note that we do not 
        create an instance module at this time. Initialization happens at 
        runtime.
        """
        try:
            module = importlib.import_module(module_source)
        except (ImportError, SyntaxError) as e:
            # Wrap import and syntax errors in ModulusError, so that the
            # application can handle any exceptions without having to know
            # anything about what's going on
            raise ModulusError(e) from e

        try:
            module_cls_name = getattr(module, '__module__')
        except AttributeError:
            # In case __module__ isn't defined, assume the module class is
            # the same as the module file itself, but title case
            module_name = module_source.split('.')[-1]
            module_cls_name = module_name.title()

        try:
            module_cls = getattr(module, module_cls_name)
        except AttributeError:
            raise ModulusError("failed to load module class '{}'".format(
                module_cls_name))

        try:
            module_args = getattr(module_cls, '__args__')
        except AttributeError:
            raise ModulusError("module '{}' has no arguments list".format(
                module_name))

        self.current_module = module_cls
        self.possible_args = module_args

    def set_arg(self, arg_key, arg_value):
        """
        Loads a module argument (`arg_key`) if it is in the list of valid
        arguments for the current module (`possible_args`).
        If there's no current module, raise an exception.
        """
        if self.current_module is None:
              raise ModulusError("cannot set an argument with no module")
        if arg_key in self.possible_args:
            self.current_args[arg_key] = arg_value
        else:
            raise ModulusError("'{}' is not a valid argument".format(arg_key))

    def run_module(self):
        """
        Calls the module callback.
        We create an instance of the module here so that we can pass the
        arguments list to the initializer, and leave any type-checking up to
        the module.
        """
        module = self.current_module(**self.current_args)
        module.callback()
