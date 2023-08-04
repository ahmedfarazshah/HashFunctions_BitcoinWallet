import hashlib

file = "d:/BlockChain/Lab No 6/2.1 Building Blocks - Hash structures, signatures, and coins (3).pptx"

# Determining and spliting the file as per block size
blocksize = len(file) // 8 
datablocks = [file[i:i+blocksize]for i in range(0, len(file), blocksize)]
print (datablocks)

block1 = 'd:/BlockCha'
block2 = 'in/Lab No 6'
block3 = '/2.1 Buildi'
block4 = 'ng Blocks -'
block5 = ' Hash struc'
block6 = 'tures, sign'
block7 = 'atures, and'
block8 = ' coins (3).'
block9 = 'pptx'

hashb = hashlib.sha256(block9.encode()).hexdigest()
print(hashb)

blockhash1 = 'ccc238072bef11dd4f039bc13b2d1e0c95680744585ae3782ada5ec8aa5a0d24'
blockhash2 = 'b009f60f4c91f361e9ba09bf3d2b29cf4c555868645414a3e9d1e443cfdf9ebd'
blockhash3 = '99f3f2a54be9632865fbfcd01ce32a5fbfe7382814973d29d9b3017ddb26c476'
blockhash4 = 'a80909d54662c9676e8901287bb256559acd87f962b9708c50ce417124514784'
blockhash5 = '94e90266fcc1957222bc800cc6bbc54066170700bd468d32723d437250e67b19'
blockhash6 = 'a698533943cd5c8155d61f0c1676586617114302c8c5445b0fb9a9e4e03191b3'
blockhash7 = '6400a5543fc1ad0b132d8c78fcfcf6788be6e172babcc07b2854dabf99eafa7a'
blockhash8 = '2c0127e4131283769e34767db0cc488f2e3533d97b5df1e46ad768ac6cc6d49d'
blockhash9 = '1512e97a4b84b0da4f2fba9d03ae3dfacc9de18a722276c8726df9f87d51698c'

# sum of the hashes

bh12 =  blockhash1 + blockhash2
bh34 = blockhash3 + blockhash4
bh56 = blockhash5 + blockhash6
bh78 = blockhash7 + blockhash8


# now hashes of the above

hashb1 = hashlib.sha256(bh78.encode()).hexdigest()
print(hashb1)

hash_bh12 = 'f92d2717e68ef241d3ac56fa8928ecf7a05a1378346a4c6b553709abed25dc33'
hash_bh34 = 'd3ff9b36ff062783d142ed4cf54d9a60fce266475e6ac956178ec3d31ac4e762'
hash_bh56 = '62ad0119192d5fd8ab5b9df47b9f80eca0c23e850c64c06f6344d50ceed376b8'
hash_bh78 = '398a5fa99e3dad83c2cd0164dbe79a26232d8b2caea5e63927e3ad41f5f14e73'

# sum of the above hashes

sh1234 = hash_bh12 + hash_bh34
sh5678 = hash_bh56 + hash_bh78

# now hashes of the above sum

hashb2 = hashlib.sha256(sh5678.encode()).hexdigest()
print(hashb2)

hash_sh1234 = 'd53d2448455276e14597878981f60e47f5475a9a79185a0c02a6b2ebdedf3860'
hash_sh5678 = 'fd7ba6aa52d8cc5be622ccc9a4660edd235b3454480ca4e84d893d2ef04e7bc5'
# sum of the above

sum1to8 = hash_sh1234 + hash_sh5678

# hash of the above

hashb3 = hashlib.sha256(sum1to8.encode()).hexdigest()
print(hashb3)

# hash1to8= 'f3cdb2dd088fadd91587edcacd6c2fa54e53834c109f4faa039a34b69e7d262a'

node= sum1to8 + blockhash9
merklehash = hashlib.sha256(node.encode()).hexdigest()
print (merklehash)

merkleh = '868604a3d3de38c009470f7afe5b9efec2f8dd4edc1ef9451f39af3b017038ee'

# hence the merkle hash is '868604a3d3de38c009470f7afe5b9efec2f8dd4edc1ef9451f39af3b017038ee'