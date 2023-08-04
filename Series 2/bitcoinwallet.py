import base58
import hashlib
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def generate_ecdsa_keys():
    private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def generate_bitcoin_address(public_key):
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.UncompressedPoint
    )
    public_key_hash = hashlib.sha256(public_key_bytes).digest()
    wallet_address = base58.b58encode_check(b"\x00" + public_key_hash).decode()
    return wallet_address

# Generate ECDSA keys
private_key, public_key = generate_ecdsa_keys()

# Generate Bitcoin wallet address
wallet_address = generate_bitcoin_address(public_key)

print("Private Key:", private_key)
print("Public Key:", public_key)
print("Bitcoin Wallet Address:", wallet_address)
