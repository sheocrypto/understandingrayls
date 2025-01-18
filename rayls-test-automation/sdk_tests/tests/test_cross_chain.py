import pytest
from core.utils.assertions import assert_event_received
from core.utils.helpers import wait_for_event

class TestCrossChainMessaging:
    """Test cases for cross-chain messaging via SDK"""
    
    async def test_send_cross_chain_message(self, sdk_client, test_data):
        """Test sending a message across chains"""
        # Arrange
        message = {
            'source_chain': 'ethereum',
            'target_chain': 'rayls',
            'payload': {'action': 'transfer', 'amount': '100'}
        }
        
        # Act
        tx_hash = await sdk_client.send_message(message)
        event = await wait_for_event(
            sdk_client,
            'MessageDelivered',
            timeout=30
        )
        
        # Assert
        assert tx_hash is not None, "Transaction hash should be returned"
        assert_event_received(
            event,
            expected_source='ethereum',
            expected_target='rayls'
        )
    
    async def test_resource_registration(self, sdk_client):
        """Test registering a new resource for cross-chain access"""
        # Arrange
        resource = {
            'name': 'TestResource',
            'chain': 'ethereum',
            'address': '0x1234567890abcdef1234567890abcdef12345678'
        }
        
        # Act
        result = await sdk_client.register_resource(resource)
        
        # Assert
        assert result['status'] == 'registered'
        assert result['resource_id'] is not None
