from ..validation_items import BaseValidationItem
from ..validators import BaseValidator


class TextValidator(BaseValidator):
    def __init__(self, validation_item):
        super(TextValidator, self).__init__()

        if not issubclass(validation_item, BaseValidationItem):
            raise ValueError('Invalid validation item.')

        self.__validation_item = validation_item

    def valid(self, value):
        if self.__validation_item.test(unicode(value)):
            self.change_validation_state(self.VALID)
        elif value:
            self.change_validation_state(self.INVALID)
        else:
            self.change_validation_state(self.TRANSITIONAL)
