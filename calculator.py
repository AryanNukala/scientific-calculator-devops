import math
#for testing the webhok.
class ScientificCalculator:
    """Scientific Calculator with menu-driven operations"""
    
    def square_root(self, x):
        """Calculate square root of x"""
        if x < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(x)
    
    def factorial(self, x):
        """Calculate factorial of x"""
        if x < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if not isinstance(x, int):
            raise ValueError("Factorial only defined for integers")
        return math.factorial(x)
    
    def natural_log(self, x):
        """Calculate natural logarithm (base e) of x"""
        if x <= 0:
            raise ValueError("Natural log only defined for positive numbers")
        return math.log(x)
    
    def power(self, x, b):
        """Calculate x raised to power b"""
        return math.pow(x, b)

def display_menu():
    """Display calculator menu"""
    print("\n" + "="*50)
    print("     SCIENTIFIC CALCULATOR")
    print("="*50)
    print("1. Square Root (√x)")
    print("2. Factorial (x!)")
    print("3. Natural Logarithm (ln x)")
    print("4. Power (x^b)")
    print("5. Exit")
    print("="*50)

def main():
    """Main function to run calculator"""
    calc = ScientificCalculator()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '5':
            print("\nThank you for using Scientific Calculator!")
            break
        
        try:
            if choice == '1':
                x = float(input("Enter number: "))
                result = calc.square_root(x)
                print(f"\n√{x} = {result}")
            
            elif choice == '2':
                x = int(input("Enter integer: "))
                result = calc.factorial(x)
                print(f"\n{x}! = {result}")
            
            elif choice == '3':
                x = float(input("Enter number: "))
                result = calc.natural_log(x)
                print(f"\nln({x}) = {result}")
            
            elif choice == '4':
                x = float(input("Enter base (x): "))
                b = float(input("Enter exponent (b): "))
                result = calc.power(x, b)
                print(f"\n{x}^{b} = {result}")
            
            else:
                print("\nInvalid choice! Please select 1-5.")
        
        except ValueError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()