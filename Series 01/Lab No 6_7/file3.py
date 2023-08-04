import hashlib

file = 'd:/BlockChain/Lab No 6/Lab 6-6-2023.pdf'

# Determining and spliting the file as per block size
blocksize = len(file) // 8 
datablocks = [file[i:i+blocksize]for i in range(0, len(file),blocksize)]
print (datablocks)

block1 = 'd:/B'
block2 = 'lock'
block3 = 'Chai'
block4 = 'n/La'
block5 = 'b No'
block6 = '6/L'
block7 = 'ab 6'
block8 = '-6-2'
block9 = '023'
block10 = 'pdf'

hashb = hashlib.sha256(block10.encode()).hexdigest()
print(hashb)
blockhash1 = '25159a03232340e5c989a854cf4b8730a0446b0790029955cb18e73d000b350b'
blockhash2 = '0c030586945fe504b604ecc2e875c38ede400cd5cd73da9730302162e6b02c6f'
blockhash3 = 'b1e160b3fbfb8c7f562239715e76e8502d0a8bec215c941480321b57a760b0d7'
blockhash4 = 'ba488b3d01ba86e61376f5345781803c735ca5992141b37cbb55b325378c76db'
blockhash5 = '8a9a60b2c3ee4fddfb28b007533bb6506aa174063c49d17221049400e404a76a'
blockhash6 = 'ee16d537a302806f4995b286816715f1de608aeb97f15ec7613e0e15c8192b62'
blockhash7 = 'c90e2853804e8f1d31ee3d7f0d03b533299315a801d5e63519d50f99e3c4c50e'
blockhash8 = '7a636c6bd9fee0755be642164fda9f02c3f03708d70e5cf94583b1d894ca05f0'
blockhash9 = '168167b979b5fbf412591964c809645cd7d13b52627f208fc1508dd7e6046886'
blockhash10 = 'c35b21d6ca39aa7cc3b79a705d989f1a6e88b99ab43988d74048799e3db926a3'

# sum of the hashes

bh12 =  blockhash1 + blockhash2
bh34 = blockhash3 + blockhash4
bh56 = blockhash5 + blockhash6
bh78 = blockhash7 + blockhash8
bh90 = blockhash9 + blockhash10

# now hashes of the above

hashb1 = hashlib.sha256(bh90.encode()).hexdigest()
print(hashb1)

hash_bh12 = '667f7dd41e89b7efafd44d586b77b2fc857ed6b42f616db28f75209a7651018a'
hash_bh34 = '27fbbb9bc29d71884d104022d45b5e3edb955f88596d129cec344f5bb01e7aca'
hash_bh56 = '63e70d34b5e7cb087aff288237baa0e460319825793e4d7794f418568a3766af'
hash_bh78 = 'aabe23ffb16f92f12abcc6cded0f8fb4a26f108b87cfdee525a8a018c3351859'
hash_bh90 = '514aefa149b022b1f63095fa88690c3612775a07b8cffd2b54ac7e26dead7070'

# sum of the above hashes

sh1234 = hash_bh12 + hash_bh34
sh5678 = hash_bh56 + hash_bh78

# now hashes of the above sum

hashb2 = hashlib.sha256(sh5678.encode()).hexdigest()
print(hashb2)

hash_sh1234 = 'de46cd92b158480c917e4fefe1f7725e729bdefb47d3445d2e560e62fe6cd6df'
hash_sh5678 = '678133ff9cc7d7944ac4c8e892967e204af9beda5db8b46b615ddce9bef790c4'

# sum of the above

sum1to8 = hash_sh1234 + hash_sh5678

# hash of the above

hashb3 = hashlib.sha256(sum1to8.encode()).hexdigest()
print(hashb3)

hash1to8= 'f9e71a2fd09b8901f795bf9bb0d3fe30312d26b8f3af294c569c17d28eda819a'
# hash_bh90 = '514aefa149b022b1f63095fa88690c3612775a07b8cffd2b54ac7e26dead7070'

node = hash1to8 + hash_bh90
merklehash = hashlib.sha256(node.encode()).hexdigest()
print(merklehash)

# hence the merkle hash is '6714ed9072ea405bad09f6326e59d8f83bfdad9bda859df31aa7899737742dbc'
            # '6714ed9072ea405bad09f6326e59d8f83bfdad9bda859df31aa7899737742dbc'