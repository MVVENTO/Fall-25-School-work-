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

import re

# Step 1: 
# Read the text file (cipher plaintext)
with open('cipher.txt', 'r') as file:
    text = file.read()

# Step 2: 
# Use regex to fina all letters a-z
letters_only = re.findall(r'[a-z]', text)

# Step 3:
# Manually Count letter Frequency
freq = {}
for letter in letters_only:
    if letter in freq:
        freq[letter] += 1
    else:
        freq[letter] = 1

# Step 4 :
# Sort letters by Frequency (High to low)
sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
sorted_letters = [item[0] for item in sorted_freq]

# Step 5:
# Sort Letters by Frequency (High to low)
print("Letter Frequency (Sorted Most used to least used):")
for letter, count in sorted_freq:
    print(f"{letter}: {count}")

# Results : 
