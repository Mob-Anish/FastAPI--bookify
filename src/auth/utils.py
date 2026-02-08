from passlib.context import CryptContext

password_context = CryptContext(
    schemes=['bcrypt']
)

# Create encrypted password
def create_hash_password(password: str) -> str:
    hash = password_context.hash(password)

    return hash

# Verify the password from login users
def verify_password(password: str, hash: str) -> bool:
    return password_context.verify(password, hash)
