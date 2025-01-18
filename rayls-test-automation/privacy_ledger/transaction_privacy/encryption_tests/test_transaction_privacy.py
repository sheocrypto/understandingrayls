import pytest
from core.utils.assertions import verify_encryption
from core.utils.helpers import generate_transaction

class TestTransactionPrivacy:
    def test_end_to_end_encryption(self):
        """Test end-to-end encryption of private transactions"""
        # Arrange
        transaction = generate_transaction(
            sender="institution_a",
            receiver="institution_b",
            amount=1000,
            privacy_level="maximum"
        )

        # Act
        encrypted_tx = transaction.encrypt()
        delivered_tx = transaction.send()
        decrypted_tx = delivered_tx.decrypt(receiver="institution_b")

        # Assert
        verify_encryption(encrypted_tx)
        assert decrypted_tx.amount == 1000
        assert decrypted_tx.sender == "institution_a"
        assert not delivered_tx.is_visible_to("institution_c")


