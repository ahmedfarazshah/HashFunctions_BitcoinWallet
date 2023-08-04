import hashlib
import random
import hashlib
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


def generateTxid():
    random_int = random.randint(0, 9999999999)
    random_str = str(random_int)
    hash_object = hashlib.sha256(random_str.encode())
    hex_digest = hash_object.hexdigest()
    return hex_digest


def generateInput():
    prevTxid = generateTxid()
    prevOutputIndex = random.randint(0, 5)
    return prevTxid, prevOutputIndex


def generateOutput():
    recipientAddress = 'recipient_address_' + str(random.randint(1, 100))
    amount = round(random.uniform(0.001, 1.0), 8)
    return recipientAddress, amount


def generateTransactionFee():
    return round(random.uniform(0.0001, 0.001), 8)


def generateRandomTransaction():
    txid = generateTxid()
    inputPrevTxid, inputPrevOutputIndex = generateInput()
    outputRecipientAddress, outputAmount = generateOutput()
    transactionFee = generateTransactionFee()
    return ( txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee)

def  concatenateString(txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee):
    transactionData = str(txid) + str(inputPrevTxid) + str(inputPrevOutputIndex) + str(outputRecipientAddress) + str(outputAmount) + str(transactionFee)
    str(transactionData)
    return transactionData

def generateECDSAKeyPair():
    private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key


def ECDSASign(privateKey, message):
    signature = privateKey.sign(message, ec.ECDSA(hashes.SHA256()))
    return signature


def ECDSAVerify(publicKey, message, signature):
    try:
        publicKey.verify(signature, message, ec.ECDSA(hashes.SHA256()))
        return True
    except:
        return False


def main():
    txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee = generateRandomTransaction()
    transactionDataAsMessage = concatenateString(txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee).encode()
    transactionDataAsMessageSHA256Hashed = hashlib.sha256(transactionDataAsMessage).digest()
    ECDSAPrivateKey, ECDSAPublicKey = generateECDSAKeyPair()
    signature = ECDSASign(ECDSAPrivateKey, transactionDataAsMessageSHA256Hashed)
    verified = ECDSAVerify(ECDSAPublicKey, transactionDataAsMessageSHA256Hashed, signature)

    print("------------------------------------------------------------ECDSA----------------------------------------------")
    print("ECDSA Public Key:", ECDSAPublicKey.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))
    print("ECDSA Private Key:", ECDSAPrivateKey.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption()))
    print("transaction Data As Message SHA256 Hashed:", transactionDataAsMessageSHA256Hashed.hex())
    print("Signature:", signature.hex())
    print("Verification:", verified)


main()