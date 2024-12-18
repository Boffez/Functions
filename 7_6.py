from hide_card_num import hide

def main():
    card_number = input("Enter a credit card number (16 digits): ")

    try:
        masked_card_number = hide(card_number)

        print(f"Masked credit card number: {masked_card_number}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()