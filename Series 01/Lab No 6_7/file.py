# part 1 hash sha 256(1d0ada7a906e529d19fb2aca66911eaaee84ff4c7c6b685f019cd79c2deec5ff)
# part 2 hash sha 256(6c8ed1b6a6745bc64645ce63e23c9258545de0bf1c3c8efdfb3fad46d5d1fb6c)
# part 3 hash sha 256(c43194ab05fca649152ea3b92c49eacee99902badd7ea503e3315d49a83781ba)
# part 4 hash sha 256(b349939cb094a89e4cf720b895df300c0d5c7b3f0f3a237bc026cad42637fb61)

import hashlib
part1 = '1d0ada7a906e529d19fb2aca66911eaaee84ff4c7c6b685f019cd79c2deec5ff'
part2 = '6c8ed1b6a6745bc64645ce63e23c9258545de0bf1c3c8efdfb3fad46d5d1fb6c'
part3 = 'c43194ab05fca649152ea3b92c49eacee99902badd7ea503e3315d49a83781ba'
part4 = 'b349939cb094a89e4cf720b895df300c0d5c7b3f0f3a237bc026cad42637fb61'


sum12 = part1 + part2
print(sum12)
sumof12 = ('1d0ada7a906e529d19fb2aca66911eaaee84ff4c7c6b685f019cd79c2deec5ff6c8ed1b6a6745bc64645ce63e23c9258545de0bf1c3c8efdfb3fad46d5d1fb6c')
hashsum12 = hashlib.sha256(sumof12.encode()).hexdigest()
print (hashsum12)
hashof12 =('a1d1f83cb2b5fcf557e6cae6962774ebfba159cea5d43c4a8ebb61a02a7a67bf')


sum34 = part3 + part4
print(sum34)
sumof34 = ('c43194ab05fca649152ea3b92c49eacee99902badd7ea503e3315d49a83781bab349939cb094a89e4cf720b895df300c0d5c7b3f0f3a237bc026cad42637fb61')
hashsum34 = hashlib.sha256(sumof34.encode()).hexdigest()
print(hashsum34)
hashof34 =('02d937710a779508721c03e1637064e652d183a4e5d1da28d0f25538c4bcaf9b')


merkle = hashof12 + hashof34
print (merkle)
merkle = 'a1d1f83cb2b5fcf557e6cae6962774ebfba159cea5d43c4a8ebb61a02a7a67bf02d937710a779508721c03e1637064e652d183a4e5d1da28d0f25538c4bcaf9b'

merklehash = hashlib.sha256(merkle.encode()).hexdigest()
print(merklehash)

# merklehash = 448ec525a32f5f92dd9ef89c40829d0eb7c2edd59cb1639b92aea49af1ba76bc

                # or for the last you can do
                # 

# merklehash = hashlib.sha256((hashof12+hashof34).encode()).hexdigest()
# print(merklehash)
