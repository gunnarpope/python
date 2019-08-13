
import os, hashlib, binascii
from base64 import b64encode
password = 'password'
salt = b64encode(os.urandom(32)).decode('utf-8')
print('salt: ', salt)
dk = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), b'salt', 100000)
token = b64encode(dk).decode('utf-8') 
#token = binascii.hexlify(dk)
print(token)
