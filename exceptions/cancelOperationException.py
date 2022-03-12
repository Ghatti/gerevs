class CancelOperationException(StopIteration):
    def __init__(self, err_msg="A operação foi cancelada."):
        super().__init__(err_msg)
