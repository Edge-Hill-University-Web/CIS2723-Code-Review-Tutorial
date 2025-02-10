import datetime

def calculate_age(birth_year):
    current_year = datetime.datetime.now().year
    return current_year - birth_year

def format_username(first_name, last_name):
    return first_name.lower() + '.' + last_name.lower()

def divide_numbers(a, b):
    return a / b

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def process_numbers(numbers):
    """
    This function takes a list of numbers and returns their product.
    It iterates over the list and multiplies each number together.
    """
    total = 0
    for num in numbers:
        total += num  # Could use built-in sum()
    return total

def greet_user(name):
    print("Hello, " + name + "! Welcome to our system.")

def caluclate_discount(price, discount):  # Issue: Typo in function name
    return price - (price * discount / 100)

def do_thing(x, y):  # Issue: Unclear purpose
    result = x * y - x + y
    return result

# Example function calls (for testing purposes)
if __name__ == "__main__":
    print(calculate_age(2025))  # Issue: Future year
    print(format_username("John", "Doe"))
    print(divide_numbers(10, 0))  # Issue: Division by zero
    print(read_file("non_existent_file.txt"))  # Issue: File does not exist
    print(process_numbers([1, 2, 3, 4, 5]))
    greet_user("Alice")
    print(caluclate_discount(100, 10))  # Issue: Function name typo
    print(do_thing(5, 3))  # Issue: Unclear purpose
