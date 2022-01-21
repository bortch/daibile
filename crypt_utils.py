import hashlib


def sha256d(data: str) -> str:
    return hashlib.sha256(hashlib.sha256(data.encode()).digest()).hexdigest()


def checksum(data: str) -> str:
    """This function returns as a checksum the last 4 characters of the sha256 hash of data"""
    return sha256d(data)[:8]


def is_checksum_valid(data: str) -> bool:
    """This function returns True if the checksum is valid"""
    return checksum(data) == data[-8:]


def add_checksum(data: str) -> str:
    """This function returns data with a checksum"""
    return data + checksum(data)


def hash160(data: str) -> str:
    """This function is used to hash the public key"""
    return hashlib.new('ripemd160', hashlib.sha256(data.encode()).digest()).hexdigest()
