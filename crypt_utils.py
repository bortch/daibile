import hashlib


def sha256d(data: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


def checksum(data: bytes) -> bytes:
    """This function returns as a checksum the last 4 characters of the sha256 hash of data"""
    value = sha256d(data)
    return value[-8:]


def is_checksum_valid(data: bytes) -> bool:
    """This function returns True if the checksum is valid"""
    return checksum(data) == data[-8:]


def add_checksum(data: bytes) -> bytes:
    """This function returns data with a checksum"""
    return data + checksum(data)


def hash160(data: str) -> str:
    """This function is used to hash the public key"""
    return hashlib.new('ripemd160', hashlib.sha256(data.encode()).digest()).hexdigest()


def hash_object(data: object, excludes: list[str] = []) -> bytes:
    """this method is used to hash the record twice. 
    Ferguson and Schneier says it makes SHA-256 invulnerable 
    to 'length-extensio' attack"""
    h = b""
    for key in sorted(data.__dict__.keys()):
        if key in excludes:
            continue
        h += str(data.__dict__[key]).encode()
    h = bytes(h)
    return sha256d(h)
