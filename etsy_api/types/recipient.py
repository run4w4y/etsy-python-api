from .string_enum import StringEnum
from enum import auto


class Recipient(StringEnum):
    MEN = auto()
    WOMEN = auto()
    UNISEX_ADULTS = auto()
    TEEN_BOYS = auto()
    TEEN_GIRLS = auto()
    TEENS = auto()
    BOYS = auto()
    GIRLS = auto()
    CHILDREN = auto()
    BABY_BOYS = auto()
    BABY_GIRLS = auto()
    BABIES = auto()
    BIRDS = auto()
    CATS = auto()
    DOGS = auto()
    PETS = auto()
    NOT_SPECIFIED = auto()
