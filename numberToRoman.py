def int_to_roman(num):
    # Mapping of integers to Roman numeral components
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    roman_numeral = ""
    for i in range(len(val)):
        while num >= val[i]:  # Check if the current value fits into the number
            roman_numeral += syms[i]  # Append the corresponding Roman numeral
            num -= val[i]  # Reduce the number by the value
    
    return roman_numeral

# Example usage
number = 2025
print(f"The Roman numeral for {number} is {int_to_roman(number)}.")
