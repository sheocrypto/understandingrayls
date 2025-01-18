"""Helper functions for Rayls test automation framework."""

from datetime import datetime
from typing import List, Dict, Any, Optional
from enum import Enum

def generate_transaction(
    sender: str = None,
    receiver: str = None,
    amount: float = 0,
    privacy_level: str = "standard",
    type: str = "standard",
    participants: List[str] = None,
    amounts: List[float] = None,
    source: str = None,
    frequency: str = "normal"
) -> 'Transaction':
    """Generate a test transaction with specified parameters."""
    transaction = Transaction(
        sender=sender,
        receiver=receiver,
        amount=amount,
        privacy_level=privacy_level,
        type=type,
        participants=participants,
        amounts=amounts,
        source=source,
        frequency=frequency
    )
    return transaction

def generate_kyc_data(
    identity_type: str,
    risk_level: str,
    jurisdiction: str
) -> 'KYCData':
    """Generate test KYC data for verification."""
    return KYCData(
        identity_type=identity_type,
        risk_level=risk_level,
        jurisdiction=jurisdiction
    )

