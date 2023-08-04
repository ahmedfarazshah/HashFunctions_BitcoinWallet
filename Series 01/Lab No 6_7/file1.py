part1 = 'Blockchain.com (formerly Blockchain.info) is a cryptocurrency financial services company'
part2 = 'The company began as the first Bitcoin blockchain explorer in 2011'
part3 = 'later created a cryptocurrency wallet that accounted for 28% of bitcoin transactions between 2012 and 2020.'
part4 = 'It also operates a cryptocurrency exchange'
part5 = 'provides institutional markets lending business and data, charts, and analytics.'
part6 = 'Blockchain.com is a private company'
part7 = 'The company is led by CEO Peter Smith'
part8 = 'Blockchain.info was established by Ben Reeves in 2011.'

import hashlib

# def hashing(part1,part2,part3,part4,part5,part6,part7,part8):
#     return hashlib.sha256((part1,part2,part3,part4,part5,part6,part7,part8).encode()).hexdigest()
# print(hashing)
# hashing(part1)

hashp1 = hashlib.sha256(part8.encode()).hexdigest()
print(hashp1)
parth1 = 'cc3d0e39c2316a008ec5932c6d57c4999ff390cd8ef38f44781014a380774119'
parth2 = '90f9a38014d98be90d9a07b85765aeb1872330813671d21c9cf01343fbe7a308'
parth3 = '0adf82d847b59af8dd70678b1e798dc2061d8e75d32703aea5fd09dabcd9de65'
parth4 = '8345e58646940c112b06521b675a4654fc41d81443c2232d47198c3a54944d62'
parth5 = 'a97265688763d2a000c287cf86e0fe793ea0c09fd8d4e99b3f400fcc8aa48bd6'
parth6 = '014445333d5dd73c04cb643f6261f7133f636401fc7e5bdf1bd49f288cf6f6a4'
parth7 = 'f721d362869beed94fc56edf7a526f424d881f65501806d93277347778c18fdd'
parth8 = '0386ce21736e364647eed4848076f4a738172488dc37430a406a9a7dba014f8d'

# first four parts

sumhp12 = parth1 + parth2
sumhp34 = parth3 + parth4
sumhp56 = parth5 + parth6
sumhp78 = parth7 + parth8

hashp2 = hashlib.sha256(sumhp78.encode()).hexdigest()
print(hashp2)

hashp12 = 'd83510150804d6b17b0244827698bd526a915e245f080f7c7f71c4eddff4ebbc'
hashp34 = '96411fa24b8c9b5a992ecbf3125a147dd751b9a08a3048c4dacd17d7fd1fb176'
hashp56 = '8b5cc9d825ead707a75ab3f146ebe8f265c5b59b65a4329a60d263971709b1c3'
hashp78 = 'f8eb4400454ac510f7ec84723c85b0d7b5df11ae80ed3c07a3305d341d52b479'

# sum of hashes

sum_of_hash1234 = hashp12 + hashp34
sum_of_hash5678 = hashp56 + hashp78

# hashes

hashp3 = hashlib.sha256(sum_of_hash5678.encode()).hexdigest()
print(hashp3)
node_hash1234 = '8b6b3c1a3c8e008b66d80295a649c00806620f4caf08286a09e107c00c62f1d5'
node_hash5678 = '6fc8da5b094b20525901f517df01106ef5c7bed5ff4af4b7459055e8c855ec20'

# sum
merklesum = node_hash1234 + node_hash5678

merklehash= hashlib.sha256(merklesum.encode()).hexdigest()
print(merklehash)

# hence merkle hash is "185e6099f00f9f8a6828255f70a6766c22dd9cd27743bf4adfb241cbf40208e2"