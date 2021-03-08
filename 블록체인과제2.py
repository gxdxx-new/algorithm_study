from cryptography.fernet import Fernet

key = Fernet.generate_key()

cipherSuite = Fernet(key)

fr = open("data.txt", 'rb')
cipherText = cipherSuite.encrypt(fr.read())
fr.close()

fw = open("encrypted.txt", 'wb')
fw.write(cipherText)
fw.close()

fr2 = open("encrypted.txt", 'rb')
plainText = cipherSuite.decrypt(fr2.read())
fr2.close()

print(plainText)