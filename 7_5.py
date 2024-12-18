
from number_in_range import is_within_range

def main():
    
    number = int(input("A number: "))

    
    x = 2
    y = 15

    
    result = is_within_range(number, x, y)

    
    if result:
        print(f"Number {number} in the range <{x},{y}>: yes")
    else:
        print(f"Number {number} in the range <{x},{y}>: no")


if __name__ == "__main__":
    main()