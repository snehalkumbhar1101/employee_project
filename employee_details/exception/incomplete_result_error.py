"""Custom error when result is not complete."""


class IncompleteResultError(Exception):
    """IncompleteResult Error class."""

    def __init__(self, message):
        """Initialize with a message."""
        super().__init__(message)
        self.message = message
