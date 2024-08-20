# Write a program to fill in a letter template given below with name and date.

letter = ''' Dear <|Name|>,
  You are selected!
  <|Date|> '''

print(letter.replace("<|Name|>", "Mayank").replace(
    "<|Date|>", "7/6/2024"))  # Chaining of replace function

# letter = letter.replace("<|Name|>", "Mayank")
# print(letter.replace("<|Date|>", "7/6/2024"))

# New thing learn
# if we want to replace a word in a already replaced string it can be directly by above syntax
