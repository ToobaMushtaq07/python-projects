#password lenth  checker
import logging
logging.basicConfig(level=logging.ERROR, format="%(levelname)s: %(message)s")
class WeakPasswordError(Exception):
    pass
try:
    password = input("Enter password: ")
    if len(password) < 8:
        raise WeakPasswordError("Password must be at least 8 characters long.")
    print("Password accepted.")
except WeakPasswordError as e:
    logging.error(e)



#Marks validation
import logging

logging.basicConfig(level=logging.ERROR, format="%(levelname)s: %(message)s")

class InvalidMarksError(Exception):
    pass

try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")

    print("Valid marks.")

except InvalidMarksError as e:
    logging.error(e)
except ValueError:
    logging.error("Invalid input.")