import pytest
from core.utils.assertions import verify_hsm_integration
from core.utils.helpers import generate_key_pair

class TestHSMKeyManagement:
    def test_secure_key_generation(self):
        """Test secure key generation through HSM"""
        # Arrange
        key_specs = {
            "type": "BIP32",
            "strength": "256bit",
            "backup_required": True
        }

        # Act
        key_pair = generate_key_pair(hsm=True, **key_specs)
        derived_keys = key_pair.derive_child_keys(count=5)

        # Assert
        verify_hsm_integration(key_pair)
        assert key_pair.is_hsm_backed
        assert len(derived_keys) == 5
        for key in derived_keys:
            assert key.verify_derivation_path()

    def test_key_rotation(self):
        """Test zero-downtime key rotation"""
        # Arrange
        original_key = generate_key_pair(hsm=True)
        accounts = original_key.get_associated_accounts()

        # Act
        new_key = original_key.initiate_rotation()
        rotation_result = new_key.complete_rotation()

        # Assert
        assert rotation_result.success
        assert rotation_result.downtime_duration == 0
        for account in accounts:
            assert account.verify_access(new_key)
            assert not account.verify_access(original_key)

    @pytest.mark.security
    def test_multi_signature_setup(self):
        """Test multi-signature HSM key configuration"""
        # Arrange
        required_signatures = 3
        total_signers = 5
        
        # Act
        multi_sig = generate_key_pair(
            hsm=True,
            multi_sig=True,
            required_signatures=required_signatures,
            total_signers=total_signers
        )
        
        # Assert
        assert multi_sig.verify_multi_sig_setup()
        assert multi_sig.required_signatures == required_signatures
        assert len(multi_sig.signers) == total_signers
        assert multi_sig.is_hsm_backed
