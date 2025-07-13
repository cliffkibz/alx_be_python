# Ask the user for their current age
current_age_str = input("How old are you? ")

# Convert the input to an integer
current_age = int(current_age_str)

# Years between 2023 and 2050
years_until_2050 = 2050 - 2023  # 27 years

# Calculate future age
age_in_2050 = current_age + years_until_2050

# Display the result
print(f"In 2050, you will be {age_in_2050} years old.")

