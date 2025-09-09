# Author : Melissa Vento-Wolverton
# Date Deadline: 9/10/2025
# File Name : cipher.py
# Project #1
# Description : 
''' For Project 1, you are required to write a detailed report explaining how you decrypted the
provided ciphertext below, which was encrypted using a substitution cipher. Begin by
describing the concept of substitution ciphers and their vulnerability to frequency analysis. In
your favorite programming language, either Python or C++, write a program to calculate the
relative frequency of all letters A–Z in the ciphertext. Compare these frequencies with the
general English language letter frequencies provided in Table 1.1, focusing on substituting letters
with closely matching frequency values. Since the ciphertext is relatively short, note that its letter
frequencies may not perfectly align with standard English frequencies, so iterative refinement
will be necessary. Document your approach, the challenges you encountered, and how you
adjusted substitutions to make the decrypted text coherent.

Include screenshots of your program, the intermediate results, and the final output in the report.
Additionally, provide the link to your executable code on an online platform, such as Google
Colab (https://colab.research.google.com), where reviewers can run your code and verify the
results. Report of your work should be exported into a PDF file, ensuring it contains the detailed
explanation of each step, the screenshots, and the online code link. Submit the final PDF file on
Brightspace. Your report should be clear, thorough, and demonstrate both the logic behind your
approach and the practical implementation of your solution. The ciphertext is given below: '''

# Author : Melissa Vento-Wolverton
# Date Deadline: 9/10/2025
# File Name : cipher.py
# Project #1
# Description : Substitution cipher decryption using frequency analysis and manual overrides

import re

# Step 1: Read ciphertext
with open('cipher.txt', 'r') as file:
    text = file.read()

# Step 2: Frequency analysis
letters_only = re.findall(r'[a-z]', text)
freq = {}
for letter in letters_only:
    freq[letter] = freq.get(letter, 0) + 1

# Step 3: Sort letters by frequency (descending)
sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
sorted_letters = [item[0] for item in sorted_freq]

print("Letter Frequency (Most used to least used):")
for letter, count in sorted_freq:
    print(f"{letter}: {count}")

# Step 4: Initial mapping using frequency analysis
freq_order = 'etaoinshrdlucmfwypvbgkjqxz'  # English letter frequency
substitution_map = {}
for cipher_letter, eng_letter in zip(sorted_letters, freq_order):
    substitution_map[cipher_letter] = eng_letter

# Keep a copy of initial frequency-based mapping for reporting
freq_based_map = substitution_map.copy()

# Step 5: Manual overrides for context (applied AFTER initial guess)
manual_overrides = {
    'x': 'f',  # 'oc' -> 'of'
    'w': 'i',  # single-letter words
    'j': 'o',  # if-> of
    'n': 'u',  # stfdy ->study
    'q': 'd',  # vata -> data
    'a': 'a',  #  correct "that the"
    'e': 'e'   # from  :the"




}
substitution_map.update(manual_overrides)

# Step 6: Decode text using final substitution map
decoded_text = ''.join(substitution_map.get(c, c) if c.islower() else c for c in text)

# Step 7: Output frequency-based mapping
print("\nInitial Frequency-Based Map (cipher => guessed letter):")
for cipher_letter in sorted_letters:
    print(f"{cipher_letter} => {freq_based_map.get(cipher_letter)}")

# Step 8: Output final substitution map
print("\nFinal Substitution Map with Manual Overrides:")
for cipher_letter in sorted_letters:
    print(f"{cipher_letter} => {substitution_map.get(cipher_letter)}")

# Step 9: Output decoded text
print("\nDecoded Text Guess:")
print(decoded_text)
