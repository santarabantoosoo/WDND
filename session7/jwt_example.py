import jwt
import base64

payload = {'name': 'Omar Gaber'}
algo = 'HS256'  # HMAC-SHA 256
secret = 'learning'

print('_______________JWT_______________')
encoded_jwt = jwt.encode(payload, secret, algorithm=algo)
print(encoded_jwt)
print('______________________________')

# secret = 'learningss'
print('_______________DECODE_______________')
decoded_jwt = jwt.decode(encoded_jwt, secret, verify=True)
print(decoded_jwt)
print('______________________________')


# print(str(encoded_jwt).split("."))
# print(str(encoded_jwt).split(".")[1]+"==")
# decoded_base64 = base64.b64decode(str(encoded_jwt).split(".")[1]+"==")
# print(decoded_base64)


# JWT EXERCISE
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXJrIjoiY2VudHJhbCBwYXJrIn0.H7sytXDEHK1fOyOYkII5aFfzEZqGIro0Erw_84jZuGc'

header = base64.b64decode(str(token).split(".")[1]+'==')
print(header)
