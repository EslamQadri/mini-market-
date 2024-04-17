import random
import string


def random_code():
    def generate_random_string(length):
        # Define the characters and digits that can be used in the random string
        characters = string.ascii_lowercase + string.digits  # letters (both lowercase and uppercase) + digits

        # Generate a random string of the specified length
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

    # Example: Generate a random string of length 10
    random_string = generate_random_string(14)
    return random_string