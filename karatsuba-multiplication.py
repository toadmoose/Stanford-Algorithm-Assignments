def karatsuba(x, y):
    # Base case for recursion
    if x < 10 or y < 10:
        return x * y
    
    # Calculate the number of digits
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split the digit sequences
    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)

    # 3 recursive calls
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

# The two 64-digit numbers
num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627

# Calculate the product
result = karatsuba(num1, num2)

print(result)
