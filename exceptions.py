class status_error(BaseException):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return self.value+"Failed to fetch icons. Status code: "