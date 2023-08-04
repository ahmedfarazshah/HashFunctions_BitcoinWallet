import hashlib

sender = 'umairjavaidmanj@gmail.com'
recipent = 'ahmedfarazshah42@gmail.com'
subject = 'module-1 final assessment'
messagebody = 'this is the work that i have tried'
nonce = 0
container = sender + recipent + subject + messagebody + nonce
hash1 = hashlib.sha256(container.encode()).hexdigest()

def prog(hash1):
    attempts = 0
    while True:
        attempts=attempts+1
        hash_result = hashing(hash1)
        if hash_result[:2] == "ff":
            break
    nonce += 1
	container
    return attempts, hash_result

task1 = prog(hash1)

def prog2(hash1):
    attempts = 0
    while True:
        attempts += 1
        hash_result = hashing(hash1)
        if hash_result[:2] == "ffff":
            break
        nonce += 1
		container
    return attempts, hash_result

task2 = prog2(hash1)

print(task1)
print(task2)


# task 3

task = 'adding a value in the nonce will change the whole hash value as well as its difficulty level  have seen it in task1 and task2'
