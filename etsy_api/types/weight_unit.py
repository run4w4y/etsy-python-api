from .string_enum import StringEnum
from enum import auto


class WeightUnit(StringEnum):
    OZ = auto()
    LB = auto()
    G = auto()
    KG = auto()
