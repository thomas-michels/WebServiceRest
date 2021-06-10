from fastapi.security import OAuth2PasswordBearer

OAUTH2 = OAuth2PasswordBearer(tokenUrl='/')
