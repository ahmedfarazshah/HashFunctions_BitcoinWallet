# def logic(x, y):
#     return x + y +50

# logic(5, 6)

# print(logic)

import hashlib
#open file and read
downloaded_file= "Lab6.pdf"
with open(downloaded_file,"rb") as file:
    file_data= file.read()
 #now divide the file into 8 equal parts
def blockSize():
   block_Size = len(file_data) //1024
   return block_Size
   blockSize()
blocks=[file_data[i:i+blockSize()] for i in range(0,len(file_data),blockSize())]
    # Step 3: Calculate SHA-256 hashes for each block
def generatehashes():
   block_hashes = [hashlib.sha256(block).hexdigest() for block in blocks]
   return block_hashes
# Step 4: Concatenate the hashes to generate the Merkle tree
merkle_tree = generatehashes().copy()
while len(merkle_tree) > 1:
    temp_tree = []
    for i in range(0, len(merkle_tree), 2):
        left_hash = merkle_tree[i]
        right_hash = merkle_tree[i+1] if i+1 < len(merkle_tree) else merkle_tree[i]
        merged_hash = hashlib.sha256((left_hash + right_hash).encode()).hexdigest()
        temp_tree.append(merged_hash)
    merkle_tree = temp_tree
# Step 5: Print the Merkle root
merkle_root = merkle_tree[0]
print("Merkle Root:", merkle_root)