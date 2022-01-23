import unittest
from transaction import Transaction, TransactionInput, TransactionOutput
from record_type import RecordType


class TestTransaction(unittest.TestCase):
    pass
    # def test_transaction_creation(self):
    #     inputs = [TransactionInput(transaction_id="previous_transaction_hash", output_index=0)]
    #     outputs = [TransactionOutput(value=10, src_pub_key="my_public_key")]
    #     transaction = Transaction(inputs, outputs, amount)
    #     self.assertEqual(transaction.sender, sender)
    #     self.assertEqual(transaction.recipient, recipient)
    #     self.assertEqual(transaction.amount, amount)
    #     self.assertEqual(transaction.type, RecordType.TRANSACTION)

    # def test_transaction_creation_with_invalid_sender(self):
    #     with self.assertRaises(ValueError):
    #         Transaction("", "recipient", 10)

    # def test_transaction_creation_with_invalid_recipient(self):
    #     with self.assertRaises(ValueError):
    #         Transaction("sender", "", 10)

    # def test_transaction_creation_with_invalid_amount(self):
    #     with self.assertRaises(ValueError):
    #         Transaction("sender", "recipient", -10)

    # def test_transaction_creation_with_invalid_amount_type(self):
    #     with self.assertRaises(ValueError):
    #         Transaction("sender", "recipient", "10")

    # def test_transaction_creation_with_invalid_precision(self):
    #     with self.assertRaises(ValueError):
    #         Transaction("sender", "recipient", 10, precision=0)

    # def test_transaction_creation_with_invalid_precision_type(self):
    #     with self.assertRaises(ValueError):
    #         Transaction("sender", "recipient", 10, precision="0")


if __name__ == '__main__':
    unittest.main()
