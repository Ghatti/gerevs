class CancelOperationException(ValueError):
    def __init__(self):
        super().__init__("A operação foi cancelada.")
