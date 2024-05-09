def validate_license_plate(plate):
    length = len(plate)
    
    if length == 6:
        # Check older style format (ABC123)
        if all(c.isupper() for c in plate[:3]) and all(c.isdigit() for c in plate[3:]):
            return "The plate is a valid older style plate."
        else:
            return "The plate is not valid."
    elif length == 7:
        # Check newer style format (1234ABC)
        if all(c.isdigit() for c in plate[:4]) and all(c.isupper() for c in plate[4:]):
            return "The plate is a valid newer style plate."
        else:
            return "The plate is not valid."
    else:
        # If length does not match either format, it's invalid
        return "The plate is not valid."

# Input from the user
user_input = input("Enter the license plate: ")
# Output the validation result
print(validate_license_plate(user_input))
