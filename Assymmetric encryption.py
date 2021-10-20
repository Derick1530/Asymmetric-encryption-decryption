from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Generating a key
print("""Derick Zihalirwa & Aliyu  
 ////////////////////////
//  -Practical Part-  //
///////////////////////
""")
private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
public_key = private_key.public_key()

# Storing the keys

pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

with open('Bank/private_key.pem', 'wb') as f:
    f.write(pem)
with open('Grace/private_key.pem', 'wb') as f:
    f.write(pem)
pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )


with open('public_key.pem', 'wb') as f:
    f.write(pem)

f = open('Bank/info.txt', 'rb')
message = f.read()
f.close()

encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
f = open('Grace/info.encrypted', 'wb')
f.write(encrypted)
f.close()
# Grace RECEIVED THE ENCRYPTED MESSAGE
# AND AUTOMATICALLY THE SYSTEM WILL DECRYPTED IT USING THE PRIVATE KEY of GRACE
original_message = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
with open('Grace/Bank_info.txt','wb') as f:
    f.write(original_message)


#Hacker
#
#
# decrypted = public_key.decrypt()
# with open("Hacker/plainText.text", 'wb') as f:
#         f.write(decrypted)