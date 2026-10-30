def detect_repeated_words(paragraph):
    # Normalize case and remove punctuation
    text = paragraph.lower()
    for char in [',', '.', '!', '?', ':', ';']:
        text = text.replace(char, '')

    words = text.split()
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    print("\n--- Case Study 36: Repeated Word Detection ---")
    for word, count in word_counts.items():
        if count > 1:
            print(f"Word '{word}' appears {count} times.")


# Example Usage
sample_paragraph = "Python is great. Programming in Python is fun, and learning Python opens new doors."
detect_repeated_words(sample_paragraph)