import hashlib


class This():
    str_var: str
    int_var: int
    float_var: float
    bool_var: bool
    list_var: list
    dict_var: dict
    tuple_var: tuple
    set_var: set
    id: str

    def __init__(self):
        self.str_var = 'str'
        self.int_var = 11
        self.float_var = 1.1
        self.bool_var = True
        self.list_var = [1, 2, 3]
        self.dict_var = {'a': 1, 'b': 2}
        self.tuple_var = (1, 2, 3)
        self.set_var = {1, 2, 3}
        self.id = self.get_id()

    def __str__(self):
        res = ""
        for key in sorted(self.__dict__.keys()):
            res += f"{key}: {str(self.__dict__[key]).encode()}\n"
        return res

    def get_id(self):
        _id = ""
        for key in sorted(self.__dict__.keys()):
            if key == "id":
                continue
            _id += hashlib.sha256(str(self.__dict__[key]).encode()).hexdigest()
        self.id = hashlib.sha256(_id.encode()).hexdigest()
        return self.id


if __name__ == "__main__":
    this = This()
    print(this.get_id())
