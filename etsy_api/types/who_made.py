from .string_enum import StringEnum
from enum import auto


class WhoMade(StringEnum):
    I_DID = auto()
    COLLECTIVE = auto()
    SOMEONE_ELSE = auto()