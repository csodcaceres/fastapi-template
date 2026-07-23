from app.exceptions.exceptions import NotFoundException


class ItemNotFoundException(NotFoundException):
    """
    Exception raised when an item is not found.
    """
    pass