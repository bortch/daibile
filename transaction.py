from record_interface import RecordInterface
from record_type import RecordType


class Transaction(RecordInterface):

    _type: RecordType = RecordType.TRANSACTION
    _data: dict = {"sender": "", "recipient": "", "amount": 0, "precision": 4}

    def __init__(self, sender: str, recipient: str, amount: int, precision: int = 4) -> None:
        super().__init__(self._type, self._data)
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.precision = precision

    @property
    def sender(self) -> str:
        return self.data['sender']

    @property
    def recipient(self) -> str:
        return self.data['recipient']

    @property
    def amount(self) -> int:
        return self.data['amount']

    @property
    def type(self) -> RecordType:
        return self._type

    @property
    def precision(self) -> int:
        return self.data['precision']

    @sender.setter
    def sender(self, value: str):
        try:
            if not value or not isinstance(value, str):
                raise ValueError('empty string or not a string')
        except ValueError:
            raise ValueError('sender must be a non-empty string')
        self.data['sender'] = value

    @recipient.setter
    def recipient(self, value: str):
        try:
            if not value or not isinstance(value, str):
                raise ValueError('empty string or not a string')
        except ValueError:
            raise ValueError('recipient must be a non-empty string')
        self.data['recipient'] = value

    @amount.setter
    def amount(self, value: int):
        try:
            if not value or not isinstance(value, int) or value < 0:
                raise ValueError('empty or zero amount or not an int')
        except ValueError:
            raise ValueError('amount must be a non-empty int greater than 0')
        self.data['amount'] = value

    @precision.setter
    def precision(self, value: int):
        try:
            if not value or not isinstance(value, int) or value < 0:
                raise ValueError('empty or zero amount or not an int')
        except ValueError:
            raise ValueError('precision must be an int >= 0')
        self.data['precision'] = value
