import ecdsa
from key_pair import KeyPair
from transaction import Transaction, TransactionInput, TransactionOutput
from crypt_utils import hash_object, hash160
from hashlib import sha256
from ecdsa.util import sigencode_string, sigdecode_string, sigencode_der


class Wallet():
    """
    A class to store (as a wallet) key chain composed of private and public keys
    """

    _key_chain: dict[str, KeyPair] = {}

    def __init__(self, key_pair: list[KeyPair] = None) -> None:
        if key_pair is None:
            key_pair = [KeyPair("default")]
        for kp in key_pair:
            self.add_key_pair(kp)

    def add_key_pair(self, key_pair: KeyPair) -> None:
        """
        Add a known key pair to the key chain of the wallet
        """
        if key_pair.name in self.key_chain:
            key_name = key_pair.name+"_"+str(len(self.key_chain))
            self.key_chain[key_name] = key_pair
            self.key_chain[key_name].name = key_name
        else:
            self.key_chain[key_pair.name] = key_pair

    def sign(self, data: bytes, key_chain_name: str) -> bytes:
        """
        Sign data with the private key
        """
        private_key = self.key_chain[key_chain_name].private_key
        return private_key.sign_digest_deterministic(data, sigencode=sigencode_string,
                                                     hashfunc=sha256)

    def verify(self, hash: bytes, signature: str, key_chain_name: str) -> bool:
        """
        Verify the signature of hash with the public key
        """
        public_key = self.key_chain[key_chain_name].public_key
        return public_key.verify_digest(signature, hash)

    @property
    def key_chain(self) -> dict[str, KeyPair]:
        """
        Return the key chain of the wallet
        """
        return self._key_chain

    def create_transaction(self, outputs_addr: list[TransactionOutput],
                           inputs_addr: list[TransactionInput], key_chain_name: str) -> Transaction:
        """
        Create a transaction with the given value and outputs
        """

        # As each inputs spends a previous output,
        # the sender's public key will be used to verify
        # that the sender is the owner of locked coins from unspent transaction outputs (UTXOs)
        # (coins received from previous transactions and used as source for the current one)
        # It will be used to verify the ownership of the inputs (source of value) of the transaction
        src_pub_key = self.key_chain[key_chain_name].public_key.to_string()

        # the recipient's public key will be used to lock the coins to its address

        # It will be added to the transaction output (destination of the value)

        # source of value to spend
        inputs = []

        # create inputs of the transaction
        # (inputs are previous transaction used as source of funds - UTXOs)
        for input_addr in inputs_addr:
            transaction_input = input_addr
            # ~ScriptSig: public key and signature
            transaction_input.full_public_key = src_pub_key
            transaction_input.digital_signature = self.key_chain[key_chain_name].address.public_address
            # The sender's private key will be used to unlock value used in each transaction.
            # To unlock the amount that holds the current input_addr, we provide:
            # 1) a digital signature:
            #       It's calculated with the private key and
            #       the hash of the transaction source of funds and its index
            # 2) the public key of the sender
            digital_signature = self.sign(
                hash_object(input_addr), key_chain_name)
            # ~ScriptSig
            transaction_input.digital_signature = digital_signature
            inputs.append(transaction_input)

        transaction = Transaction(inputs, outputs_addr)
        transaction.id = hash_object(transaction)
        return transaction

    def public_address(self, key_chain_name: str = "default") -> bytes:
        """
        Return the public address of the wallet
        """
        return self.key_chain[key_chain_name].address.public_address
