def calculate_bmr(gender, weight, height, age):
    """Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict Equation."""
    if gender == "male":
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == "female":
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Invalid gender. Please enter 'male' or 'female'.")

def get_activity_factor():
    """Get the activity level from the user and return the corresponding factor."""
    print("\nChoose your activity level:")
    print("1. Sedentary (little or no exercise)")
    print("2. Lightly active (light exercise/sports 1-3 days/week)")
    print("3. Moderately active (moderate exercise/sports 3-5 days/week)")
    print("4. Very active (hard exercise/sports 6-7 days/week)")
    print("5. Extra active (very hard exercise/sports & physical job)")
    
    while True:
        try:
            choice = int(input("Enter the number (1-5): "))
            if 1 <= choice <= 5:
                return [1.2, 1.375, 1.55, 1.725, 1.9][choice - 1]
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def feet_inches_to_cm(height_ft_in):
    """Convert height from feet.inches format to centimeters."""
    feet, inches = map(float, height_ft_in.split('.'))
    return (feet * 30.48) + (inches * 2.54)

def get_user_input():
    """Get user details (gender, age, weight, height in feet.inches format)."""
    while True:
        gender = input("Enter your gender (male/female): ").strip().lower()
        if gender in ["male", "female"]:
            break
        else:
            print("Invalid gender! Please enter 'male' or 'female'.")
    
    while True:
        try:
            age = int(input("Enter your age (years): "))
            weight = float(input("Enter your weight (kg): "))
            height_ft_in = input("Enter your height in feet.inches (e.g., 5.11 for 5 feet 11 inches): ")
            feet, inches = map(float, height_ft_in.split('.'))
            if age > 0 and weight > 0 and feet >= 0 and 0 <= inches < 12:
                height = feet_inches_to_cm(height_ft_in)
                return gender, age, weight, height
            else:
                print("Invalid input! Age and weight must be positive, and height must be valid (e.g., 5.11).")
        except ValueError:
            print("Invalid input! Please enter numeric values.")

def main():
    """Main function to calculate maintenance calories."""
    print("Welcome to the Maintenance Calorie Calculator!")
    
    while True:
        gender, age, weight, height = get_user_input()
        activity_factor = get_activity_factor()
        
        # Calculate BMR
        bmr = calculate_bmr(gender, weight, height, age)
        
        # Calculate maintenance calories
        maintenance_calories = bmr * activity_factor
        
        # Display results
        print(f"\nYour Basal Metabolic Rate (BMR) is: {bmr:.2f} calories/day")
        print(f"Your estimated maintenance calories are: {maintenance_calories:.2f} calories/day")
        
        # Ask if the user wants to calculate again
        again = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for using the Maintenance Calorie Calculator. Goodbye!")
            break

# Run the program
main()