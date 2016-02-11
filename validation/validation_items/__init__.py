from abc import abstractmethod, ABCMeta


class BaseValidationItem(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def test(self, value):
        pass
