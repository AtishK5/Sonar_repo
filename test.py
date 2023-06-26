def calculate_sum(a, b):
    sum = a + b
    return sum

def calculate_product(a, b):
    product = a * b
    return product

def main():
    num1 = 5
    num2 = 10

    result_sum = calculate_sum(num1, num2)
    result_product = calculate_product(num1, num2)

    print("Sum:", result_sum)
    print("Product:", result_product)

if __name__ == "__main__":
    main()
