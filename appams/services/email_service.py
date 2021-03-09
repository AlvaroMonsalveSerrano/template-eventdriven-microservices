import logging


def send_mail(*args) -> bool:
    logging.info(f"Send mail to:{args[0]} subject:{args[1]} operation:{args[2]}. Message: Operation '{args[2]}' not valid.")
    return True
