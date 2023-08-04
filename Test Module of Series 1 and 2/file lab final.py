import hashlib
def hashing(msg):
    sha256 = hashlib.sha256()
    sha256.update(msg.encode('utf-8'))
    return sha256.hexdigest()

def prog(sender, recipient, subject, body, nonce):
    msg = sender + recipient + subject + body + nonce
    attempts = 0
    while True:
        attempts += 1
        hash_result = hashing(msg)
        if hash_result[:2] == "ff":
            break
        nonce += 1
        msg = sender + recipient + subject + body + str(nonce)

    return attempts, hash_result
    
def prog2(sender, recipient, subject, body, nonce):
    msg = sender + recipient + subject + body + nonce
    attempts = 0
    while True:
        attempts += 1
        hash_result = hashing(msg)
        if hash_result[:4] == "ffff":
            break
        nonce += 1
        msg = sender + recipient + subject + body + str(nonce)
    return attempts, hash_result
sender_email = "hasnianbunjivi@gmail.com"
recipient_email = "nust_blockchain@nust.com"
email_subject = "Hello"
email_body = "This is final results of lab task final."
nonce = 0
attempts_prog, hash_result_prog = prog(sender_email, recipient_email, email_subject, email_body, nonce)
print("Task 1 - Attempts:", attempts_prog)
print("Task 1 - Hash Result:", hash_result_prog)
attempts_prog2, hash_result_prog2 = prog2(sender_email, recipient_email, email_subject, email_body, nonce)
print("Task 2 - Attempts:", attempts_prog2)
print("Task 2 - Hash Result:", hash_result)