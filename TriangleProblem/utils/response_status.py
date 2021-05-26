STATUS = {
    # 2xx
    200: 'OK',
    # 3xx
    # 4xx
    400: 'Bad Request',
    404: 'Not Found'
}

def get_status(cls, code: int) -> str:
    return cls.STATUS.get(code, 'Invalid')


