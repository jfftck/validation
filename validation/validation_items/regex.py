import re

from ..validation_items import BaseValidationItem


class RegExValidationItem(BaseValidationItem):
    def __init__(self, regex='.*'):
        self.__regex = regex

    def test(self, value):
        return re.match(self.__regex, value)
