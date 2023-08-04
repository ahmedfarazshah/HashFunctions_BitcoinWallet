#string of file hash sha 256 (c27783392976304d9ec296c6cf318f4145e780d02b78c679347e93408553a59c)

import hashlib

cal_hash = ('c27783392976304d9ec296c6cf318f4145e780d02b78c679347e93408553a59c')

filename = 'd:/BlockChain/Lab 5/Lab5-6-2023.pdf'
with open(filename, "rb") as file:
    file_cont = file.read()
    matched = hashlib.sha256(file_cont).hexdigest()

if matched == cal_hash : 
    print ("hashes match")

else :
    print ("hashes don't match")

print (matched)


                        # Task # 02

filename_02 = 'd:/BlockChain/Lab 5/sample2.txt'
with open ( filename_02, 'rb') as file:
    newtohash = file.read()
    newhash = hashlib.sha256(newtohash).hexdigest()

print(newhash)


                    # Task #03


toget = 'd:/BlockChain/Lab 5/message1.bin'
with open (toget, 'r') as file:
    readtoget = file.read()
    hashrtg = hashlib.md5(readtoget.encode()).hexdigest()
print(hashrtg)

toget = 'd:/BlockChain/Lab 5/message1.bin'
with open (toget, 'r') as file:
    readtoget = file.read()
    hashrtg5 = hashlib.sha1(readtoget.encode()).hexdigest()
print(hashrtg5)

        # .................


toget2 = 'd:/BlockChain/Lab 5/message2.bin'
with open (toget2, 'r') as file:
    readtogett = file.read()
    hashrtg2 = hashlib.sha1(readtogett.encode()).hexdigest()

print(hashrtg2)

toget2 = 'd:/BlockChain/Lab 5/message2.bin'
with open (toget2, 'r') as file:
    readtogett = file.read()
    hashrtg0 = hashlib.md5(readtogett.encode()).hexdigest()
print(hashrtg0)



# md5 have collisions so it is not given a lisence :D