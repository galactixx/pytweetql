class APIResponseParseError(Exception):
    """
    Error for irregular parsing of API response provided.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)