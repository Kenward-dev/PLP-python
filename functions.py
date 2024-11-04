price = int(input('Enter the price: '))

discount_percent = int(input('Enter the discount percentage: '))

def calculate_discount(price, discount_percent):
    if not isinstance(price, int) or not isinstance(discount_percent, int):
        raise ValueError("Price and discount percentage must be integers.")
    
    elif discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        discounted_price = price - discount_amount
        print(f"price = {discounted_price}")
    
    else:
        print(f"price = {price}")
        
calculate_discount(price, discount_percent)