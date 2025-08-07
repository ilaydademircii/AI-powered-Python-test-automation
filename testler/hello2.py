

# C:/Users/zehra/demo/testler/hello2.py test edilecek dosyanın path demo proje adı testler paket hello2 module
# C:/Users/zehra/demo/Calistir.py   test kodunun yapıştırılacağı path
def factorial(n):
    if n < 0:
        raise ValueError("Negative values are not allowed.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


# Main function to test the factorial function
if __name__ == "__main__":
    try:
        print("Factorial of 5 is:", factorial(5))  # Expected output: 120
        print("Factorial of 0 is:", factorial(0))  # Expected output: 1
    except Exception as e:
        print(f"Error: {e}")
