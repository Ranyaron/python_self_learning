from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

with open('test/test.txt', 'wb') as out_file:
    recipient_key = RSA.importKey(open('receiver.pem').read())

    session_key = get_random_bytes(16)

    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    out_file.write(cipher_rsa.encrypt(session_key))

    cipher_aes = AES.new(session_key, AES.MODE_ECB)
    data = b'blah blah blah Python blah blah'
    ciphertext, tag = cipher_aes.encrypt(data)

    out_file.write(cipher_aes.nonce)
    out_file.write(tag)
    out_file.write(ciphertext)