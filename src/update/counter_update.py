from ..model.counter import Counter
from ..message.counter_msg import CounterMessage


def update(msg: CounterMessage, model: Counter) -> Counter:
    """
    Update the counter based on the message received.
    """

    if msg == CounterMessage.INCREMENT:
        model.count += 1
    elif msg == CounterMessage.DECREMENT:
        model.count -= 1
    elif msg == CounterMessage.RESET:
        model.count = 0
    elif msg == CounterMessage.INIT:
        pass

    return model
