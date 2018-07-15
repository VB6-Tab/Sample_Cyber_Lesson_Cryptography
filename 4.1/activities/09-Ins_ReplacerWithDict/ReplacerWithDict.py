# A dict of vowels as keys with their shifted forms as the values
shifty_dicty = {
  "a":"b",
  "e":"f",
  "i":"j",
  "o":"p",
  "u":"v",
  "y":"z"
}

# The original message and the variable the encoded message will be placed in
original_message = "this is the original message! Hooray!"
encoded_message = ""

# Loop through the original message character by character
for character in original_message:

  # Check to see if the current character is one of the keys in the dictionary
  if(character in shifty_dicty.keys()):

    # Use the current character as the index to place the new value into encoded_message
    encoded_message += shifty_dicty[character]
  
  # If the character is not a key in the dictionary, simply place the current character into encoded_message
  else:
    encoded_message += character

print(encoded_message)