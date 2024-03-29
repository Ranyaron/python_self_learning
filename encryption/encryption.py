from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key = key.exportKey()
file_out = open('private.pem', 'wb')
file_out.write(private_key)
print(private_key)

public_key = key.publickey().exportKey()
file_out = open('receiver.pem', 'wb')
file_out.write(public_key)
print(public_key)
