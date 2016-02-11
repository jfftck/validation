from abc import abstractmethod, ABCMeta


class BaseValidator(object):
    __metaclass__ = ABCMeta

    VALID = 1
    INVALID = 2
    TRANSITIONAL = 3

    def __init__(self):
        self.__callback = None
        self.__validation_item = None
        self.__validation_state = self.TRANSITIONAL

    def change_validation_state(self, state):
        if state != self.__validation_state:
            self.__validation_state = state
            self.validation_state_changed(state)

    def set_callback(self, callback):
        self.__callback = callback

    def validation_state(self):
        return self.__validation_state

    def validation_state_changed(self, state):
        if hasattr(self.__callback, "__call__"):
            self.__callback(state)
        else:
            raise ValueError('Callback is unset.')

    @abstractmethod
    def valid(self, value):
        pass
