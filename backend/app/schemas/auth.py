from pydantic import BaseModel, EmailStr

# Model for User Registration
class UserRegistrationRequest(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str

# Model for User Login
class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str

# Model for Authentication Response
class AuthResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int

# Model for Refresh Token Response
class RefreshTokenResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
