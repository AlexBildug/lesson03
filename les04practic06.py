start_number = int(input("Enter start number:"))
end_number = int(input("Enter end number:"))

# Generate elements from start_number to end_number (including)
my_count = 0
for element in range(start_number, end_number + 1):
    # Check if this element is the prime number
    is_prime = True
    for divider in range(2, element):
        # If we've found any divider the remainder of which is zero
        # So current element is not the prime number
        if divider > 1 and element % divider == 0:
            is_prime = False
            break

    # Current element is the prime number
    if is_prime:
        print(element)
        my_count += 1

print("Total count of prime numbers")
print(my_count)