# Program to spell out a name using the ICAO phonetic alphabet


def icao_word(letter):
    icao_alphabet = {
        'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
        'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
        'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
        'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
        'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
        'Y': 'Yankee', 'Z': 'Zulu'
    }
    return icao_alphabet.get(letter.upper(), letter)  # Return the letter itself if not found


name = input("Enter a name to spell out: ")

# Spell out the name using the ICAO phonetic alphabet
spelled_out_name = [icao_word(letter) for letter in name if letter.isalpha() or letter.isspace()]


print("Spelled out name:", ' '.join(spelled_out_name))