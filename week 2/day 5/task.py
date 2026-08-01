import logging

# Configure logging
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Custom Exception
class InvalidAgeError(Exception):
    """Raised when the age is less than 18."""
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    print("Access Granted!")

except InvalidAgeError as e:
    logging.error(e)

except ValueError:
    logging.error("Invalid input! Please enter a number.")