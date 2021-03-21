from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.fernet import Fernet
import time

private_key = rsa.generate_private_key( # 개인 키 생성
    public_exponent=65537,            # e: 65537이나 3을 이용 (대부분 65537)
    key_size=2048,                    # n의 비트 수: 512보다 커야 한다
    backend=default_backend()
)
public_key = private_key.public_key()   # 공개 키 생성

start = time.time()

messages = []
with open(r"C:\Users\남기돈\Desktop\data.txt", "rb") as f:
    message = f.read(190)
    while message != b"":
        messages.append(message)
        message = f.read(190)

# 암호화
encrypted_message = []
for message in messages:
    encrypted = public_key.encrypt(
        message,
        padding.OAEP(                   # OAEP: Optimal Asymmetric Encryption Padding
            mgf=padding.MGF1(algorithm=hashes.SHA256()),    # 짧은 메시지에 패딩을 추가
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    encrypted_message.append(encrypted)

# 복호화
original_message = []
for message in encrypted_message:
    original = private_key.decrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    original_message.append(original)

end = time.time()

if(messages == original_message):
    print(end - start)

fr = open(r"C:\Users\남기돈\Desktop\data.txt", "rb")
key = Fernet.generate_key()
f = Fernet(key)

start2 = time.time()

token = f.encrypt(fr.read())
d = f.decrypt(token)

end2 = time.time()

print(end2 - start2)

fr.close()