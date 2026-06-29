class AppException(Exception):
    def __init__(
        self,
        message: str = "业务异常",
        code: int = 400,
        status_code: int = 400,
    ):
        self.message = message
        self.code = code
        self.status_code = status_code
