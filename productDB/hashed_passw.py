from passlib.context import CryptContext

pwd_co = CryptContext(schemes = ['bcrypt'],deprecated = 'auto')

class Hashed():
    def cryp(password:str):
        hashed = pwd_co.hash(password)
        return hashed