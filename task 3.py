def count_words(text):
    """
    Counts the frequency of each unique word in the given text.
    Returns a dictionary with words as keys and their frequencies as values.
    """
    skips = [".", ",", ":", ";", "'", '"']  # Characters to skip
    for ch in skips:
        text = text.replace(ch, "")  # Remove punctuation
    word_counts = {}
    for word in text.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def main():
    # Read text from user input or a file
    user_input = input("Enter your text or provide a filename: ")
    try:
        with open(user_input, "r") as file:
            text = file.read()
    except FileNotFoundError:
        text = user_input

    # Calculate word frequencies
    word_frequencies = count_words(text.lower())

    # Display results
    print("\nWord Frequencies:")
    for word, frequency in word_frequencies.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()
