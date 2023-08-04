# Modulues form the crytolibrary
from cryptography.hazmat.primitives.asymmetric import rsa, dsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives import padding

text = ("this text needs to be encrypted using rsa and dsa")

# with open(text, "rb") as temp:
#     file = temp.read()
# Not need to convert into binary as the text/string value have pre-determined value

public_exponent= 65537
key_size = 2048

privatekey = rsa.generate_private_key(public_exponent, key_size)
print ("private",privatekey)

# # 0x00000274D1D2F650 private key 0000026822BAF650
# privatekey.public_key()
# publickey = '0x0000026DE6AFF690'