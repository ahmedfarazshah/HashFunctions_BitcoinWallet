# import bcrypt;
import hashlib;

# string

Name_id = 'hmed'

# convert to encode

Convert_id=Name_id.encode()

print(Convert_id)


# bcrypt_name = bcrypt.hashpw(Name_id.encode(), bcrypt.gensalt()).decode()
#MD-5

# print(bcrypt_name)

Blake2  = hashlib.blake2b(Name_id.encode()).hexdigest()
#MD-5
print(Blake2)


md5_name  = hashlib.sha256(Name_id.encode()).hexdigest()
#MD-5
print(md5_name)

sha_512  = hashlib.sha512(Name_id.encode()).hexdigest()
#MD-5
print(sha_512)

sha_256  = hashlib.sha256(Name_id.encode()).hexdigest()
print(sha_256)

Sha_1  = hashlib.sha1(Name_id.encode()).hexdigest()
print(Sha_1)

#sha-1
ripemd160_Name = hashlib.new("ripemd160", Name_id.encode()).hexdigest()
print(ripemd160_Name) 

 