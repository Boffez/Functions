
def hide(card_number):
    """Mask the credit card number, showing only the first two and last four digits."""
    if len(card_number) != 16:
        raise ValueError("Card number must be 16 digits long.")
    
    return card_number[:2] + '*' * 10 + card_number[-4:]