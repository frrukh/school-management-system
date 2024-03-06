def generate_password(length):
    import random
    import string
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(length))
    print(password)

generate_password(12)