import os
import base64

# Generate a 32-byte (256-bit) secure random key
secure_key = base64.b64encode(os.urandom(32)).decode('utf-8')
print(secure_key)
