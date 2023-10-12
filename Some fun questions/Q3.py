def count_vowels(word):
    vowels = "aeiou"
    count = 0
    word = word.lower()
    for char in word:
        if char in vowels:
            count += 1
    return count


def reverse_string(sentence):
    reversed_sentence = ""
    word = ""
    i = len(sentence) - 1
    while i >= 0:
        if sentence[i] == " ":
            reversed_sentence += word[::-1] + " "
            word = ""
        else:
            word += sentence[i]
        i -= 1
    reversed_sentence += word[::-1]
    return reversed_sentence


def main():
    sentence_input = input("Enter a sentence: ")
    vowels_count = count_vowels(sentence_input)
    print(f"The number of vowels in '{sentence_input }' is: {vowels_count}")
    reversed_sentence = reverse_string(sentence_input)
    print(f"The reversed sentence is: {reversed_sentence}")

main()
