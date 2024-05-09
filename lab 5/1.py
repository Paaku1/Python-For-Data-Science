def scrabble_score(word):
    # Define the dictionary mapping each letter to its Scrabble™ score
    scores = {
        'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }

    # Calculate the total score for the word
    total_score = 0
    for letter in word:
        if letter.upper() in scores:  # Convert letter to uppercase to match keys
            total_score += scores[letter.upper()]
        else:
            return "Error: Contains non-alphabet character"

    return f"{word.upper()} is worth {total_score} points."

# Get user input
input_word = input("Enter a word to score: ")
print(scrabble_score(input_word))
