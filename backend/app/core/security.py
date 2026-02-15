import jwt
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

class Security:
    def __init__(self, secret_key, algorithm='HS256'):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.expiration_time = timedelta(hours=1)  # Token expiration time

    def generate_token(self, user_id):
        expiration = datetime.utcnow() + self.expiration_time
        token = jwt.encode({'user_id': user_id, 'exp': expiration}, self.secret_key, algorithm=self.algorithm)
        return token

    def verify_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            return None  # Token has expired
        except jwt.InvalidTokenError:
            return None  # Invalid token

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)

    @staticmethod
    def check_password(hashed_password, password):
        return check_password_hash(hashed_password, password)