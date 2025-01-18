import pytest
from core.utils.assertions import verify_cross_chain_transfer
from core.utils.helpers import generate_bridge_transaction

class TestCrossChainTransfer:
    def test_asset_bridging(self):
        """Test cross-chain asset transfer functionality"""
        # Arrange
        transfer = generate_bridge_transaction(
            source_chain="ethereum",
            destination_chain="rayls",
            asset_type="ERC20",
            amount=1000
        )

        # Act
        bridge_result = transfer.execute_bridge()
        confirmation = bridge_result.wait_for_confirmation()

        # Assert
        verify_cross_chain_transfer(bridge_result)
        assert confirmation.status == "completed"
        assert confirmation.destination_balance == 1000
        assert confirmation.source_balance == 0

    @pytest.mark.integration
    def test_message_passing(self):
        """Test cross-chain message passing"""
        # Arrange
        message = generate_cross_chain_message(
            source="private_subnet_a",
            destination="private_subnet_b",
            payload="confidential_data"
        )

        # Act
        delivery = message.send()
        verification = delivery.verify_receipt()

        # Assert
        assert delivery.status == "delivered"
        assert verification.integrity_check == "passed"
        assert verification.privacy_maintained
