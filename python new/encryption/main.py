import cryptography
from cryptography.fernet import Fernet


def crypto(text, task):
    key = b'umG8xc9yTbg4kn72FO4h0XKPCbTaCtpxTVVrk-gTUbs='
    crypter = Fernet(key)
    try:
        if task == 'e':
            pw = crypter.encrypt(text.encode())
            return str(pw, 'utf8')
        elif task == 'd':
            pw = crypter.decrypt(text.encode())
            return str(pw, 'utf8')
    except Exception:
        return f'Something went wrong: {Exception}'


print(crypto('gAAAAABg9nHvtn0cLJVSHi_8JXGtRPpyW_DSsnjq24Jlp4U07DA7oXqAOPlkiMuVLDWjiyWvBlAOTlpcCnr4sKEKsgXX_6xlbg==', 'd'))