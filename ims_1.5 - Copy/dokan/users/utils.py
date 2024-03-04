import random
import string

def generate_unique_workspace_identifier(username):
    # Concatenate username with a random string
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return f"{username}_{random_string}"
