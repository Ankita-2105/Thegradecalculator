# ----------------------------------------------------------------------
# Python Grade Calculator
# This script calculates the final course percentage based on weighted scores
# for homework, midterms, and final exams, and assigns a letter grade.
# ----------------------------------------------------------------------

# ---1. GREETING AND INTRODUCTION ---
print("\n================================")
print("    WEIGHTED GRADE CALCULATOR ")
print("==================================")
print("Please enter the weights (as percentages) and")
print("your scores (as a percentage) for each category.")
print("Example: Enter '20' for a 20% weight or '92.5' for a score.\n")

# ---2. INPUT COLLECTION AND DATA CONVERSION (Gathering Weights) ---
# Function to get a valid weight input
def get_weight_input(category):
    while True:
        try:
            weight = float(input(f"Enter the weight for {category} (in %): "))
            if 0 <= weight <= 100:
                return weight / 100  # Convert percentage to decimal
            else:
                print("Please enter a valid weight between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
# Function to get a valid score input
def get_score_input(category):
    while True:
        try:
            score = float(input(f"Enter your score for {category} (in %): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a valid score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
# Collect weights
homework_weight = get_weight_input("Homework")
midterm_weight = get_weight_input("Midterms")
final_weight = get_weight_input("Final Exam")
# Validate total weight
total_weight = homework_weight + midterm_weight + final_weight
if total_weight != 1.0:
    print("\nError: The total weight must equal 100%. Please restart the program and try again.")
    exit()
# Collect scores
homework_score = get_score_input("Homework")
midterm_score = get_score_input("Midterms")
final_score = get_score_input("Final Exam")
# ---3. CALCULATION OF FINAL PERCENTAGE ---
final_percentage = (homework_score * homework_weight +
                    midterm_score * midterm_weight +
                    final_score * final_weight)
# ---4. DETERMINATION OF LETTER GRADE ---
if final_percentage >= 90:

    letter_grade = 'A'
elif final_percentage >= 80:
    letter_grade = 'B'
elif final_percentage >= 70:
    letter_grade = 'C'
elif final_percentage >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'
# ---5. OUTPUT OF RESULTS ---
print("\n================================")
print("          FINAL RESULTS         ")
print("==================================")
print(f"Your final course percentage is: {final_percentage:.2f}%")
print(f"Your letter grade is: {letter_grade}")
print("==================================\n")


# End of the Grade Calculator Script

