from .string_enum import StringEnum
from enum import auto


class DimensionsUnit(StringEnum):
    IN = auto()
    FT = auto()
    MM = auto()
    CM = auto()
    M = auto()