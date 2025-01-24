import pytest
import boto3
from eth_account.messages import encode_defunct
import os

def test_awskms_sign_integration():
    """Integration test with real AWS KMS.
    
    Required:
        - AWS credentials configured (via env vars, config file, or IAM role)
        - AWS_KMS_KEY_ID: KMS key ID or ARN
    Optional:
        AWS_REGION: AWS region (defaults to system configuration)
    """
    try:
        from eth_signer.signer import AWSKMSKey
        from eth_account import Account
        
        if not os.getenv('AWS_KMS_KEY_ID'): pytest.skip("AWS KMS key ID not configured")
        
        key = AWSKMSKey(kms_client=boto3.client('kms', region_name=os.getenv('AWS_REGION')), 
                        key_id=os.getenv('AWS_KMS_KEY_ID'))
        
        message = encode_defunct(text="Hello, AWS KMS!")
        signature = key.sign_message(message).signature
        assert len(signature) == 65  # R (32 bytes) + S (32 bytes) + V (1 byte)
        assert Account.recover_message(message, signature=signature).lower() == key.address.lower()
    except ImportError as e:
        pytest.fail(f"Failed to import AWSKMSKey: {str(e)}") 