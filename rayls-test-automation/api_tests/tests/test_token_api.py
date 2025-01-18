import pytest
from http import HTTPStatus
from core.utils.assertions import assert_response
from core.utils.helpers import generate_token_params

class TestTokenAPI:
    """Test cases for Token Management API endpoints"""
    
    def test_create_token_success(self, api_client, test_data):
        """Test successful token creation with valid parameters"""
        # Arrange
        token_params = generate_token_params(test_data['token'])
        
        # Act
        response = api_client.post('/v1/tokens', json=token_params)
        
        # Assert
        assert_response(
            response,
            expected_status=HTTPStatus.OK,
            schema='token_creation_response.json'
        )
        assert response.json()['token']['symbol'] == test_data['token']['symbol']
    
    def test_token_transfer(self, api_client, test_data):
        """Test token transfer between accounts"""
        # Arrange
        transfer_params = {
            'from': test_data['accounts']['test_wallet'],
            'to': test_data['accounts']['test_contract'],
            'amount': '1000000000000000000'  # 1 token
        }
        
        # Act
        response = api_client.post('/v1/tokens/transfer', json=transfer_params)
        
        # Assert
        assert_response(
            response,
            expected_status=HTTPStatus.OK,
            schema='token_transfer_response.json'
        )
        assert response.json()['status'] == 'success'
