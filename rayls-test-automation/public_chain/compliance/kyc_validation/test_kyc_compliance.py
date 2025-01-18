import pytest
from core.utils.assertions import verify_kyc_compliance
from core.utils.helpers import generate_kyc_data

class TestKYCCompliance:
    def test_account_verification(self):
        """Test KYC verification for new account creation"""
        # Arrange
        kyc_data = generate_kyc_data(
            identity_type="individual",
            risk_level="medium",
            jurisdiction="US"
        )

        # Act
        verification = kyc_data.submit_verification()
        account = verification.create_account()

        # Assert
        verify_kyc_compliance(verification)
        assert verification.status == "approved"
        assert account.kyc_status == "verified"
        assert account.risk_rating == "medium"

    
