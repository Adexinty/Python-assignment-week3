# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage to apply.
    
    Returns:
    - float: The final price after discount if discount is 20% or more, 
             otherwise the original price.
    """
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Subtract the discount from the original price
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, return original price
        return price

# Prompt user for input and display the final price
try:
    # Ask user for the original price of the item
    price = float(input("Enter the original price of the item: $"))
    
    # Ask user for the discount percentage
    discount = float(input("Enter the discount percentage: "))

    # Calculate the final price using the function
    final_price = calculate_discount(price, discount)

    # Check if discount was applied and print the appropriate message
    if discount >= 20:
        print(f"Discount applied. Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price: ${final_price:.2f}")
except ValueError:
    # Handle cases where the user input is not a valid number
    print("Please enter valid numeric values for price and discount percentage.")
