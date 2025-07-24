from enum import Enum, auto


class CounterMessage(Enum):
    INCREMENT = auto()
    DECREMENT = auto()
    RESET = auto()
    INIT = auto()
