from mean_var_std import calculate
import test_module  # included for testing

def main():
    # Example usage
    data = [0,1,2,3,4,5,6,7,8]
    result = calculate(data)
    print("Calculation result:")
    for key, value in result.items():
        print(f"{key}: {value}")
    
    # Run unit tests from test_module.py
    print("\nRunning unit tests...")
    test_module.run_tests()  # assuming test_module has a run_tests() function

if __name__ == "__main__":
    main()
