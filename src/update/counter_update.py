from ..model.counter import Counter
from ..message.counter_msg import CounterMessage


def update(msg: CounterMessage, model: Counter) -> Counter:
    """
    Update the counter based on the message received.
    """

    updated = False
    if msg == CounterMessage.INCREMENT:
        model.count += 1
        updated = True
    elif msg == CounterMessage.DECREMENT:
        model.count -= 1
        updated = True
    elif msg == CounterMessage.RESET:
        model.count = 0
        updated = True
    elif msg == CounterMessage.INIT:
        pass

    if updated:
        model.save_to_db()
    return model
