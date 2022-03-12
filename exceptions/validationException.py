class ValidationException(ValueError):
    def __init__(self, err_msg="Houve um erro de valicação."):
        super().__init__(err_msg)
