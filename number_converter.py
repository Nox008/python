def words_to_num(text):
    ones = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16,
        "seventeen": 17, "eighteen": 18, "nineteen": 19
    }
    
    tens = {
        "twenty": 20, "thirty": 30, "forty": 40,
        "fifty": 50, "sixty": 60, "seventy": 70,
        "eighty": 80, "ninety": 90
    }
    
    multiples = {
        "hundred": 100, "thousand": 1000, "million": 1000000
    }
    
    words = text.lower().replace("-", " ").split()
    total = 0
    current = 0
    
    for word in words:
        if word in ones:
            current += ones[word]
        elif word in tens:
            current += tens[word]
        elif word == "hundred":
            current *= multiples[word]
        elif word in ["thousand", "million"]:
            current *= multiples[word]
            total += current
            current = 0
        elif word == "and":
            continue
        else:
            raise ValueError(f"Unknown word: {word}")
    
    return total + current


# Example usage:
text = str(input("Enter Your Number in  Words:"))
print(words_to_num(text))  # Output: 1233
