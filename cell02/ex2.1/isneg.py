def main():
    try:
        num = float(input("Enter a number:20 ").strip())  
        if num < 0:
            print("This number is negative.")
        elif num > 0:
            print("This number is positive.")
        else:
            print("This number is zero.")  
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
