import re
from collections import Counter

text = input("Enter your paragraph:\n")

words = text.split()
total_words = len(words)

total_characters = len(text)

characters_without_spaces = len(text.replace(" ", ""))

sentences = re.split(r"[.!?]+", text)
sentences = [sentence for sentence in sentences if sentence.strip()]
number_of_sentences = len(sentences)

cleaned_text = re.sub(r"[^\w\s]", "", text.lower())
cleaned_words = cleaned_text.split()

if cleaned_words:
    most_frequent_word = Counter(cleaned_words).most_common(1)[0]
else:
    most_frequent_word = None

print("\n--- Word Counter Results ---")
print("Total words:", total_words)
print("Total characters:", total_characters)
print("Characters excluding spaces:", characters_without_spaces)
print("Number of sentences:", number_of_sentences)

if most_frequent_word:
    print("Most frequent word:", most_frequent_word[0])
    print("Frequency:", most_frequent_word[1])
else:
    print("Most frequent word: None")