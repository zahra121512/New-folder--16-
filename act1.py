def decimal_to_binary(decimal_number):
  binary_number = ""
  for i in range(decimal_number.bit_length()):
    remainder = decimal_number >> i & 1
    binary_number = str(remainder) + binary_number

  # Handle negative numbers using a while loop
  if decimal_number < 0:
    while binary_number[0] == '0':
      binary_number = binary_number[1:]

  return binary_number

# Get the decimal number from the user
decimal_number = int(input("Enter a decimal number: "))

# Convert the decimal number to binary
binary_number = decimal_to_binary(decimal_number)

# Print the result
print("The binary equivalent of", decimal_number, "is", binary_number)