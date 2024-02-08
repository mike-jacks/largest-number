class LargestNumberCalculator:
    def __init__(self): pass

    def find_largest_number(self, num1: float, num2: float, num3: float) -> float:
        largest_number = num1
        if num2 > largest_number:
            largest_number = num2
        if num3 > largest_number:
            largest_number = num3
        return largest_number

def main():
    largest_number_calculator = LargestNumberCalculator()
    largest_number = largest_number_calculator(3, 7, 6)
    print(largest_number)

if __name__ == "__main__":
    main()
