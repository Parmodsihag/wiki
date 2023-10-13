from django.test import TestCase

# # Create your tests here.
if __name__ == "__main__":
    def calculate_actual_price(reduced_price, discount_percentage):
        # Convert the discount percentage to a decimal
        discount_decimal = discount_percentage / 100.0

        # Calculate the actual price
        actual_price = reduced_price / (1 - discount_decimal)

        return actual_price

    # Given values
    reduced_price = 72422
    discount_percentage = 2

    # Calculate the actual price
    actual_price = calculate_actual_price(reduced_price, discount_percentage)

    # Print the result
    print(f"The actual price is: {actual_price}")
