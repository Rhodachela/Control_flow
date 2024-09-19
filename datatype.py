value = input("Enter a value (string or number): ")

# Attempt to convert value to int or float
def convert_value(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value  # It's a string if conversion fails

converted_value = convert_value(value)

match converted_value:
    case int():
        print("You have entered an integer:", converted_value)
    case float():
        print("You have entered a float:", converted_value)
    case str():
        print("You have entered a string:", converted_value)
    case _:
        print("You have entered an invalid data type!")
