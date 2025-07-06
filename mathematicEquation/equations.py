import math

# --- 1. Area and Perimeter Calculations ---

def calculate_rectangle_area_perimeter(length, width):
    """
    Calculates the area and perimeter of a rectangle.

    Args:
        length (float or int): The length of the rectangle.
        width (float or int): The width of the rectangle.

    Returns:
        tuple: A tuple containing (area, perimeter).
    """
    if length <= 0 or width <= 0:
        return "Invalid input: Length and width must be positive.", "Invalid input: Length and width must be positive."
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def calculate_circle_area_perimeter(radius):
    """
    Calculates the area and circumference (perimeter) of a circle.

    Args:
        radius (float or int): The radius of the circle.

    Returns:
        tuple: A tuple containing (area, circumference).
    """
    if radius <= 0:
        return "Invalid input: Radius must be positive.", "Invalid input: Radius must be positive."
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return area, circumference

def calculate_square_area_perimeter(side):
    """
    Calculates the area and perimeter of a square.

    Args:
        side (float or int): The length of the side of the square.

    Returns:
        tuple: A tuple containing (area, perimeter).
    """
    if side <= 0:
        return "Invalid input: Side length must be positive.", "Invalid input: Side length must be positive."
    area = side * side
    perimeter = 4 * side
    return area, perimeter

# --- 2. Average Calculation ---

def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.

    Args:
        numbers (list): A list of numbers (integers or floats).

    Returns:
        float or str: The average of the numbers, or an error message if the list is empty.
    """
    if not isinstance(numbers, list):
        return "Input must be a list of numbers."
    if not numbers:
        return "Cannot calculate average of an empty list."
    
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

# --- 3. Constant Values ---

def get_mathematical_constants():
    """
    Returns common mathematical constant values.

    Returns:
        dict: A dictionary containing common mathematical constants.
    """
    return {
        "Pi (π)": math.pi,
        "Euler's number (e)": math.e,
        "Tau (τ)": math.tau, # Tau is 2*pi
        "Infinity": float('inf'),
        "Not a Number (NaN)": float('nan')
    }

# --- 4. Multiplication Table ---

def generate_multiplication_table(value, limit):
    """
    Generates a multiplication table for a given value up to a specified limit.

    Args:
        value (int or float): The number for which to generate the table.
        limit (int): The upper limit for multiplication (e.g., if limit is 10, it goes up to value * 10).

    Returns:
        list: A list of strings, each representing a line in the multiplication table.
              Returns an error message if limit is not a positive integer.
    """
    if not isinstance(limit, int) or limit <= 0:
        return ["Invalid limit: Limit must be a positive integer."]

    table_lines = []
    print(f"\n--- Multiplication Table for {value} up to {limit} ---")
    for i in range(1, limit + 1):
        result = value * i
        line = f"{value} x {i} = {result}"
        print(line)
        table_lines.append(line)
    return table_lines # Returning the list of lines if you want to use them programmatically

